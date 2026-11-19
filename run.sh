#!/usr/bin/env bash
python3 -m pip install --quiet -r requirements.txt >/dev/null 2>&1 || true
echo "Task ready: implement the function in solution.py and run pytest."
