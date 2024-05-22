import sys
from src.pneumoniaDisease.cloud_storage.s3_operation import S3Operation
from src.pneumoniaDisease.constants.constant import *
from src.pneumoniaDisease.entity.artifact_entity import DataIngestionArtifact
from src.pneumoniaDisease.entity.config_entity import DataIngestionConfig
from src.pneumoniaDisease.exception import CustomException
from src.pneumoniaDisease.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        self.data_ingestion_config = data_ingestion_config
        self.s3 = S3Operation()

    def get_data_from_s3(self)->None:
        try:
            logging.info("Entered the get_data_from_s3 method of Data ingestion class")
            self.s3.sync_folder_from_s3(folder=self.data_ingestion_config.data_path, bucket_name=self.data_ingestion_config.bucket_name, bucket_folder_name=self.data_ingestion_config.s3_data_folder)
            logging.info("Exited the get_data-from_s3 method of Data ingestion class")
        except Exception as e:
            raise CustomException(e, sys) 
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Entered the initiate-data_ingestion method of Data ingestin class")
            self.get_data_from_s3()
            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path
            )
            logging.info("Exited the initiate_data_ingestion method of Data Ingestion class")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)