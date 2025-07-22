import pandas as pd 
import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataingestionConfig:
    train_data_path : str=os.path.join('artifacts','train.csv')
    test_data_path : str=os.path.join('artifacts','test.csv')
    raw_data_path : str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.igestion_config = DataingestionConfig()
    def inititate_data_ingestion(self):
        logging.info("Entered the data ingestion method or componenet")
        try:
            df = pd.read_csv(r"C:\Users\ThinkPad\Downloads\stud.csv")
            logging.info("Dataset read as dataframe")
            os.makedirs(os.path.dirname(self.igestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.igestion_config.raw_data_path,index=False,header=True)
            logging.info("train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.igestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.igestion_config.test_data_path,index = False,header = True)
            logging.info("ingestion of the data is completed")
            return(
                self.igestion_config.train_data_path,
                self.igestion_config.test_data_path,

            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.inititate_data_ingestion()      

