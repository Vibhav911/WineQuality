import os
from WineQProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from WineQProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
        ## Note: You can add different data transformation techniques such as Scaler, PCA and all
        #You can perform all kinds of EDA in ML cycle here before passing this data to the model

        # I am only adding train_test_spliting cz this data is already cleaned up
        
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        
        # Split the data into train and test ( 0.75 and 0.25)
        train, test = train_test_split(data, test_size=0.25)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Train and Test data are created at {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)