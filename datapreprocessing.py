# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:16:27 2020

@author: Nikhilkumar
"""

import numpy as np #mathematical function
import matplotlib.pyplot as plt #Plots and Graphs 
import pandas as pd #importing and managing Dataset

#importing Dataset
dataset=pd.read_csv('data.csv')
X=dataset.iloc[:,:-1].values 
y=dataset.iloc[:,3].values 

#Taking Care of Missing Data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

#encoding Categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)

#splitting the dataset into Training Set and Testing Set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=0)
