import os
import glob

from generic_utils import load_json, logging, PATH_MODBUS_TABLES, FILENAME_METADATA

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s",
)


def check_folder_structure(path_parent_folder: str, filename_metadata: str) -> None:
    """
    Check that all folders in a directory and its subdirectories are in the format manufacturer/model.

    :param path_parent_folder: The path to the directory containing the JSON files.
    :param filename_metadata: The filename of the JSON files to validate.
    """
    for filename_metadata in glob.glob(
        os.path.join(path_parent_folder, "**", filename_metadata), recursive=True
    ):
        if "sample" in filename_metadata:
            continue

        logging.debug(f"Checking {filename_metadata}...")
        data = load_json(filename_metadata)
        expected_path = os.path.join(
            path_parent_folder, data["manufacturer"], data["model"]
        )
        # From actual path remove the last folder which is the version
        actual_path = os.path.dirname(os.path.dirname(filename_metadata))
        assert (
            actual_path == expected_path
        ), f"Folder structure for {filename_metadata} is incorrect. Expected {expected_path}, got {actual_path}."

        # Check that there is a 'latest' folder in the model's directory
        model_dir = os.path.join(
            path_parent_folder, data["manufacturer"], data["model"]
        )
        assert os.path.exists(
            os.path.join(model_dir, "latest")
        ), f"Missing 'latest' folder in {model_dir}"


if __name__ == "__main__":
    logging.info("Checking all metadata.json files...")
    check_folder_structure(PATH_MODBUS_TABLES, FILENAME_METADATA)
    logging.info("Check complete.")
