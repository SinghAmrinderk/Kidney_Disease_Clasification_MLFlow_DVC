import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "secret/secret.yaml"
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        '''
        When exist_ok is set to True (which is the default), os.makedirs() will not raise an error if the directory already exists. 
        It will simply proceed without attempting to create the directory again.
        If exist_ok were set to False and the directory already existed, os.makedirs() would raise a FileExistsError.
        '''
        os.makedirs(filedir, exist_ok=True)  
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        '''
        os.path.exists(filepath) function is used to check whether a file or directory exists at a given path. 
        It returns True if the file or directory exists, and False otherwise.
        '''
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")