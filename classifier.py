# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import KFold
import os.path
import _pickle as cPickle




def classifier(df):
    with open('dump/classifier.pkl', 'rb') as fid:
        classifier= cPickle.load(fid)
    
    
        # load it again missing values
    with open('dump/imputer.pkl', 'rb') as fid:
        imputer= cPickle.load(fid)
         
            # load it again for scalar
    with open('dump/sc.pkl', 'rb') as fid:
        sc= cPickle.load(fid)    
#col1=[col]

    X = df.iloc[:,1:-1].values
#  
    X[:, :-1] = imputer.transform(X[:, :-1])
    #

    X = sc.transform(X)
    #

    y_pred = classifier.predict(X)
    
    return y_pred
    
   


