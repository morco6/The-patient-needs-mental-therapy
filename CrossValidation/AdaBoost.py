# -*- coding: utf-8 -*-

from sklearn.ensemble import AdaBoostClassifier

class AdaBoost:
    
    def __init__(self):
        self.classifier = None
    
    def run(self, dataset, X_train, X_test, y_train, y_test):
        #Fitting AdaBoost Classification to the Training set
        #base estimator is Decision Tree by default
        self.classifier = AdaBoostClassifier(n_estimators=50)
        self.classifier.fit(X_train, y_train)
        
        #Predicting the Test set results
        self.classifier.predict(X_test)
        
        return [self.__class__.__name__, self.classifier]