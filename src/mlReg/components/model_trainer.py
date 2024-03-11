import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestRegressor
from src.mlReg.entity.config_entity import ModelTrainerConfig
from src.mlReg.utils.logger import logger


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def training(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        X_train = train_data.drop([self.config.target_column], axis=1)
        X_test = test_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]
        y_test = test_data[self.config.target_column]

        dt = RandomForestRegressor(n_estimators=self.config.n_estimators, criterion= self.config.criterion, max_features= self.config.max_features,
                                   max_depth= self.config.max_depth, min_samples_leaf= self.config.min_samples_leaf, 
                                   min_samples_split= self.config.min_samples_split)
        dt.fit(X_train, y_train)

        joblib.dump(dt, os.path.join(self.config.root_dir, self.config.model_name))
