import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from catboost import CatBoostRegressor
from src.exception import CustomException
from src.logger import logging
from xgboost import XGBRegressor
from src.utils import save_object 
from src.utils import evaluate_model
@dataclass
class ModelTrainerConfig:
    trained_model_filepath = os.path.join("artifacts","model.pkl")
class ModelTrainer:
    def __init__(self):
        self.model_trainer = ModelTrainerConfig
    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("split,train and test input data")
            xtrain,ytrain,xtest,ytest = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]

            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            
            model_report:dict = evaluate_model(xtrain=xtrain,ytrain = ytrain,xtest = xtest,ytest = ytest,
                                               models = models)
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]
            if best_model_score <0.6:
                raise CustomException("no best model found")
            logging.info('best model found on both training and test data')
            save_object(
                file_path=self.model_trainer.trained_model_filepath,
                obj=best_model
            )
            predicted = best_model.predict(xtest)
            r2score = r2_score(ytest,predicted)
            return r2score


        except Exception as e:
            raise CustomException(e,sys)