#!/bin/bash
# postCreateCommand.sh

echo "START Install"

if [ ! -d .venv ]; then
    poetry config virtualenvs.in-project true --local
    poetry install
    ln -sf .venv/bin .
fi

sudo chown -R vscode:vscode .

echo "FINISH Install"