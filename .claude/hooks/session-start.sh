#!/bin/bash
# Cloud-session setup for README/translation work on this fork: the package itself
# (core deps only; the [dev] extra pulls the full training stack) plus the tools the
# README sync ratchet, the changelog check and the linter need.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
python3 -m pip install --quiet --disable-pip-version-check -e . pytest pytest-cov ruff
