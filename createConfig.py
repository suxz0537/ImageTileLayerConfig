# read config.json from all sub directories and return json object
import os
import json

def read_config():

    config_data = {}
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            if name == "config.json":
                file_path = os.path.join(root, name)
                with open(file_path, "r") as config_file:
                    config_data = json.load(config_file)
    return config_data

print(read_config())