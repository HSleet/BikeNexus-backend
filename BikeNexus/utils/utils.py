import json
from BikeNexus import db

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
