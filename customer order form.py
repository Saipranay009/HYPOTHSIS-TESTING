# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:31:29 2022

@author: Sai pranay
"""

#Hypothesis Testing of Tele call data of 4 centers across globe
#To check if there is error in the audit or not
#By using anova using level of significance(alpha=5%=0.05)

import pandas as pd

co=pd.read_csv('E:\\DATA_SCIENCE_ASS\\HYPOTHESIS  TEST\\Costomer+OrderForm.csv')
co.head()
co.dtypes
list(co)
co.shape
co.value_counts()
co.describe().T

'''
#Test of Hypothesis
Ho: c1 = c2 = c3 = c4 ---> All 4 call centers defective % are varying by 5% from center
H1: c1 != c2 != c3 != c4 ---> Any one of the 4 call centers defective % are NOT varying by 5% from center
'''
#Converting categorical data to numerical by label encoding

from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()

for i in range(0,4,1):
    co.iloc[:,i]=LE.fit_transform(co.iloc[:,i])
print(co)

c1=co['Phillippines']
c2=co['Indonesia']
c3=co['Malta']
c4=co['India']

import scipy.stats as stats
z,p=stats.f_oneway(c1,c2,c3,c4)
print(z,p)
alpha=0.05

if p>alpha:
    print('Accepted Ho and Rejected H1')
else:
    print('Accepted H1 and Rejected Ho')
    
#Inference: As per the test of hypothesis we are getting to accept Ho,
#-so,All the 4 call centers defective % are under the 5% level of significance from center.