#!/bin/bash

EXPERIMENT_INPUT="$1"
file_name=logs/execution_00.log
counter=0

while [ -e "${file_name}" ]; do
  file_name=$(printf '%s_%02d.log' "logs/execution" "$(( ++counter ))")
done

script -c "PYTHONPATH=. python3 runner.py ${EXPERIMENT_INPUT}" -f "${file_name}"