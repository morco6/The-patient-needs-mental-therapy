# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Charts:
    
    def __init__(self, *args):
        self.ds = args[0]
        self.labelDic = args[1]
    
    def AgeDistribuition(self):
        #Distribution by Age
        plt.figure()
        sns.distplot(self.ds['age'], bins=15)
        plt.title('Distribuition by age')
        plt.xlabel('Age')
        
    def checkImbalance(self, labelName, title):
        #Balance between treated and untreated
        labels = self.labelDic['Label_' + labelName]
        graph = sns.countplot(x=labelName, data=self.ds)
        graph.set_xticklabels(labels)
        plt.title(title)
        
    def mentalHealth(self, labelName, *args):
        #General method for statistic graphs
        graph = sns.catplot(x=labelName, y='treatment', hue='gender',
                           data=self.ds, kind='bar',  ci=None,
                           aspect=1, legend_out = True)
        graph.set_xticklabels(self.labelDic['Label_'+labelName])
        
        plt.title('Mental health condition')
        plt.ylabel('Probability')
        if args:
            plt.xlabel(args[0])
        else:
            plt.xlabel(labelName.replace('_',' ').title())
        for t, l in zip(graph._legend.texts, self.labelDic['Label_gender']): t.set_text(l.title())
        graph.fig.subplots_adjust(top=0.8,right=0.8)
        plt.show()
        
    def evaluationModels(self, models):
        s = pd.Series(models)
        s = s.sort_values(ascending=False)
        #Colors
        ax = s.plot(kind='bar') 
        for p in ax.patches:
            ax.annotate(str(round(p.get_height(),2)), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.ylim([70.0, 90.0])
        plt.xlabel('Algorithm')
        plt.ylabel('Percentage')
        plt.title('Success of model')
        plt.show()