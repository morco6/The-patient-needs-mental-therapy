# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier

class RandomForest:
    
    def __init__(self):
        self.classifier = None
    
    def run(self, dataset, X_train, X_test, y_train, y_test):
        # Fitting Random Forest Classification to the Training set
        self.classifier = RandomForestClassifier(max_depth = None, 
                                                 min_samples_leaf=8, 
                                                 min_samples_split=2, 
                                                 n_estimators = 10, 
                                                 criterion = 'gini', 
                                                 random_state = 42)

        self.classifier.fit(X_train, y_train)
        
        # Predicting the Test set results
        self.classifier.predict(X_test)

        return [self.__class__.__name__, self.classifier]