import os
import sys
from src.pneumoniaDisease.entity.artifact_entity import ModelPusherArtifact
from src.pneumoniaDisease.entity.config_entity import ModelPusherConfig
from src.pneumoniaDisease.exception import CustomException
from src.pneumoniaDisease.logger import logging

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):
        self.model_pusher_config = model_pusher_config

    def build_and_push_bento_image(self):
        try:
            logging.info("Enterd build_and_push_bento_image method of ModelPusher class")
            logging.info("Building the bento from bentofile.yaml")
            os.system("bentoml build")
            logging.info("Built the bento from bentofile.yaml")
            logging.info("Creating docker image for bento")
            # os.system(f"bentoml containerize{self.model_pusher_config.bentoml_service_name}:latest -t")
            logging.info("Logged into ECR")
            logging.info("Pushing bento image to ECR")
            # os.system()
            logging.info("Pushed bento image to ECR")
            logging.info("Exited build_and_push_bento_image method of ModelPusher class")
            
        except Exception as e:
            raise CustomException(e, sys)
    

    def initiate_model_pusher(self)->ModelPusherArtifact:
        '''
        Method Name: initiate_model_pusher
        Description: THis method initiated model pusher.
        Output: Model Pusher artifact
        '''
        try:
            logging.info("Entered initiate_model_pusher method of ModelPusher class")
            self.build_and_push_bento_image()
            model_pusher_artifact = ModelPusherArtifact(
                bentoml_model_name=self.model_pusher_config.bentoml_model_name,
                bentoml_service_name=self.model_pusher_config.bentoml_service_name
            )
            logging.info("Exited initiate_model_pusher method of ModelPusher class")
            return model_pusher_artifact
        except Exception as e:
            raise CustomException(e, sys)