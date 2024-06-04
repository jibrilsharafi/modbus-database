import os
import json
import logging
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s",
)

MODBUS_TABLE_DIRECTORY = 'modbus-tables'
README_PATH = "README.md"

def get_device_metadata(directory: str) -> List[Dict[str, Any]]:
    """
    Walks through a directory and collects all metadata.json files.

    :param directory: The directory to walk through.
    :return: A list of dictionaries representing the metadata of each device.
    """
    devices = []
    for root, dirs, files in os.walk(directory):
        if "metadata.json" in files:
            with open(os.path.join(root, "metadata.json")) as f:
                metadata = json.load(f)
                metadata["path"] = os.path.relpath(root, directory).replace("\\", "/")
                if "sample" not in metadata["manufacturer"].lower():
                    devices.append(metadata)
                    logging.debug(
                        f"Loaded metadata from {os.path.join(root, 'metadata.json')}"
                    )
    return devices


def format_devices(devices: List[Dict[str, Any]]) -> list[str]:
    """
    Formats the device information into a Markdown table.

    :param devices: A list of dictionaries representing the metadata of each device.
    :return: A string representing the formatted device information.
    """
    formatted = []
    formatted.append("| Manufacturer | Model | Industry | Application |")
    formatted.append("|--------------|-------|----------|-------------|")
    for device in sorted(devices, key=lambda x: (x["manufacturer"].lower(), x["model"].lower())):
        formatted.append(
            f"| **[{device['manufacturer']}]({device['path']})** | [{device['model']}]({device['path']}/{device['model']}) | {device['tags']['industry']} | {device['tags']['application']} |"
        )
    return formatted

def find_start_end_table(readme: List[str]) -> tuple[int, int]:
    """
    Finds the start and end of the table in the README.

    :param readme: A list of strings representing the README.
    :return: A tuple of integers representing the start and end of the table.
    """
    start_table = next(
        i
        for i, line in enumerate(readme)
        if "| Manufacturer | Model | Industry | Application |" in line
    )
    end_table = next(
        i
        for i, line in enumerate(readme)
        if line.strip().startswith("## Usage")
    ) - 1

    return start_table, end_table

def update_table() -> None:
    """
    Updates the device information in the README.
    """
    devices = get_device_metadata(MODBUS_TABLE_DIRECTORY)
    formatted_devices = format_devices(devices)

    with open(README_PATH, "r") as f:
        readme = f.readlines()

    start_table, end_table = find_start_end_table(readme)
    
    # Replace the previous table with the new one
    readme[start_table:end_table] = formatted_devices
    # Between start and end, add newline every other line
    readme[start_table:end_table] = [line + "\n" for line in readme[start_table:end_table]]

    with open(README_PATH, "w") as f:
        f.writelines(readme)
        logging.info("Updated README.md with device information")

def count_devices() -> int:
    """
    Counts the number of devices.

    :param devices: A list of dictionaries representing the metadata of each device.
    :return: An integer representing the number of devices.
    """
    return len(get_device_metadata(MODBUS_TABLE_DIRECTORY))

def update_count() -> None:
    """
    Updates the devices count in the README.

    :param devices: An integer representing the number of devices.
    """
    BADGE_MARKDOWN = "[![Devices Count](https://img.shields.io/badge/Devices"
    BADGE_COLOR = "blue"
    BADGE_LINK = "#devices"
    
    total_devices = count_devices()
    
    with open(README_PATH, "r") as f:
        readme = f.readlines()
    
    for i, line in enumerate(readme):
        if BADGE_MARKDOWN in line:
            readme[i] = f"{BADGE_MARKDOWN}-{total_devices}-{BADGE_COLOR})]({BADGE_LINK})\n"
            break

    with open(README_PATH, "w") as f:
        f.writelines(readme)
        logging.info("Updated device count in README.md")

if __name__ == "__main__":
    logging.info("Updating README.md")
    
    update_table()
    update_count()
    
    logging.info("Finished updating README.md")