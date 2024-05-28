import logging

import validate_json

PATH_METADATA_METADATA_SCHEMA = 'schemas/metadata_schema.json'
PATH_MODBUS_TABLES = 'modbus-tables'
FILENAME_METADATA = 'metadata.json'

PATH_METADATA_REGISTERS_SCHEMA = 'schemas/registers_schema.json'
PATH_MODBUS_TABLES = 'modbus-tables'
FILENAME_REGISTERS = 'registers.json'

if __name__ == "__main__":    
    logging.info("Validating all metadata.json files...")
    validate_json.main(PATH_METADATA_METADATA_SCHEMA, PATH_MODBUS_TABLES, FILENAME_METADATA)
    logging.info("Validation complete.")
    
    logging.info("Validating all registers.json files...")
    validate_json.main(PATH_METADATA_REGISTERS_SCHEMA, PATH_MODBUS_TABLES, FILENAME_REGISTERS)
    logging.info("Validation complete.")