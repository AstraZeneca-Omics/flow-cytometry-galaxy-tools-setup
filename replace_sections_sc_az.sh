#!/bin/bash

SOURCE_FILE=single-cell-ebi-gxa.yaml.lock
sed 's/\(tool_panel_section_id:\).*\(hca_sc_.*\)$/\1 hca_sc_all/' $SOURCE_FILE > sc_mod_az.yaml.lock
rm $SOURCE_FILE
