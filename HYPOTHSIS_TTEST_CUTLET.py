# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:24:33 2022

@author: Sai pranay
"""

#Hypothesis Testing of Cutlets
#To check if there is significant difference between unit A&B or not
#By using Two sample mean test using level of significance(alpha=5%=0.05)

#=----------------importing-----------

import pandas as pd
cl = pd.read_csv("E:\\DATA_SCIENCE_ASS\\HYPOTHESIS  TEST\\Cutlets.csv")
print(cl)
list(cl)
cl.shape
cl.info()
cl.describe()
cl.columns

#-----------histogram
cl['Unit A'].hist()
cl['Unit B'].hist()

'''
#Test of Hypothesis
Ho: UnitA = UnitB ---> No significant difference in diameter of cutlets of two units
H1: UnitA != UnitB ---> Significant difference in diameter of cutlets of two units
'''

A=cl['Unit A']
B=cl['Unit B']
alpha=0.05 #alpha is the level of significance
from scipy.stats import ttest_ind
z,p=ttest_ind(A,B)
print(z,p)

if p>alpha:
    print('Accepted Ho and Rejected H1')
else:
    print('Accepted H1 and Rejected Ho')
    
#Inference: As we have got to accept Ho that implies there is No significant
#---------- difference between the diameters of Unit A and Unit B





