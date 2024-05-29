from typing import Any, Dict
import json
import os
import logging

PATH_MODBUS_TABLES = "modbus-tables"
FILENAME_METADATA = "metadata.json"

PATH_METADATA_METADATA_SCHEMA = "schemas/metadata_schema.json"
FILENAME_METADATA = "metadata.json"

PATH_METADATA_REGISTERS_SCHEMA = "schemas/registers_schema.json"
FILENAME_REGISTERS = "registers.json"

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s",
)

def load_json(path: str) -> Dict[str, Any]:
    """
    Load a JSON file and return its contents as a dictionary.

    :param filename: The path to the JSON file.
    :return: The contents of the JSON file as a dictionary.
    :raises json.JSONDecodeError: If the file cannot be decoded as JSON.
    """
    assert os.path.exists(path), f"File {path} does not exist."

    with open(path, "r") as file:
        return json.load(file)
