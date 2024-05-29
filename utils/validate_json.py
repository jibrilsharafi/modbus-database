import os
import glob
from jsonschema import validate

from generic_utils import (
    load_json,
    logging,
    PATH_MODBUS_TABLES,
    FILENAME_METADATA,
    PATH_METADATA_METADATA_SCHEMA,
    PATH_METADATA_REGISTERS_SCHEMA,
    FILENAME_REGISTERS,
)


def validate_all(path_schema: str, path_parent_folder: str, filename: str) -> None:
    """
    Validate all JSON files in a directory and its subdirectories against a schema.

    :param path_metadata_schema: The path to the JSON schema file.
    :param path_parent_folder: The path to the directory containing the JSON files.
    :param filename_metadata: The filename of the JSON files to validate.
    """
    schema = load_json(path_schema)
    for filename in glob.glob(
        os.path.join(path_parent_folder, "**", filename), recursive=True
    ):
        if "sample" in filename:
            continue

        logging.debug(f"Validating {filename}...")
        data = load_json(filename)
        validate(data, schema)
        logging.debug(f"JSON data in {filename} is valid.")


if __name__ == "__main__":
    logging.info("Validating all metadata.json files...")
    validate_all(PATH_METADATA_METADATA_SCHEMA, PATH_MODBUS_TABLES, FILENAME_METADATA)
    logging.info("Validation complete.")

    logging.info("Validating all registers.json files...")
    validate_all(PATH_METADATA_REGISTERS_SCHEMA, PATH_MODBUS_TABLES, FILENAME_REGISTERS)
    logging.info("Validation complete.")
