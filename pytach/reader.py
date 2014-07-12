import os
import glob
import json
import inspect

base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
print base_path

def read_path(path):    
    files = glob.glob(base_path + path + '/*.json')
    config = {}
    for file in files:
        with open(file) as json_file:
            json_data = json.load(json_file)
            config[json_data['name']] = json_data

    return config

def read_file(file):
    with open(base_path + file) as json_file:
        return json.load(json_file)