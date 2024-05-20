# Component
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from WineQProject.utils.common import save_json
from WineQProject.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config
        
        
    def eval_metric(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis = 1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)    # settting tracking uri as doing in the remote server
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metric(test_y, predicted_qualities)
            
            #Saving metric as local
            scores={'rmse':rmse, 'mae':mae, 'r2':r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)    # saving in mlflow
            mlflow.log_metric('rmse', rmse)
            mlflow.log_metric('r2', r2)
            mlflow.log_metric('mae', mae)
            
            
            # Check if you are working in uri or local file
            # model registry does not work with file store
            if tracking_uri_type_store != 'file':
                
                # Register the model
                # There are other way to use the Model Registry, which depends on the use case, 
                # please refer to the document for more information:
                # https://www.mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, 'model', registered_model_name="ElasticnetModel")
            
            else:
                mlflow.sklearn.log_model(model,'model')
                
                # Save the model to the model registry
            