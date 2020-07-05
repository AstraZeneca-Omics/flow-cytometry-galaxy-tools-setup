#!/bin/bash

for s in single-cell-ebi-gxa single-cell-IUC; do
    SOURCE_FILE=$s.yaml.lock
    echo "Modifying $SOURCE_FILE..."
    python reassign_sections.py --input $SOURCE_FILE --reassignment reassignments/$s.yaml --output $s.mod.yaml.lock
    rm $SOURCE_FILE
done
