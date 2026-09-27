"""``utils/config_bounds.py`` must stay a leaf, and keep the streaming runtime off
the ``soup version`` import path (#780).

``config/schema.py`` takes its stream-buffer, read-ahead and noise-floor bounds
from the leaf. If the leaf grows a ``soup_cli`` import, or the schema goes back to
importing ``layer_stream``, six modules (``layer_stream``, ``layer_shard``,
``async_disk_source``, ``safetensors_reader``, ``queue``, ``_queue``) creep back
onto CLI startup with no other test noticing.
"""

from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

import pytest

import soup_cli.utils.async_disk_source as async_disk_source
import soup_cli.utils.config_bounds as config_bounds
import soup_cli.utils.layer_stream as layer_stream
import soup_cli.utils.ship_verdict as ship_verdict


def _imported_modules(path: Path) -> list[str]:
    names = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.append(node.module or "")
    return names


def test_leaf_imports_nothing_from_soup_cli():
    imported = _imported_modules(Path(config_bounds.__file__))
    offenders = [m for m in imported if m == "soup_cli" or m.startswith("soup_cli.")]
    assert not offenders, (
        f"config_bounds imports {offenders}; it must stay a dependency-free leaf "
        "or the schema drags that module's subtree onto `soup version` again."
    )


def _in_modules_after(code: str, module: str) -> bool:
    proc = subprocess.run(
        [sys.executable, "-c", f"import sys\n{code}\nprint({module!r} in sys.modules)"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, (proc.stdout, proc.stderr)
    return proc.stdout.strip() == "True"


def test_cli_import_does_not_load_layer_stream():
    assert not _in_modules_after("import soup_cli.cli", "soup_cli.utils.layer_stream"), (
        "`import soup_cli.cli` loaded soup_cli.utils.layer_stream. Something on the "
        "CLI import path imports it eagerly; config bounds belong in utils/config_bounds."
    )


def test_probe_would_catch_layer_stream():
    """Control: the probe must report the module when it IS loaded."""
    assert _in_modules_after(
        "import soup_cli.cli\nimport soup_cli.utils.layer_stream",
        "soup_cli.utils.layer_stream",
    )


@pytest.mark.parametrize(
    ("module", "name"),
    [
        (layer_stream, "MIN_STREAM_BUFFERS"),
        (layer_stream, "MAX_STREAM_BUFFERS"),
        (layer_stream, "DEFAULT_STREAM_BUFFERS"),
        (layer_stream, "MIN_STREAM_READ_AHEAD"),
        (layer_stream, "MAX_STREAM_READ_AHEAD"),
        (layer_stream, "DEFAULT_STREAM_READ_AHEAD"),
        (layer_stream, "SUPPORTED_STREAM_TASKS"),
        (layer_stream, "ROLLOUT_STREAM_TASKS"),
        (async_disk_source, "MIN_STREAM_READ_AHEAD"),
        (async_disk_source, "MAX_STREAM_READ_AHEAD"),
        (async_disk_source, "DEFAULT_STREAM_READ_AHEAD"),
        (ship_verdict, "MIN_NOISE_FLOOR_RUNS"),
        (ship_verdict, "MAX_NOISE_FLOOR_RUNS"),
    ],
    ids=lambda v: v.__name__.rsplit(".", 1)[-1] if hasattr(v, "__name__") else v,
)
def test_runtime_reexports_the_leaf_instead_of_redeclaring(module, name):
    """Re-exported, not copied: a redeclared value could drift from the schema bound.

    Checked on the source, not with ``is``: CPython caches small ints, so a copied
    ``MIN_STREAM_BUFFERS = 2`` would still be identical to the leaf's object.
    """
    tree = ast.parse(Path(module.__file__).read_text(encoding="utf-8"))
    from_leaf = {
        alias.asname or alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module == "soup_cli.utils.config_bounds"
        for alias in node.names
    }
    assigned = {
        target.id
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (node.targets if isinstance(node, ast.Assign) else [node.target])
        if isinstance(target, ast.Name)
    }
    assert name in from_leaf, f"{module.__name__} must import {name} from config_bounds"
    assert name not in assigned, f"{module.__name__} redeclares {name}; re-export it instead"
    assert getattr(module, name) is getattr(config_bounds, name)
