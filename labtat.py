# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:51:59 2022

@author: Sai pranay
"""

#Hypothesis Testing of Avg TAT and recorded TAT (TAT-Turn Around Time)
#To check if there is significant difference between Avg TAT and recorded TAT or not
#By using ANOVA using level of significance(alpha=5%=0.05)

import pandas as pd
lt=pd.read_csv("E:\\DATA_SCIENCE_ASS\\HYPOTHESIS  TEST\\LabTAT.csv")
print(lt)
list(lt)
lt.shape
lt.describe()
lt.info()

'''
#Test of Hypothesis
Ho: l1 = l2 = l3 = l4 ---> All laboratories avg TAT is same
H1: l1 != l2 != l3 != l4 ---> Any one of the laboratories avg TAT among the 4 are not same
'''
l1=lt['Laboratory 1']
l2=lt['Laboratory 2']
l3=lt['Laboratory 3']
l4=lt['Laboratory 4']

import scipy.stats as stats
z,p=stats.f_oneway(l1,l2,l3,l4)
print(z,p)
alpha=0.05

if p>alpha:
    print('Accepted Ho and Rejected H1')
else:
    print('Accepted H1 and Rejected Ho')
    
#Inference: As per the test of hypothesis we are getting to accepted H1,
#---------- so,we can say any one of the laboratories avg TAT among the 4 are not same