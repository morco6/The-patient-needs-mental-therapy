# -*- coding: utf-8 -*-

from sklearn.svm import SVC

class SVM:
    
    def __init__(self):
        self.classifier = None
    
    def run(self, dataset, X_train, X_test, y_train, y_test):
        # Fitting SVM Classification to the Training set
        self.classifier = SVC(kernel = 'rbf', random_state = 0)
        self.classifier.fit(X_train, y_train)
        
        # Predicting the Test set results
        self.classifier.predict(X_test)

        return [self.__class__.__name__, self.classifier]