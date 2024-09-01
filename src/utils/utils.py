from typing import Union
import yaml


def read_yaml(file_path: str) -> Union[dict, list]:
    """
    Reads a YAML file from the specified file path and returns the parsed data.

    Parameters:
        file_path (str): The path to the YAML file.

    Returns:
        dict or list: The parsed data from the YAML file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")


if __name__ == "__main__":
    read_yaml()
