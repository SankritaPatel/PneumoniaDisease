import sys
from src.pneumoniaDisease.components.model_evaluation import ModelEvaluation
from pneumoniaDisease.components.model_trainer import ModelTrainer
from src.pneumoniaDisease.components.data_transformation import DataTransformation
from src.pneumoniaDisease.components.data_ingestion import DataIngestion
from src.pneumoniaDisease.entity.artifact_entity import(DataIngestionArtifact, DataTransformationArtifact, ModelEvaluationArtifact, ModelTrainerArtifact)
from src.pneumoniaDisease.entity.config_entity import (DataIngestionConfig, DataTransformationConfig, ModelEvaluationConfig, ModelTrainerConfig)
from src.pneumoniaDisease.exception import CustomException
from src.pneumoniaDisease.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_evaluation_config=ModelEvaluationConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from s3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from s3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        try:
            logging.info("Entered the start_data_transformation method of TrainPipeline class")
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=self.data_transformation_config,
            )
            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )
            logging.info("Exited the start_data_transformation method of TrainPipeline class")
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            logging.info("Entered the start_model_trainer method of TrainPipeline class")
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,model_trainer_config=self.model_trainer_config,)
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            logging.info("Exited the start_model_trainer method of TrainPipeline class")
            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_evaluation(
        self,
        model_trainer_artifact: ModelTrainerArtifact,
        data_transformation_artifact: DataTransformationArtifact,
    ) -> ModelEvaluationArtifact:
        logging.info("Entered the start_model_evaluation method of TrainPipeline class")

        try:
            model_evaluation = ModelEvaluation(
                data_transformation_artifact=data_transformation_artifact,
                model_evaluation_config=self.model_evaluation_config,
                model_trainer_artifact=model_trainer_artifact,
            )

            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()

            logging.info(
                "Exited the start_model_evaluation method of TrainPipeline class"
            )

            return model_evaluation_artifact

        except Exception as e:
            raise CustomException(e, sys)
    
    
    def run_pipeline(self) -> None:
        try:
            logging.info("Entered the run_pipeline method of TrainPipeline class")
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            print("data ingestion done")
            data_transformation_artifact: DataTransformationArtifact = (
                self.start_data_transformation(
                    data_ingestion_artifact=data_ingestion_artifact
                )
            )
            print("Data transformation Done")
            model_trainer_artifact: ModelTrainerArtifact = self.start_model_trainer(
                data_transformation_artifact=data_transformation_artifact
            )
            print("Model Trainer Done")
            model_evaluation_artifact: ModelEvaluationArtifact = (
                self.start_model_evaluation(
                    model_trainer_artifact=model_trainer_artifact,
                    data_transformation_artifact=data_transformation_artifact,
                )
            )
            print("Model Evaulation Done")
            logging.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise CustomException(e, sys)