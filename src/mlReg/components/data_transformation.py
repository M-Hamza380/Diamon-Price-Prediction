import os
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
            )

            categorical_trf = ColumnTransformer(
                transformers=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('encoding', OrdinalEncoder(dtype= 'int64'), categorical_columns)
                ],
                verbose_feature_names_out=False,
                remainder='passthrough'
            )

            preprocess = Pipeline(
                steps=[
                    ('num_trf', numerical_trf),
                    ('cat_trf', categorical_trf)
                ]
            )

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

        train_arr = preprocess_obj.fit_transform(train)

        train_arr.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test_arr.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info(f"Split data into training and testing features")
        logger.info(train.shape)
        logger.info(test.shape)
