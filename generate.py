#!/usr/bin/env python3

import yaml
from yamlinclude import YamlIncludeConstructor
from os import path
import glob
import json


GLOBALS = {
    'ROOT_URL': 'https://abouletonfilm.fr',
    'file://': 'file://out/'
}

HERE = path.dirname(path.realpath(__file__))
SRC = path.join(HERE, 'src')
OUT = path.join(HERE, 'out')
YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=SRC)


src_files = []
for src_file in glob.glob(path.join(SRC, "*.yml")):
    filename, _ = path.splitext(path.basename(src_file))

    # Read src ile
    with open(src_file, 'r') as f:
        content = f.read()
        for key, value in GLOBALS.items():
            content = content.replace(key, value)

        data = yaml.load(content, Loader=yaml.FullLoader)

        # Write out file
        out_file_path = path.join(OUT, f"{filename}.json")
        with open(out_file_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)
