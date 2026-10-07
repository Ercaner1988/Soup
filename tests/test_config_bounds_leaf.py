<<<<<<< HEAD
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

=======
"""``utils/config_bounds.py`` must stay a leaf, and keep the streaming runtime off
the ``soup version`` import path (#780).

``config/schema.py`` takes its stream-buffer, read-ahead and noise-floor bounds
from the leaf. If the leaf grows an import, or the schema goes back to importing
a runtime module, six modules (``layer_stream``, ``layer_shard``,
``async_disk_source``, ``safetensors_reader``, ``queue``, ``_queue``) creep back
onto CLI startup with no other test noticing.
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
"""

from __future__ import annotations

import ast
<<<<<<< HEAD
import importlib

=======
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
import subprocess
import sys
from pathlib import Path

import pytest

<<<<<<< HEAD
from soup_cli.utils import config_bounds

_PROBE = (
    "import sys\n"
    "{statements}\n"
    "print('\\n'.join(sorted(m for m in sys.modules if m.startswith('soup_cli'))))\n"
)

# Before #780 the schema imported layer_stream, and layer_stream (and through it
# layer_shard, async_disk_source and safetensors_reader) was on the CLI path for
# nothing but the bounds above. Nothing else on the CLI path imports them eagerly.

=======
import soup_cli.config.schema as schema
import soup_cli.utils.async_disk_source as async_disk_source
import soup_cli.utils.config_bounds as config_bounds
import soup_cli.utils.layer_stream as layer_stream
import soup_cli.utils.ship_verdict as ship_verdict

# queue/_queue are left out: a third-party dependency may import them on some
# Python or platform, which would make the assertion flaky for non-Soup reasons.
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
_OFF_THE_CLI_PATH = (
    "soup_cli.utils.layer_stream",
    "soup_cli.utils.layer_shard",
    "soup_cli.utils.async_disk_source",
    "soup_cli.utils.safetensors_reader",
)

<<<<<<< HEAD
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

=======

def _imported_modules(path: Path) -> list[str]:
    names = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.append(node.module or "")
    return names


def test_leaf_imports_nothing():
    imported = [m for m in _imported_modules(Path(config_bounds.__file__)) if m != "__future__"]
    assert not imported, (
        f"config_bounds imports {imported}; it must stay a leaf or the schema drags "
        "that module's subtree onto `soup version` (or `import soup_cli.config.schema`)."
    )


def _loaded_after(code: str, modules: tuple[str, ...]) -> list[str]:
    probe = f"import sys\n{code}\nprint(','.join(m for m in {modules!r} if m in sys.modules))"
    proc = subprocess.run(
        [sys.executable, "-c", probe], capture_output=True, text=True, timeout=300
    )
    assert proc.returncode == 0, (proc.stdout, proc.stderr)
    return [m for m in proc.stdout.strip().split(",") if m]


def test_cli_import_loads_none_of_the_streaming_runtime():
    loaded = _loaded_after("import soup_cli.cli", _OFF_THE_CLI_PATH)
    assert not loaded, (
        f"`import soup_cli.cli` loaded {loaded}. Something on the CLI import path "
        "imports the streaming runtime eagerly; config bounds belong in utils/config_bounds."
    )


def test_probe_reports_every_module_when_loaded():
    """Control: each name is reported when it IS loaded."""
    imports = "\n".join(f"import {m}" for m in _OFF_THE_CLI_PATH)
    assert _loaded_after(f"import soup_cli.cli\n{imports}", _OFF_THE_CLI_PATH) == list(
        _OFF_THE_CLI_PATH
    )


@pytest.mark.parametrize(
    ("module", "name", "leaf_name"),
    [
        (layer_stream, "MIN_STREAM_BUFFERS", "MIN_STREAM_BUFFERS"),
        (layer_stream, "MAX_STREAM_BUFFERS", "MAX_STREAM_BUFFERS"),
        (layer_stream, "DEFAULT_STREAM_BUFFERS", "DEFAULT_STREAM_BUFFERS"),
        (layer_stream, "MIN_STREAM_READ_AHEAD", "MIN_STREAM_READ_AHEAD"),
        (layer_stream, "MAX_STREAM_READ_AHEAD", "MAX_STREAM_READ_AHEAD"),
        (layer_stream, "DEFAULT_STREAM_READ_AHEAD", "DEFAULT_STREAM_READ_AHEAD"),
        (layer_stream, "SUPPORTED_STREAM_TASKS", "SUPPORTED_STREAM_TASKS"),
        (layer_stream, "ROLLOUT_STREAM_TASKS", "ROLLOUT_STREAM_TASKS"),
        (async_disk_source, "MIN_STREAM_READ_AHEAD", "MIN_STREAM_READ_AHEAD"),
        (async_disk_source, "MAX_STREAM_READ_AHEAD", "MAX_STREAM_READ_AHEAD"),
        (async_disk_source, "DEFAULT_STREAM_READ_AHEAD", "DEFAULT_STREAM_READ_AHEAD"),
        (ship_verdict, "MIN_NOISE_FLOOR_RUNS", "MIN_NOISE_FLOOR_RUNS"),
        (ship_verdict, "MAX_NOISE_FLOOR_RUNS", "MAX_NOISE_FLOOR_RUNS"),
        (schema, "MIN_STREAM_BUFFERS", "MIN_STREAM_BUFFERS"),
        (schema, "MAX_STREAM_BUFFERS", "MAX_STREAM_BUFFERS"),
        (schema, "DEFAULT_STREAM_BUFFERS", "DEFAULT_STREAM_BUFFERS"),
        (schema, "MIN_STREAM_READ_AHEAD", "MIN_STREAM_READ_AHEAD"),
        (schema, "MAX_STREAM_READ_AHEAD", "MAX_STREAM_READ_AHEAD"),
        (schema, "DEFAULT_STREAM_READ_AHEAD", "DEFAULT_STREAM_READ_AHEAD"),
        (schema, "_STREAM_SUPPORTED_TASKS", "SUPPORTED_STREAM_TASKS"),
        (schema, "_STREAM_ROLLOUT_TASKS", "ROLLOUT_STREAM_TASKS"),
        (schema, "MIN_NOISE_FLOOR_RUNS", "MIN_NOISE_FLOOR_RUNS"),
        (schema, "MAX_NOISE_FLOOR_RUNS", "MAX_NOISE_FLOOR_RUNS"),
    ],
    ids=lambda v: v.__name__.rsplit(".", 1)[-1] if hasattr(v, "__name__") else v,
)
def test_bound_comes_from_the_leaf_and_is_never_redeclared(module, name, leaf_name):
    """Re-exported, not copied: a redeclared value could drift from the schema bound.

    Checked on the source, not with ``is`` alone: CPython caches small ints, so a
    copied ``MIN_STREAM_BUFFERS = 2`` would still be identical to the leaf's object.
    Every ``Name`` in store context counts, so tuple unpacking, ``+=``, ``for``
    targets and the walrus operator are caught as well as a plain assignment.
    """
    tree = ast.parse(Path(module.__file__).read_text(encoding="utf-8"))
    from_leaf = {
        alias.asname or alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module == "soup_cli.utils.config_bounds"
        for alias in node.names
    }
    assigned = {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)
    }
    assert name in from_leaf, f"{module.__name__} must import {name} from config_bounds"
    assert name not in assigned, f"{module.__name__} redeclares {name}; re-export it instead"
    assert getattr(module, name) is getattr(config_bounds, leaf_name)
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
