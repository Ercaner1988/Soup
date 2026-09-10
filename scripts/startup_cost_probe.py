"""Measure `soup` CLI startup cost and where it goes.

Throwaway measurement harness for the startup-cost report — stdlib only, no
project imports in this process, every figure taken from a fresh interpreter so
warm module caches cannot flatter a result.

    python scripts/startup_cost_probe.py

Reports min and median of N cold subprocess runs per variant, then the largest
cumulative `-X importtime` subtrees for `import soup_cli.cli`. Only the
*relative* shares of the importtime block are meaningful: the profiler inflates
its own totals well past the wall-clock figures above it.
"""

from __future__ import annotations

import platform
import shutil
import statistics
import subprocess
import sys
import time

RUNS = 7

# (label, argv) — the decomposition, cheapest first, so each line is the
# previous line plus one layer.
VARIANTS: list[tuple[str, list[str]]] = [
    ("interpreter floor", [sys.executable, "-c", "pass"]),
    ("+ typer + rich", [sys.executable, "-c", "import typer, rich.console"]),
    ("soup_cli.config.schema", [sys.executable, "-c", "import soup_cli.config.schema"]),
    ("soup_cli.cli", [sys.executable, "-c", "import soup_cli.cli"]),
    ("python -m soup_cli version", [sys.executable, "-m", "soup_cli", "version"]),
    ("python -m soup_cli --help", [sys.executable, "-m", "soup_cli", "--help"]),
]


def _bench(argv: list[str], runs: int = RUNS) -> tuple[float, float]:
    timings = []
    for _ in range(runs):
        started = time.perf_counter()
        proc = subprocess.run(argv, capture_output=True)
        timings.append(time.perf_counter() - started)
        if proc.returncode != 0:
            raise SystemExit(
                f"{' '.join(argv)} exited {proc.returncode}\n"
                f"{proc.stdout.decode(errors='replace')}\n"
                f"{proc.stderr.decode(errors='replace')}"
            )
    return min(timings), statistics.median(timings)


def _importtime_tree(limit: int = 12) -> list[tuple[float, str]]:
    """Largest cumulative subtrees for ``import soup_cli.cli``."""
    proc = subprocess.run(
        [sys.executable, "-X", "importtime", "-c", "import soup_cli.cli"],
        capture_output=True,
        text=True,
        errors="replace",
    )
    rows: list[tuple[float, str]] = []
    for line in proc.stderr.splitlines():
        parts = line.split("|")
        if len(parts) != 3:
            continue
        try:
            cumulative = float(parts[1].strip())
        except ValueError:  # the header row
            continue
        rows.append((cumulative / 1000.0, parts[2].rstrip()))
    rows.sort(reverse=True)
    return rows[:limit]


def main() -> None:
    print(f"{platform.platform()}")
    print(f"python {sys.version.split()[0]} ({platform.machine()})")
    print(f"`soup` console script: {shutil.which('soup') or 'NOT ON PATH'}")
    print(f"{RUNS} cold subprocess runs per variant\n")

    print(f"{'variant':30s} {'min':>10s} {'median':>10s}")
    for label, argv in VARIANTS:
        low, median = _bench(argv)
        print(f"{label:30s} {low * 1000:9.1f}ms {median * 1000:9.1f}ms")

    if shutil.which("soup"):
        for label, argv in [("soup version", ["soup", "version"]), ("soup --help", ["soup", "--help"])]:
            low, median = _bench(argv)
            print(f"{label:30s} {low * 1000:9.1f}ms {median * 1000:9.1f}ms")

    print("\n-X importtime, largest cumulative subtrees (RELATIVE shares only):")
    for cumulative, name in _importtime_tree():
        print(f"  {cumulative:9.1f}ms  {name}")


if __name__ == "__main__":
    main()
