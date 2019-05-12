# -*- coding: utf-8 -*-
"""
    Categorization of mixed values:
    1)Columns that need fixing: 'Gender' and 'Age'
    2)Group, sort and delete mixing Gender values
    3)Add a new feature(column) of 'AgeGroup' based on the 'Age' feature
"""

import pandas as pd

class Categorize:
    
    #Gender Dictionary - deep dive into the data
    gd = {}
    gd['male'] = ['male', 'm', 'male-ish', 'maile', 'mal', 'male (cis)', 'make', 'male ', 'man','msle', 'mail', 
      'malr','cis man', 'Cis Male', 'cis male']
    gd['female'] = ['cis female', 'f', 'female', 'woman', 'femake', 'female ','cis-female/femme', 'female (cis)', 'femail']
    gd['trans'] = ['trans-female', 'something kinda male?', 'queer/she/they', 'non-binary', 'nah', 'all', 
      'enby', 'fluid', 'genderqueer', 'androgyne', 'agender', 'male leaning androgynous', 'guy (-ish) ^_^', 
      'trans woman', 'neuter', 'female (trans)', 'queer', 'ostensibly male, unsure what that really means']
    
    #Continent-Country Dictionary - deep dive into the data
    ct = {}
    ct['asia'] = ['Russia','India','Israel','Singapore', 'Japan', 'Thailand', 'Georgia', 'Philippines', 'China']
    ct['africa'] = ['Portugal','South Africa','Nigeria', 'Zimbabwe']
    ct['america'] = ['United States', 'Canada', 'Mexico', 'Brazil', 'Costa Rica','Colombia','Uruguay']
    ct['europe'] = ['United Kingdom', 'Bulgaria', 'France', 'Netherlands', 'Switzerland',
      'Poland', 'Germany', 'Ireland', 'Italy', 'Sweden','Latvia', 'Romania', 'Belgium', 'New Zealand', 'Spain', 'Finland',
      'Bosnia and Herzegovina','Hungary', 'Croatia', 'Norway','Denmark', 'Greece', 'Moldova', 'Czech Republic', 'Slovenia', 'Austria']
    ct['australia'] = ['Australia']
    
    #Age groups - deep dive into the data
    ag = ['0-20', '21-30', '31-65', '66-100']
    
    def __init__(self, dataset):
        self.ds = dataset
        
    def cleanDirt(self):
        #cleaning rows that are not fit at all
        dirt = list(set(self.ds['Gender'].unique())-set(self.gd.keys()))
        self.ds = self.ds[~self.ds['Gender'].isin(dirt)]
          
    def cGenderOrCountry(self, colName):
        #categorize Gender into 3 classes: 'male', 'female' and 'trans'
        if colName == 'Gender':
            self.ds[colName] = self.ds[colName].str.lower()
            for key, val in self.gd.iteritems(): 
                for x in val: self.ds[colName] = self.ds[colName].replace(x, key)  
            self.cleanDirt() 
        #categorize countrys into 5 classes/continents: 'asia', 'africa', 'america', 'europe', 'australia'
        elif colName == 'Country':
            for key1, val1 in self.ct.iteritems(): 
                for x1 in val1: self.ds[colName] = self.ds[colName].replace(x1, key1)  
            self.ds = self.ds.rename(index=str, columns={colName: 'continent'})
        return self.ds
    
    def cAge(self):
        #continuous age to a categorical age by range - adding a new feature
        self.ds['age_group'] = pd.cut(self.ds['Age'], [0,20,30,65,100], labels=self.ag, include_lowest=True)
        return self.ds