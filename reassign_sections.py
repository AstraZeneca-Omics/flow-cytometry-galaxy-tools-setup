import yaml
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="YAML input with tools and sections to correct")
parser.add_argument("--reassignment", required=True, help="YAML reassignment for tools and sections to correct")
parser.add_argument("--output", required=True, help="YAML output for tools and sections to corrected")

args = parser.parse_args()

by_section = dict()
by_section_regexp = dict()
by_tool = dict()
by_section_label = dict()

with open(args.input, 'r') as i_file:
    install_file = yaml.load(i_file)

with open(args.reassignment) as r_file:
    reassignment = yaml.load(r_file)

    # load reassignments into memory, by section_id, by section_id_regexp, by section_label and by tool_id.
    for r in reassignment['reassign_to_section_id']:
        if 'section_id' in r:
            by_section[r['section_id']] = r['destination_section_id']
        elif 'section_id_regexp' in r:
            by_section_regexp[r['section_id_regexp']] = r['destination_section_id']
        elif 'section_label' in r:
            by_section_label[r['section_label']] = r['destination_section_id']
        elif 'tool_id' in r:
            by_tool[r['tool_id']] = r['destination_section_id']

# replace in the lock file the section ids with the following order of preference:
# A.- By exact match of tool_id
# B.- By exact match of tool_panel_section_id to one in by_section
# C.- By regexp match of tool_panel_section_id to one in by_section_regexp
# D.- By exact match of tool_panel_section_label to one in by_section_label
for tool in install_file['tools']:
    if tool['name'] in by_tool:
        tool['tool_panel_section_id'] = by_tool[tool['name']]
    elif 'tool_panel_section_id' in tool:
        if tool['tool_panel_section_id'] in by_section:
            tool['tool_panel_section_id'] = by_section[tool['tool_panel_section_id']]
        elif len(by_section_regexp) > 0:
            for k, v in by_section_regexp.items():
                if re.match(k, tool['tool_panel_section_id']):
                    tool['tool_panel_section_id'] = v
                    break
    elif 'tool_panel_section_label' in tool and tool['tool_panel_section_label'] in by_section_label:
        tool['tool_panel_section_id'] = by_section_label[tool['tool_panel_section_label']]
        del tool['tool_panel_section_label']

with open(args.output, 'w') as output:
    yaml.dump(install_file, output)