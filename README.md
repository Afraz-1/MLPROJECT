## Student Performance Evaluater
This project demonstrates how to build a clean, scalable, and deployable ML application using:

Modular programming (separate pipelines, utilities, web app)

Centralized logging & custom exceptions

Data and model pipelines

Flask web interface for predictions


Approach for the project
Data Ingestion :

In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.
Data Transformation :

In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.
Model Training :

In this phase base model is tested . The best model found was catboost regressor.
After this hyperparameter tuning is performed on catboost and knn model.

Prediction Pipeline :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.
Flask App creation :

Flask app is created with User Interface to predict the gemstone prices inside a Web Application.
