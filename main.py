from WineQProject import logger
from WineQProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


# Data Ingestion Stage
STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
   
   
# Data Validation Stage 
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e