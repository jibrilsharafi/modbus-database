import json
import os
import glob
import logging
from jsonschema import validate, ValidationError

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')

def load_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        logging.error(f"Error loading JSON file {filename}: {e}")
        raise e

def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        logging.error(f"JSON invalid: {e.message}")
        raise e

def main(path_metadata_schema, path_parent_folder, filename_metadata):
    schema = load_json(path_metadata_schema)
    for filename in glob.glob(os.path.join(path_parent_folder, '**', filename_metadata), recursive=True):
        if 'sample-manufacturer' in filename:
            continue
        logging.debug(f"Validating {filename}...")
        data = load_json(filename)
        validate_json(data, schema)
        logging.debug(f"JSON data in {filename} is valid.")