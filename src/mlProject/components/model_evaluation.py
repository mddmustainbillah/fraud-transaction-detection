# import os
# import pandas as pd
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# from urllib.parse import urlparse
# import numpy as np
# import joblib
# from src.mlProject.entity.config_entity import ModelEvaluationConfig
# from src.mlProject.utils.common import save_json
# from pathlib import Path


# class ModelEvaluation:
#     def __init__(self, config: ModelEvaluationConfig):
#         self.config = config

    
#     def eval_metrics(self,actual, pred):
#         rmse = np.sqrt(mean_squared_error(actual, pred))
#         mae = mean_absolute_error(actual, pred)
#         r2 = r2_score(actual, pred)
#         return rmse, mae, r2
    


#     def save_results(self):

#         test_data = pd.read_csv(self.config.test_data_path)
#         model = joblib.load(self.config.model_path)

#         test_x = test_data.drop([self.config.target_column], axis=1)
#         test_y = test_data[[self.config.target_column]]
        
#         predicted_qualities = model.predict(test_x)

#         (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
        
#         # Saving metrics as local
#         scores = {"rmse": rmse, "mae": mae, "r2": r2}
#         save_json(path=Path(self.config.metric_file_name), data=scores)



import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from urllib.parse import urlparse
import numpy as np
import joblib
from src.mlProject.entity.config_entity import ModelEvaluationConfig
from src.mlProject.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred)
        recall = recall_score(actual, pred)
        f1 = f1_score(actual, pred)
        cm = confusion_matrix(actual, pred)

        return accuracy, precision, recall, f1, cm

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        predicted_classes = model.predict(test_x)

        accuracy, precision, recall, f1, confusion_matrix = self.eval_metrics(test_y, predicted_classes)

        # Saving metrics as local
        scores = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "confusion_matrix": confusion_matrix.tolist()
        }
        save_json(path=Path(self.config.metric_file_name), data=scores)

