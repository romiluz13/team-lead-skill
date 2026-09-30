#!/bin/sh
set -eu
SIM_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$SIM_ROOT/run.py" "$@"
