#!/usr/bin/env python3

import yaml
from yamlinclude import YamlIncludeConstructor
from os import path
import os
import glob
import json
import re
import io


GLOBALS = {
    'ROOT_URL': 'https://abouletonfilm.fr',
}


def replace_in_content(content):
    # Globals
    for key, value in GLOBALS.items():
        content = content.replace(key, value)
    
    return content


HERE = path.dirname(path.realpath(__file__))
SRC = path.join(HERE, 'src')
INCLUDE = path.join(SRC, "includes")
OUT = path.join(HERE, 'out')
YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader,
                                           base_dir=INCLUDE)


src_files = []

for src_file in glob.glob(path.join(SRC, "*.yml")):
    filename, _ = path.splitext(path.basename(src_file))

    # Read src ile
    with io.open(src_file, 'r', encoding='utf8') as f:
        content = f.read()
        
        data = yaml.load(content, Loader=yaml.FullLoader)
        json_str = json.dumps(data, indent=4)
        json_to_write = replace_in_content(json_str)

        out_file_path = path.join(OUT, f"{filename}.json")

        # Delete out file before writing it (i got a bug)
        os.remove(out_file_path)

        # Write out file
        with io.open(out_file_path, 'w', encoding='utf8') as outfile:
            outfile.write(json_to_write)
