# -*- coding: utf-8 -*-
"""
    The main class of the pre processing data section.
    This class runs each of the classes methods imported, 
    in the approporiate chronological order to fit data to statistical model.
"""

from MissingData import MissingData
from Categorization import Categorize
from FixOthers import FixOthers
from EncodingData import EncodingData

class PPData:
    
    def __init__(self, dataset):
        self.ds = dataset 
        
    def runPreProcessingData(self):
        #handling missing data
        self.ds = MissingData(self.ds).fixData()
        
        #categorization of gender
        self.ds = Categorize(self.ds).cGenderOrCountry('Gender')
        
        #categorization of country
        self.ds = Categorize(self.ds).cGenderOrCountry('Country')
        
        #fix age column
        self.ds = FixOthers(self.ds).fixAge()
        
        #new feature - 'AgeGroup' 
        self.ds = Categorize(self.ds).cAge()
        
        #Encoding data
        dsAndLabelsTuple = EncodingData(self.ds).encode()

        return dsAndLabelsTuple
    