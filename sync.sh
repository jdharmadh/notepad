#!/bin/bash

echo "Syncing...."

source ~/.conda.zshrc >/dev/null 2>&1
conda activate >/dev/null 2>&1

python3 fmt_script.py >/dev/null 2>&1

scp -r assets/ "$SERVER_HOSTNAME":/root/rustyservice/html/notepad >/dev/null 2>&1
scp -r _posts/ "$SERVER_HOSTNAME":/root/rustyservice/html/notepad >/dev/null 2>&1

echo "Done."
