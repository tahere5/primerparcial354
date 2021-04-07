# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 23:48:14 2021

@author: Hp
"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('clasificacion.csv')
#columna variables dependientes
x = dataset.iloc[:, :7].values 
#columna variable independiente
y = dataset.iloc[:, 7].values

from sklearn.preprocessing import LabelEncoder
labelencoder_x = LabelEncoder()
for i in range(7):
    x[:,i] = labelencoder_x.fit_transform(x[:,i])

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
           
plt.hist(y)
plt.hist(x)