import os
import pandas as pd
from sklearn.model_selection import train_test_split

from src.mlReg.entity.config_entity import DataTransformationConfig
from src.mlReg.utils.logger import logger



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def spliting_data(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into train and test features.
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Split data into training and testing features")
        logger.info(train.shape)
        logger.info(test.shape)
