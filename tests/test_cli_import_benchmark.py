"""CodSpeed regression gate for the CLI's own import cost (#780, #1065).

`soup version` and `soup --help` spend roughly half their cold-start cost --
240-300ms of a 410-680ms total, measured across three CI platforms in #780 --
importing `soup_cli.config.schema`, the dominant leaf in that profile. This
benchmark deletes that one module from `sys.modules` and re-imports it on
every CodSpeed iteration, so a PR that makes the schema tree more expensive
to build shows up as a percentage change on the PR instead of as an
unwritten cost, the way #780 itself was.

This is a different instrument than #780's own measurement, not a
replacement for it (per #1065): instruction counting inside one long-lived
interpreter, not a cold subprocess start. It will not reproduce #780's
absolute milliseconds -- OS and import-metadata caches stay warm across
iterations here, and interpreter startup itself isn't part of what's timed.
What it tracks is the same import graph's cost moving, relatively, PR to PR.

Deleting only this one leaf, not `soup_cli` wholesale, is deliberate: other
already-imported `soup_cli` modules keep their existing reference to the
parent `soup_cli.config` package, and the import machinery updates that
package's `schema` attribute to the freshly-built module on each iteration,
so nothing else in the test session is left pointing at a stale module.
"""

from __future__ import annotations

import importlib
import sys

_TARGET = "soup_cli.config.schema"


def _reimport_schema() -> None:
    sys.modules.pop(_TARGET, None)
    importlib.import_module(_TARGET)


def test_config_schema_import_cost(benchmark) -> None:
    benchmark(_reimport_schema)
