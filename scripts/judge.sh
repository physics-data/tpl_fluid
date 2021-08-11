#!/bin/bash

SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
DN="$(dirname "$SCRIPT_PATH")"
cd "${DN}/../"

rm -rf verdicts
mkdir verdicts

for i in $(seq 1 5); do
  echo "=================="
  echo "Input $i..."
  cp ./data/input.$i.json ./input.json
  python3 ./fluid.py
  echo "=================="
  echo "Running judger"
  python3 ./scripts/judge_one.py ./output.hdf5 ./data/ans.$i.hdf5 ./verdicts/$i.txt
done
