import pandas as pd
import numpy as np
import joblib
from pathlib import Path

from src.mlReg.entity.config_entity import ModelEvaluationConfig
from src.mlReg.utils.common import save_json
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evaluate_model(self, true, prediction):
        mae = np.round(mean_absolute_error(true, prediction), 2)
        mape = np.round(mean_absolute_percentage_error(true, prediction), 2)
        r2 = np.round(r2_score(true, prediction), 2)
        ad_r2 = np.round(1-((1 - r2)*(38715 - 1) / (38715 - 23 - 1)), 2)
        
        return mae, mape, r2, ad_r2
    
    def save_result(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        predict_price = model.predict(X_test)

        mae, mape, r2, adj_r2 = self.evaluate_model(y_test, predict_price)

        scores = {'Mean_Absolute_Error': mae, 
                  'Mean_Absolute_Percentage_Error': mape,
                  'R2_Score': r2,
                  'Adjusted_R2_Score': adj_r2}
        
        save_json(path= Path(self.config.metric_file), data= scores)