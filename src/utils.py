import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
def  evaluate_model(xtrain,ytrain,xtest,ytest,models):
    try:
        
        report = {}
        for model_name, model in models.items():
            model.fit(xtrain, ytrain)
            y_pred = model.predict(xtest)
            score = r2_score(ytest, y_pred)
            report[model_name] = score
        return report  # ← VERY IMPORTANT


    except Exception as e:
        CustomException(e,sys)


