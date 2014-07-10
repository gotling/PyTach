import glob
import json

def read_path(path):
    files = glob.glob(path + '/*.json')
    config = {}
    for file in files:
        with open(file) as json_file:
            json_data = json.load(json_file)
            config[json_data['name']] = json_data

    return config

def read_file(file):
    with open(file) as json_file:
        return json.load(json_file)