from WineQProject.config.configuration import ConfigurationManager
from WineQProject.components.data_transformation import DataTransformation
from WineQProject import logger


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.train_test_split()
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} finished <<<<<< \n\n x==========x")
    except Exception as e:
        logger.exception(e)
        raise e