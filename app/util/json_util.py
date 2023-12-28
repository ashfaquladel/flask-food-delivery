import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(e)

def write_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
    except FileNotFoundError as e:
        print(e)