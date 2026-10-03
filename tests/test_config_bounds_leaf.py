"""``utils.config_bounds`` stays a leaf, and the CLI stays off the modules it freed (#780).

``config.schema`` used to import ``layer_stream`` and ``ship_verdict`` only for a few
bounds, and that put ``layer_stream``, ``layer_shard``, ``async_disk_source`` and
``safetensors_reader`` on the ``soup version`` import path. The bounds now live in a
leaf that imports nothing, and the old owners re-export them, so the schema's bound
and the runtime validator's message still come from one definition.

Three things keep that true, and each is checked here rather than trusted:

* the leaf imports nothing from ``soup_cli`` (otherwise it is not a leaf);
* after ``import soup_cli.cli`` those modules are not in ``sys.modules``;
* each old owner re-exports the leaf's OBJECT, not a copy that could drift.

The ``sys.modules`` checks run in a FRESH subprocess, for the reason
``test_cli_startup_is_light`` gives: the pytest process has already imported these
modules through other tests, so an in-process assertion would prove nothing.
"""

from __future__ import annotations

import ast
import importlib
import subprocess
import sys
from pathlib import Path

import pytest

from soup_cli.utils import config_bounds

_PROBE = (
    "import sys\n"
    "{statements}\n"
    "print('\\n'.join(sorted(m for m in sys.modules if m.startswith('soup_cli'))))\n"
)

# Before #780 the schema imported layer_stream, and layer_stream (and through it
# layer_shard, async_disk_source and safetensors_reader) was on the CLI path for
# nothing but the bounds above. Nothing else on the CLI path imports them eagerly.
_OFF_THE_CLI_PATH = (
    "soup_cli.utils.layer_stream",
    "soup_cli.utils.layer_shard",
    "soup_cli.utils.async_disk_source",
    "soup_cli.utils.safetensors_reader",
)

_STREAM_BOUNDS = (
    "MIN_STREAM_BUFFERS",
    "MAX_STREAM_BUFFERS",
    "DEFAULT_STREAM_BUFFERS",
    "MIN_STREAM_READ_AHEAD",
    "MAX_STREAM_READ_AHEAD",
    "DEFAULT_STREAM_READ_AHEAD",
    "SUPPORTED_STREAM_TASKS",
    "ROLLOUT_STREAM_TASKS",
)
_NOISE_FLOOR_BOUNDS = ("MIN_NOISE_FLOOR_RUNS", "MAX_NOISE_FLOOR_RUNS")

# (module, name it exposes, name in the leaf)
_REEXPORTS = (
    [("soup_cli.utils.layer_stream", name, name) for name in _STREAM_BOUNDS]
    + [
        ("soup_cli.utils.async_disk_source", name, name)
        for name in (
            "MIN_STREAM_READ_AHEAD",
            "MAX_STREAM_READ_AHEAD",
            "DEFAULT_STREAM_READ_AHEAD",
        )
    ]
    + [("soup_cli.utils.ship_verdict", name, name) for name in _NOISE_FLOOR_BOUNDS]
    + [
        ("soup_cli.config.schema", "_STREAM_SUPPORTED_TASKS", "SUPPORTED_STREAM_TASKS"),
        ("soup_cli.config.schema", "_STREAM_ROLLOUT_TASKS", "ROLLOUT_STREAM_TASKS"),
    ]
)


def _soup_modules_after(statements: str) -> set[str]:
    """Run ``statements`` in a clean interpreter; return the soup_cli modules it loaded."""
    proc = subprocess.run(
        [sys.executable, "-c", _PROBE.format(statements=statements)],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, (proc.stdout, proc.stderr)
    return set(proc.stdout.split())


@pytest.fixture(scope="module")
def modules_after_cli_import() -> set[str]:
    return _soup_modules_after("import soup_cli.cli")


def test_leaf_imports_nothing_from_soup_cli():
    """AST, so a function-local or conditional import is caught too."""
    tree = ast.parse(Path(config_bounds.__file__).read_text(encoding="utf-8"))
    offenders = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and (
            node.level or (node.module or "").startswith("soup_cli")
        ):
            offenders.append(ast.unparse(node))
        elif isinstance(node, ast.Import) and any(
            alias.name.startswith("soup_cli") for alias in node.names
        ):
            offenders.append(ast.unparse(node))
    assert not offenders, (
        f"config_bounds must stay a leaf, but it imports {offenders}. Put the new "
        "dependency on the side that needs it, not in the leaf."
    )


def test_importing_the_leaf_loads_no_other_soup_cli_module():
    """Runtime twin of the AST check: nothing arrives transitively either."""
    assert _soup_modules_after("import soup_cli.utils.config_bounds") == {
        "soup_cli",
        "soup_cli.utils",
        "soup_cli.utils.config_bounds",
    }


@pytest.mark.parametrize("module", _OFF_THE_CLI_PATH)
def test_cli_import_does_not_load_the_freed_modules(module, modules_after_cli_import):
    assert module not in modules_after_cli_import, (
        f"`import soup_cli.cli` loads {module} again, which puts it back on the "
        "`soup version` path (#780). Run `python -X importtime -c 'import soup_cli.cli'` "
        "to see which eager import brought it in."
    )


def test_probe_would_catch_a_regression():
    """Control: the probe must actually see these modules when they ARE imported.

    Without it, a probe that silently returned an empty set (wrong prefix, changed
    output format) would make the test above pass forever while proving nothing.
    """
    imports = "".join(f"import {module}\n" for module in _OFF_THE_CLI_PATH)
    loaded = _soup_modules_after(imports + "import soup_cli.cli")
    assert set(_OFF_THE_CLI_PATH) <= loaded


@pytest.mark.parametrize(("module", "name", "leaf_name"), _REEXPORTS)
def test_old_owner_re_exports_the_leafs_object(module, name, leaf_name):
    """One definition: a copy that could drift would defeat the leaf's whole point."""
    assert getattr(importlib.import_module(module), name) is getattr(config_bounds, leaf_name)


@pytest.mark.parametrize(
    "module",
    [
        "soup_cli.utils.layer_stream",
        "soup_cli.utils.async_disk_source",
        "soup_cli.utils.ship_verdict",
    ],
)
def test_old_owner_does_not_redeclare_a_bound(module):
    """The identity check above cannot see a copy of a small int (CPython caches 2, 8, 10).

    A redeclared ``MAX_STREAM_BUFFERS = 8`` passes ``is`` until someone changes one of
    the two, so also refuse the assignment itself.
    """
    leaf_names = {name for name in vars(config_bounds) if name.isupper()}
    tree = ast.parse(Path(importlib.import_module(module).__file__).read_text(encoding="utf-8"))
    assigned = set()
    for node in tree.body:
        targets = node.targets if isinstance(node, ast.Assign) else [getattr(node, "target", None)]
        assigned |= {t.id for t in targets if isinstance(t, ast.Name)}
    assert not assigned & leaf_names, (
        f"{module} assigns {sorted(assigned & leaf_names)}; these are defined once in "
        "config_bounds and only imported elsewhere."
    )
