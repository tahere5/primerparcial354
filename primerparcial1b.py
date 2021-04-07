# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 18:59:43 2021

@author: Hp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('clasificacion.csv')
x = dataset.iloc[:, :7].values 
y = dataset.iloc[:, 7].values

from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

print ("-----MEDIA-----")
media=[]
for i in range(7):
    media.append(np.mean(x[:,i]))
print(media)

print("-----DESVIACION ESTANDAR-----")
desvstandar=[]
for i in range(7):
    desvstandar.append(np.std(x[:,i]))
print(desvstandar)


from scipy import stats
print ("-----MODA-----")
vectormoda=[]
for i in range(7):
    vectormoda.append(stats.mode(x[:,i]))
print(vectormoda)