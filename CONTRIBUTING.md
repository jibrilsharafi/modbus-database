# Contributing to Modbus Database

Thank you for your interest in contributing to the Modbus Database! This document provides guidelines for contributing.

## Adding a Modbus Table

To add a Modbus table:

1. Fork this repository.
2. In your fork, navigate to the `modbus-tables` directory.
3. Copy the `sample-manufacturer` or `sample-model` folder, depending on your objective.
4. Rename the copied folder to match the manufacturer or model you're adding, and fill in the data in the appropriate files.
5. (Optional) Run the `utils/validate_json.py` and `utils/validate_folders.py` scripts locally to ensure everything is correctly formatted and structured.
6. Commit your changes and push them to your fork.
7. Open a pull request to merge your changes into this repository.

Please note that there are GitHub Actions set up to automatically validate your contribution when you open a pull request. This includes checks for both the JSON format of the Modbus table and the folder structure in the repository.

## Format

The Modbus tables should be in a consistent, machine-readable format. You can use the `sample-manufacturer/sample-model/metadata.json` and `sample-manufacturer/sample-model/registers.json` files as a guideline for the format. You can also refer to the Modbus tables of other devices already present in the repository. Please ensure your Modbus table adheres to this format before submitting a pull request.

## Tests

Before submitting a pull request, please ensure your Modbus table is correctly formatted and the folder structure is correct. You can do this by running the `utils/validate_json.py` and `utils/validate_folders.py` scripts locally. 

To set up a virtual environment and install the necessary dependencies to run these scripts, follow these steps:

1. Create a new virtual environment: `python -m venv env`
2. Activate the virtual environment: 
    - On Windows: `.\env\Scripts\activate`
    - On Unix or MacOS: `source env/bin/activate`
3. Install the necessary dependencies: `pip install -r requirements.txt`
4. Run the validation scripts: 
    - `python utils/validate_json.py`
    - `python utils/validate_folders.py`

These scripts, along with the GitHub Actions, will also be run automatically when you open a pull request.