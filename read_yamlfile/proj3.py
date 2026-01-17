#learn retrieving paths, reading file, with/try/except
#https://note.nkmk.me/en/python-script-file-path/#get-the-absolute-path-of-the-current-script-file
#https://www.w3schools.com/python/python_try_except.asp

import os
#install yaml parser
#py -m pip install pyyaml
import yaml

#folder = os.getcwd()
folder = os.path.dirname(os.path.abspath(__file__))
yamlfile = os.path.join(folder ,"example.yaml")

if(os.path.exists(yamlfile)):
    with open(yamlfile) as stream:
        try:
            y = yaml.safe_load(stream)
            print(y)
        except yaml.YAMLError as exc:
            print("File read failed with error", exc)
        else:
            print("File read successfully.")
else:
    print(yamlfile, "doesn't exist")