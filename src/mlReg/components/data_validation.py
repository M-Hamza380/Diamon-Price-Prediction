import os
import pandas as pd

from src.mlReg.entity.config_entity import DataValidationConfig
from src.mlReg.utils.logger import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self):
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_cols.pop()
            all_schema = self.config.all_schema.keys()

            print(f'Listed columns from csv file: {all_cols}')
            print(f'Listed columns from schema file: {all_schema}')

            for col in all_cols:
                if (col not in all_schema):
                    validation_status = False

                    with open(self.config.Status_File, 'w') as f:
                        f.write(f"All schema columns: \n {all_schema} \n")
                        f.write(f"validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.Status_File, 'w') as f:
                        f.write(f"All schema columns: \n {all_schema} \n")
                        f.write(f"validation Status: {validation_status}")
            
            return validation_status
        except Exception as e:
            raise e

