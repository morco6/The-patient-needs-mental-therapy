# -*- coding: utf-8 -*-

from xgboost import XGBClassifier

class XGBoost:
    
    def __init__(self):
        self.classifier = None
    
    def run(self, dataset, X_train, X_test, y_train, y_test):
        #Fitting XGB Classification to the Training set

        self.classifier = XGBClassifier()
        self.classifier.fit(X_train, y_train)
        
        #Predicting the Test set results
        self.classifier.predict(X_test)
    
        return [self.__class__.__name__, self.classifier]
    
    