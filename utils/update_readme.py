import os
import json
import logging
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s",
)


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
                    logging.info(
                        f"Loaded metadata from {os.path.join(root, 'metadata.json')}"
                    )
    return devices


def format_devices(devices: List[Dict[str, Any]]) -> str:
    """
    Formats the device information into a Markdown table.

    :param devices: A list of dictionaries representing the metadata of each device.
    :return: A string representing the formatted device information.
    """
    formatted = "| Manufacturer | Model | Industry | Application |\n"
    formatted += "|--------------|-------|----------|-------------|\n"
    for device in sorted(devices, key=lambda x: (x["manufacturer"], x["model"])):
        formatted += f"| **[{device['manufacturer']}](modbus-tables/{device['manufacturer']})** | [{device['model']}](modbus-tables/{device['manufacturer']}/{device['model']}) | {device['tags']['industry']} | {device['tags']['application']} |\n"
    return formatted


if __name__ == "__main__":
    devices = get_device_metadata("modbus-tables")
    formatted_devices = format_devices(devices)

    with open("README.md", "r") as f:
        readme = f.readlines()

    # Find the start and end of the previous table
    start = next(
        i
        for i, line in enumerate(readme)
        if "| Manufacturer | Model | Industry | Application |" in line
    )
    end = (
        next(i for i, line in enumerate(readme[start:], start) if line.strip() == "")
        + 1
    )

    # Replace the previous table with the new one
    readme[start:end] = formatted_devices.split("\n")
    # Between start and end, add newline every other line
    readme[start:end] = [line + "\n" for line in readme[start:end]]

    with open("README.md", "w") as f:
        f.writelines(readme)
        logging.info("Updated README.md with device information")
