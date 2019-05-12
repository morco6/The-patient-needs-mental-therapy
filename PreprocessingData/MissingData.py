# -*- coding: utf-8 -*-
"""
    Handling Missing Data:
    1)drop unnecessary columns
    2)find empty values in the database
    3)filling/fitting in the missing/unwanted values
"""

class MissingData:
    
    def __init__(self, dataset):
        self.ds = dataset
       
    def fixData(self):
        self.ds = self.dropColumns()
        self.fillEmptyVals(self.findEmptyVals())
        return self.ds
        
    def dropColumns(self):
        #Delete columns that do not necessarily need.
        return self.ds.drop(columns=['Timestamp', 'comments', 'state'])
    
    def findEmptyVals(self):
        #return names of columns with empty values.
        return map(lambda feature_name: feature_name[0], filter(lambda (feature_name,value): value is True, 
                    (self.ds.isnull().sum() > 0).iteritems()))
         
    def fillEmptyVals(self, empt_lst):
        #There is only two columns with empty values: 'self_employed' and 'work_interfere'
        #only 11% is 'Yes' in the self_employed column - fill with 'No'.
        #21% is empty in the work_inference column - fill with 'noAnswer'
        newVals = ['No', 'NoAnswer']
        for x in range(2): self.ds[empt_lst[x]] = self.ds[empt_lst[x]].fillna(newVals[x])