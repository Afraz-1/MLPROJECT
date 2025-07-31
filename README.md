# Student Performance Prediction - ML Project

A complete end-to-end machine learning project that predicts student math scores based on various demographic and academic factors.

## 📊 Project Overview

This project analyzes student performance data to predict math scores using various machine learning algorithms. The system uses student demographics, parental education level, test preparation, and other academic scores to make predictions.

## 🎯 Problem Statement

Predict student math scores based on:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type (standard/free or reduced)
- Test preparation course completion
- Reading score
- Writing score

## 🏗️ Project Architecture

```
src/
├── components/
│   ├── data_ingestion.py       # Data loading and splitting
│   ├── data_transformation.py  # Feature preprocessing
│   └── model_trainer.py        # Model training and evaluation
├── pipeline/
│   └── predict_pipeline.py     # Prediction pipeline
├── exception.py                # Custom exception handling
├── logger.py                   # Logging configuration
└── utils.py                    # Utility functions
```

## 🚀 Features

- **Modular Design**: Well-structured codebase with separate components
- **Multiple ML Algorithms**: Comparison of 7 different regression models
- **Hyperparameter Tuning**: GridSearchCV for optimal model parameters
- **Data Pipeline**: Automated data preprocessing and transformation
- **Custom Exception Handling**: Detailed error tracking and logging
- **Model Persistence**: Save and load trained models
- **Web Interface Ready**: Flask application structure for deployment

## 🔧 Machine Learning Models

The project compares the following algorithms:
- **Random Forest Regressor**
- **Decision Tree Regressor**
- **Gradient Boosting Regressor**
- **Linear Regression**
- **XGBoost Regressor**
- **CatBoost Regressor**
- **AdaBoost Regressor**

## 📈 Data Processing Pipeline

1. **Data Ingestion**: Load dataset and split into train/test sets
2. **Data Transformation**: 
   - Handle missing values using SimpleImputer
   - One-hot encoding for categorical features
   - Standard scaling for numerical features
3. **Model Training**: Train multiple models with hyperparameter tuning
4. **Model Evaluation**: Select best performing model based on R² score



### Clone Repository
```bash
git clone https://github.com/Afraz-1/MLPROJECT.git
cd MLPROJECT
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Required Packages
```
pandas
numpy
scikit-learn
catboost
xgboost
flask
dill
```

## 📊 Dataset

The project uses student performance data with the following features:
- **gender**: Student's gender
- **race_ethnicity**: Student's race/ethnicity group
- **parental_level_of_education**: Education level of parents
- **lunch**: Type of lunch (standard/free or reduced)
- **test_preparation_course**: Completion status of test prep course
- **reading_score**: Student's reading score
- **writing_score**: Student's writing score
- **math_score**: Target variable - Student's math score

