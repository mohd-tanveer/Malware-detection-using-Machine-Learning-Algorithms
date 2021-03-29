# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 18:19:47 2018

@author: lenovo
"""
#from two import hello
#print("Hello from one")
#hello()
import pandas as pd
import csv
import numpy as np
from create_dataset import *
import create_dataset
import funt
import _pickle as cPickle
from classifier import *


#df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)), columns=['a', 'b', 'c', 'd', 'e'])

def get_name(p):
    str=p
    str=str[::-1]
    for i in range(0,len(str)):
        if(str[i]=="/"):
            break
    str=str[0:i:1]    
    str=str[::-1]
    return str

def classify(i,p):
    differ=i
    if(differ==0):
#        p=[]
#        print("\n\n\n")
#        print(p)
        name=[]
#        p.append("E:/guifinal/pe/hh.exe")
        print("\n\n\n")
        print(p)
        print("\n\n\n")
#        p=[['E:/guifinal/pe/HelpCtr.exe']]
        pp=p[:]
        for i in p:
            str=i[0]
            
            str=str[::-1]
            print("in for loop")
            print(str)
#            str="exe.rtCpleH/ep/lanifiug/:E"
            for j in range(0,len(str)):
                if(str[j]=="/"):
                    break
            str=str[0:j:1]    
            str=str[::-1]
            print(str)
            name.append(str)
        name
        col=funt.n
        print("\n\n\n")
        print(name)
        print(p)
        print(col)
        print("\n\n\n")
        df = create_df(col,p[0],name)
        
        pred=classifier(df)
        file=[pp,pred]
        with open('file.pkl', 'wb') as fid:
                cPickle.dump(file, fid)  
        
    
    if(differ==1):    
#        p=[]
#        p.append("E:/gui/pe/")
        print("\n\n\n")
        path=p[0]
        path=path+'/'
        print(path)
        print("\n\n\n")
        col=funt.n
        file_list= [f for f in os.listdir(path)]
        
        
        
        print(file_list)
        name=file_list[:]
        for i in range(0,len(file_list)):
            file_list[i]=path+file_list[i]
        print("\n\n\n Below for")

        print(file_list)  
        print("\n")
        print(name)
        
        
        df=create_df(col,file_list,name)
        pred=classifier(df)
        folder=[path,name,pred]
       
        with open('folder.pkl', 'wb') as fid:
            cPickle.dump(folder, fid)  
    
    return pred


    # load it again for classifier

#col2=col


#a=pd.DataFrame([create_df()])
#
#df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
#df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
#df3=df.append(df2)
