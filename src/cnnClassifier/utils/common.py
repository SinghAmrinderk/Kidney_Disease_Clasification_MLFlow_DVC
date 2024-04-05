import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read the YAML file and Return Config Box

    Args:
        path_to_yaml : path like input

    Raises: 
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    create list of directories

    Args: 
        path_to_directories: list of path of directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  ## When exist_ok is set to True, makedirs() will not raise an error if the directory already exists; 
        if verbose:                       ##it will simply return without doing anything. If exist_ok is False (the default), makedirs() will raise a FileExistsError if the directory already exists.
            logger.info(f"Created directory at: {path}")