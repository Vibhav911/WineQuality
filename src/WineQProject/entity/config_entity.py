# This program creates variables for paths of files and folders will be stored that are present in config/config.py
from dataclasses import dataclass
from pathlib import Path

# Data Ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
# Data Validation
@dataclass(frozen= True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema : dict
    
    
# Data Transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    
    
# Model Trainer
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir :Path
    train_data_path: Path
    test_data_path: Path
    model_name : str
    alpha: float
    l1_ratio: float
    target_column : str