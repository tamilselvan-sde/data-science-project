from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories

import os
from dataclasses import dataclass
from src.datascience.utils.common import read_yaml, create_directories

from src.datascience.entity import (DataIngestionConfig)
# Configuration file paths
CONFIG_FILE_PATH = "config/config.yaml"
PARAMS_FILE_PATH = "params.yaml"
SCHEMA_FILE_PATH = "schemas.yaml"

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_url: str
    local_data_file: str
    unzip_dir: str

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH,schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        self.schema = read_yaml(Path(schema_filepath))

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig( root_dir=config.root_dir,source_url=config.source_URL, local_data_file=config.local_data_file,unzip_dir=config.unzip_dir)
        return data_ingestion_config