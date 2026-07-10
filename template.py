import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

project_name = "text_summarizer"

list_of_files = [

    # GitHub Actions
    ".github/workflows/.gitkeep",

    # Artifacts & Logs
    "artifacts/.gitkeep",
    "logs/.gitkeep",

    # Configuration
    "config/config.yaml",

    # Research
    "research/trials.ipynb",

    # Root Files
    "app.py",
    "main.py",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    ".gitignore",
    "README.md",

    # Package Initialization
    f"src/{project_name}/__init__.py",

    # Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    # Config
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    # Constants
    f"src/{project_name}/constants/__init__.py",

    # Entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    # Pipeline
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/pipeline/stage_05_model_evaluation.py",

    # Utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f"{filename} already exists")