# -*- coding: utf-8 -*-

from LogisticRegression import logisticRegression
from RandomForest import RandomForest
from SupportVectorMachine import SVM
from AdaBoost import AdaBoost
from XGBoost import XGBoost

from sklearn.model_selection import cross_val_score

class CrossValidation():
        
    classificationAlgorithms = [logisticRegression(),
                                RandomForest(),
                                SVM(),
                                AdaBoost(),
                                XGBoost()]
        
    def __init__(self, dataset, X_train, X_test, y_train, y_test):
        self.ds = dataset
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.accuracyDict = {}
        self.models = {}
               
    def run(self):      
        for alg in self.classificationAlgorithms:
            results = alg.run(self.ds, self.X_train, self.X_test, self.y_train, self.y_test)
            #results incuding: the name of the algorithm and the model
            self.appendToAccuracyDict(results[0], self.kFoldCrossValidation(results[0],results[1]))
            self.appendModel(results[0], results[1])
        
    def kFoldCrossValidation(self, algName, classifier):
        accuracies = cross_val_score(estimator = classifier, 
                                     X = self.X_train, 
                                     y = self.y_train, 
                                     cv = 300)
        accuracy = accuracies.mean()
        print algName+' accuracy:',accuracy*100,'%'
        return accuracy
        
    def appendToAccuracyDict(self, algName, accuracy):
        #tup[0]->algorithm name, tup[1]->accuracy
        self.accuracyDict[algName] = accuracy*100
        
    def appendModel(self, algName, model):
        #tup[0]->algorithm name, tup[1]->accuracy
        self.models[algName] = model
        
    def getAccuracyDict(self):
        return self.accuracyDict
        
    def getModel(self, name):
        return self.models[name]
        