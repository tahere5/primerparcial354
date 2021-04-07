# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 00:58:56 2021

@author: Hp
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('clasificacion2.csv')
x = dataset.iloc[:, :7].values 
y = dataset.iloc[:, 7].values


from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)



from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, :7])
x[:, :7] = imputer.transform(x[:, :7])
print(x)

from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
sc = StandardScaler()
X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
X_train[:, :7] = sc.fit_transform(X_train[:, :7])
X_test[:, :7] = sc.transform(X_test[:, :7])