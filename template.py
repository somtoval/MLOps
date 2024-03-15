import os

# On Unix-like systems (such as Linux or macOS), the path separator is /, while on Windows systems, it's \.
# However, when you're using Path() in your code, you can use / as the path separator regardless of the underlying operating system. Path() will automatically translate it to the appropriate separator when you interact with the filesystem.
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files=[
    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py"
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py", # Unit testing is testing individual component of an application but integrated test is testing the different units once
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",# for production
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",# for testing in local environment
    "experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath) # Converting the file path we specifyed in windows, we used backword slash but using the Path() class it converts it to windows path
    filedir, filename = os.path.split(filepath) # Split the filepath variable to the directory and file name
    
    if filedir != "": # If the file path contains a folder that means it is not a single file do the below
        os.makedirs(filedir, exist_ok=True) # Create the directory and if it exists no problem
        logging.info(f"Creating directory: {filedir} for the file: {filename}") # Log your progress

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If the file exist or
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existing")