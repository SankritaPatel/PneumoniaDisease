from datetime import datetime

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# Data Ingestion Constants
ARTIFACT_DIR: str = "artifacts"
BUCKET_NAME: str = 'xraylungmages'
S3_DATA_FOLDER: str = 'data'