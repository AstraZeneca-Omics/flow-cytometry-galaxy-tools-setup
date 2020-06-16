#!/bin/bash

for s in single-cell-ebi-gxa single-cell-IUC; do
  SOURCE_FILE=$s.yaml.lock
  echo "Modifying $SOURCE_FILE..."
  sed 's/\(tool_panel_section_id:\).*\(hca_sc_.*\)$/\1 hca_sc_all/' $SOURCE_FILE > $s.mod.yaml.lock
  rm $SOURCE_FILE
done
