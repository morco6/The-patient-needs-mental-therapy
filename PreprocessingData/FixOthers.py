# -*- coding: utf-8 -*-
"""
    Last finish's:
    1)Change under zero values to positive numbers in 'Age' column
    2)Fix numbers that are not between 18-120 (by filling them via median)
"""

class FixOthers:
    
    def __init__(self, dataset):
        self.ds = dataset
        
    def fixAge(self):
        #negative numbers to positive
        self.ds['Age'] = self.ds['Age'].abs()
        #fix numbers that are not between 18-120
        notFit = map(lambda x: x[1], filter(lambda (x,y): (y < 18) or (y > 120), self.ds['Age'].iteritems()))
        calcMedian = (self.ds[~self.ds['Age'].isin(notFit)])['Age'].median()
        #replacing these numbers with the median (31)
        for x in notFit: self.ds = self.ds.replace({'Age': x}, calcMedian)
        return self.ds