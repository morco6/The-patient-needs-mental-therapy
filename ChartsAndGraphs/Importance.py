# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from xgboost import XGBClassifier

class Importance:
    
    def __init__(self, dataset):
        self.ds = dataset
        
    def calcI(self):
        # Build a classification task using informative features
        X, y = self.ds.drop(columns = ['treatment']), self.ds['treatment']
        self.forestImportance(X,y)
        self.xgBoostImportance(X,y)
        
    def forestImportance(self, X, y):
        # Build a forest and compute the feature importances
        forest = ExtraTreesClassifier(n_estimators=250, random_state=0)
        
        forest.fit(X, y)
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                     axis=0)
        indices = np.argsort(importances)[::-1]
        
        # Print the feature ranking
        print '\nFeature ranking:'
        print '\nby forest:'
        lst = list(X)
        labels = []
        for f in range(X.shape[1]):
            labels.append(lst[f])
            #print("%d. feature %s (%f)" % (f + 1, (list(X))[f], importances[indices[f]]))
        # Plot the feature importances of the forest
        plt.figure(figsize=(12,8))
        plt.title('Feature importances')
        plt.bar(range(X.shape[1]), importances[indices],
               color="r", yerr=std[indices], align='center')
        plt.xticks(range(X.shape[1]), labels, rotation='vertical')
        plt.xlim([-1, X.shape[1]])
        plt.show()
    
    def xgBoostImportance(self, X, y):
        from xgboost import plot_importance
        print '\nby XGBoost:'
        # fit model no training data
        model = XGBClassifier()
        model.fit(X, y)
        # feature importance
        #print(model.feature_importances_)
        # plot feature importance
        plot_importance(model)
        plt.show()