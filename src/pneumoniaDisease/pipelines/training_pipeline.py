import sys
from src.pneumoniaDisease.components.data_ingestion import DataIngestion
from src.pneumoniaDisease.entity.artifact_entity import(DataIngestionArtifact)
from src.pneumoniaDisease.entity.config_entity import (DataIngestionConfig)
from src.pneumoniaDisease.exception import CustomException
from src.pneumoniaDisease.logger import logging

class TrainPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method od TrainPipeline class")
            logging.info("Gettign the data from s3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from s3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline Class")
        except Exception as e:
            raise CustomException(e, sys)
    

    def run_pipeline(self)->None:
        try:
            logging.info("Entered the run_pipeline method of TrainPipeline class")
            dta_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            logging.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise CustomException(e, sys)
        