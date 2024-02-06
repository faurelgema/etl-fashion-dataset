import os
import json

def read_json_files_in_folder(folder_path):
    json_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            with open(os.path.join(folder_path, filename)) as file:
                data = json.load(file)
                json_data.append(data)
    return json_data
