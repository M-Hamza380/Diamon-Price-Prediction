import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder

from src.mlReg.entity.config_entity import DataTransformationConfig
from src.mlReg.utils.logger import logger



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def get_data_transform(self):
        try:
            numerical_columns = ['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_columns = ['cut', 'color', 'clarity']

            numerical_trf = ColumnTransformer(
                transformers= [
                    ('imputer', SimpleImputer(strategy= 'median'), numerical_columns)
                ],
                    verbose_feature_names_out=False,
                    remainder='passthrough'
            ).set_output(transform='pandas')

            categorical_trf = ColumnTransformer(
                transformers=[
                    ('imputer', SimpleImputer(strategy='most_frequent'), categorical_columns),
                    ('encoding', OrdinalEncoder(dtype= 'int64'), categorical_columns)
                ],
                verbose_feature_names_out=False,
                remainder='passthrough'
            ).set_output(transform='pandas')

            preprocess = Pipeline(
                steps=[
                    ('num_trf', numerical_trf),
                    ('cat_trf', categorical_trf)
                ]
            ).set_output(transform='pandas')

            return preprocess

        except Exception as e:
            logger.exception(e)
            raise e
    
    def spliting_data(self):
        data = pd.read_csv(self.config.data_path)
        data.drop(columns=['id'], axis=1, inplace=True)

        # Split the data into train and test features.
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        preprocess_obj = self.get_data_transform()

        target_column_name = 'price'

        train_df_features = train.drop(columns=[target_column_name], axis=1)
        train_df_target = train[target_column_name]

        test_df_features = test.drop(columns=[target_column_name], axis=1)
        test_df_target = test[target_column_name]

        train_arr_features = preprocess_obj.fit_transform(train_df_features)
        test_arr_features = preprocess_obj.transform(test_df_features)

        train_df = pd.concat([train_arr_features, train_df_target], axis=1)
        test_df = pd.concat([test_arr_features, test_df_target], axis=1)

        train_df = train_df.iloc[:,3:]
        test_df = test_df.iloc[:,3:]

        train_df.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test_df.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Split data into training and testing features")
