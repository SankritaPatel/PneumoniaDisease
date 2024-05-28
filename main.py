import sys
from src.pneumoniaDisease.pipelines.training_pipeline import TrainPipeline
from src.pneumoniaDisease.exception import CustomException
def start_training():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        print("Data Transformation Done")
    except Exception as e:
        raise CustomException(e, sys)
    
if __name__=="__main__":
    start_training()