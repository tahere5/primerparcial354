# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:21:26 2021

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


print("---MEDIA SIN LIBRERIAS---")
media=[]
for i in range(7):
    n=len(x[:,i])
    med=sum(x[:,i])/n
    media.append(med)
print (media)

print ("---DESVIACION ESTANDAR SIN LIBRERIAS---")
import math
S = 0
N = n
S1=0
desviacionestandar=[]
for m in range(7) :
    for i in range(0,N):
        S=S+x[i,m]
    promedio=S/N
#   hasta acá saca el promedio, necesario para las siguientes operaciones
    for j in range(0,N):
        S1=S1+(x[j,m]-promedio)*(x[j,m]-promedio)
    vari=S1/N
    estandar=math.sqrt(vari)
#   hasta acá saca la varianza, necesaria para obtener la desviacion estandar
    desviacionestandar.append(estandar)
    S1=0
    S=0
print(desviacionestandar)

print ("-----MODA SIN LIBRERIAS-----")
from collections import Counter
modP=[]
valorP=[]
for k in range(7):
    data=Counter(x[:,k]).most_common()
    tdata=len(data)
    mayor=0
    valida=True
    for i in range(tdata):
        cuenta=0
        for j in range (tdata):
            var=data[i]
            varC=data[j]
            if(var[1]==varC[1]):
                cuenta=cuenta+1
        if(cuenta==tdata):
            valida=False
    for i in range(tdata):
        var=data[i]
        if(var[1]==n):
            valida=False
    for i in range(tdata):
        var=data[i]
        if(var[1]==n):
            valida=False
    for i in range(tdata):
        var=data[i]
        if(var[1]==n/2):
            valida=False 
    if(valida==True):
        may=0
        moda=0
        for i in range(tdata):
            var=data[i]
            if(may>var[1]):
                may=may
                moda=moda
            elif(var[1]>may):
                may=var[1]
                moda=var[0]
        modP.append(moda)
        valorP.append(may)
        print("MODA: ",moda," con ", may," repeticiones")
