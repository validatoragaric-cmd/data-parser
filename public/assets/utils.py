# utils.py

import os
import json
from datetime import datetime

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_timestamp():
    return str(int(datetime.now().timestamp()))

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))