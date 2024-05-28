# Contributing to Modbus Database

Thank you for your interest in contributing to the Modbus Database! This document provides guidelines for contributing.

## Adding a Modbus Table

To add a Modbus table:

1. Fork this repository.
2. In your fork, navigate to the `modbus-tables` directory.
3. If a subdirectory for the manufacturer of the Modbus table does not exist, create one.
4. If a subdirectory for the model of the Modbus table does not exist within the manufacturer's subdirectory, create one.
5. Add the Modbus table to the model's subdirectory.
6. Commit your changes and push them to your fork.
7. Open a pull request to merge your changes into this repository.

## Format

The Modbus tables should be in a consistent, machine-readable format. Please ensure your Modbus table adheres to this format before submitting a pull request.

## Tests

Before submitting a pull request, please run the tests to ensure your Modbus table is correctly formatted. The tests can be run with the following command:

```bash
python -m unittest discover tests