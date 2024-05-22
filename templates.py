import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name = 'pneumoniaDisease'

list_of_files = [
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/cloud_storage/__init__.py',
    f'src/{project_name}/cloud_storage/s3_operation.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_evaluation.py',
    f'src/{project_name}/components/model_trainer.py',
    f'src/{project_name}/components/model_pusher.py',
    f'src/{project_name}/constants/__init__py',
    f'src/{project_name}/entity/artifact_entity.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/pipelines/__init__.py',
    f'src/{project_name}/pipelines/training_pipeline.py',
    f'src/{project_name}/pipelines/prediciton_pipeline.py',
     f'src/{project_name}/exception.py',
     f'src/{project_name}/logger.py',
     f'src/{project_name}/utils.py',
     'main.py',
     'app.py',
     'Dockerfile',
     'requirements.txt',
     'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass #Create an empty file
        logging.info(f"Creating empty files: {filepath}")
    else:
        logging.info(f"{filename} is already exists.")