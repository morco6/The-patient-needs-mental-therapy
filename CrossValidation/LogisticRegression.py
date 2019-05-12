# -*- coding: utf-8 -*-

from sklearn.linear_model import LogisticRegression

class logisticRegression:
    
    def __init__(self):
        self.classifier = None
        
    def run(self, dataset, X_train, X_test, y_train, y_test):
        #Train a logistic regression model on the training set
        self.classifier = LogisticRegression(random_state = 0)
        self.classifier.fit(X_train, y_train)
        
        #Predicting the Test set results
        self.classifier.predict(X_test)
        
        return [self.__class__.__name__, self.classifier]