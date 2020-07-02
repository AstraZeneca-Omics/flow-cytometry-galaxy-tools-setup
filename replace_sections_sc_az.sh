#!/bin/bash

for s in single-cell-ebi-gxa single-cell-IUC; do
  SOURCE_FILE=$s.yaml.lock
  echo "Modifying $SOURCE_FILE..."
  sed 's/\(tool_panel_section_id:\).*\(hca_sc_.*\)$/\1 hca_sc_all/' $SOURCE_FILE | \
      sed "s/tool_panel_section_label: 'Text Manipulation'/tool_panel_section_id: data_manipulation/" | \
      sed "s/tool_panel_section_label: 'RNA-Seq'/tool_panel_section_id: hca_sc_all" | \
      sed "s/tool_panel_section_label: FASTA/FASTQ manipulation/tool_panel_section_id: hca_sc_all" \
	  > $s.mod.yaml.lock
  rm $SOURCE_FILE
done
