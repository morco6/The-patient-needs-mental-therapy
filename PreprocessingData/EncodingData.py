# -*- coding: utf-8 -*-
"""
    Encoding The Data:
    The purpose of this class is to convert strings to numbers such that will
    fit to statistical model
"""

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

class EncodingData:
    
    def __init__(self, dataset):
        self.ds = dataset
        
    def encode(self):
        #encoding the dataset and create a dictionary for the encoded data (without Age)
        labels = {}
        label_encoder = LabelEncoder()
        for feature in self.ds:
            label_encoder.fit(self.ds[feature])
            mapping_label_names = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
            self.ds[feature] = label_encoder.transform(self.ds[feature])
            lKey, lVal = 'Label_' + feature.lower(), sorted(list(mapping_label_names))
            labels[lKey] = lVal
        #Age feature is not proportional - scaling the Age feature:
        self.ageScaling()
        return (self.ds.rename(str.lower, axis='columns'), labels)
    
    def ageScaling(self):
        #Age feature is more dominant than the rest (not proportional)
        #Origin Age range: 18-72
        #scaling the Age feature to fit the others(range:0-3):
        mms = MinMaxScaler(feature_range=(0, 3))
        self.ds['Age'] = mms.fit_transform(self.ds[['Age']])