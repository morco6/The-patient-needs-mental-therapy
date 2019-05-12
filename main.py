# -*- coding: utf-8 -*-
"""
    Author: Mor Cohen
    Website: http://www.morc.io
    A solution to the question: "The patient needs mental therapy?".
    Prediction: The diagnosis according to the data in database.
    Survey by: https://osmihelp.org
    Origin download: https://docs.google.com/spreadsheets/d/1cr65P3ciL2tD4W4KOCTz4Ik67iD52S_DKHXypqgta2o/edit#gid=1001406186
    For more details about the spreadsheet: 'DatasetInfo.txt'
"""

import pandas as pd
from sklearn.model_selection import train_test_split

#The main class of the pre processing data
from PreprocessingData.PPData import PPData
#The class of Charts
from ChartsAndGraphs.Chart import Charts
#Calculate feature importance 
from ChartsAndGraphs.Importance import Importance
#Cross Validation class (Algorithms: Logistic Regression, Random Forest, SVM, Boosting)
from CrossValidation.CrossValidation import CrossValidation

"""- Preprocessing Data -""" 
#Reload the database
dataset = pd.read_csv('Mental_Health_in_Tech_Survey.csv')
#Check some details about the dataset structure for better analyse
#dataset.info() 
#Run the pre processing data (including 6 classes: PPData(main class), MissingData, Categorization, FixOthers, EncodingData)
dataset_And_Encoded_Labels = PPData(dataset).runPreProcessingData()
dataset, labels = dataset_And_Encoded_Labels[0], dataset_And_Encoded_Labels[1]


"""- Vizualization: Charts and grapghs -""" 
charts = Charts(dataset, labels)
#Distribution by Age
charts.AgeDistribuition()
#Probabilitys of mental health condition:
#by age
charts.mentalHealth('age_group')
#by family history
charts.mentalHealth('family_history', 'Do you have a family history of mental illness?')
#
charts.checkImbalance('continent', 'Where do you live?')
#by benefits
charts.mentalHealth('benefits', 'Does your employer provide mental health benefits?')
#by work interfere
charts.mentalHealth('work_interfere', 'If you have a mental health condition, do you feel that it interferes with your work?')
#check imbalance => there is a good balance
charts.checkImbalance('treatment', 'Treated or not')

#Feature Selecting - Include graphs
#calculation of the features importances and displaying on graph
fs = Importance(dataset)
fs.calcI()

#self_employed is showing in the forest feature importance but not in the xgboost feature importance
#lets check why:
#charts.checkImbalance('self_employed', 'Are you self-employed?')
#Answer: There is a huge imbalance between yes/no.


"""Prepare for predicting"""
#from the forest/xgboost feature Importance we get:
#Note: 'work_interfere' have 21% 'NoAnswer'(was a missing value) but dosn't make a significant impact
selected_features = ['age', 'work_interfere', 'gender', 'continent', 'family_history', 'benefits', 'no_employees', 'leave']

#X - Independent, y - Dependent
X = dataset[[col for col in dataset.columns if col in selected_features]]
y = dataset['treatment']

#Training set and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


"""Cross Validation - Logistic Regression, Random Forest, SVM, AdaBoost, XGBoost"""
cv = CrossValidation(dataset, X_train, X_test, y_train, y_test)
cv.run()
accuracyDic = cv.getAccuracyDict()

#Which is the best model?
charts.evaluationModels(accuracyDic) 

# _-Ranking-_ #
#RandomForest: 83.14%
#AdaptiveBoost: 82.86%
#SupportVectorMachine: 82.83%
#XGBoost: 82.64%
#LogisticRegression: 80.39%

model = cv.getModel('RandomForest')

################# Saving The Model #################
        
import pickle
filename = 'model.sav'
pickle.dump(model, open(filename, 'wb'))