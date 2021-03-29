# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 18:03:15 2018

@author: hp
"""
import _pickle as cPickle


# save the classifier
with open('classifier.pkl', 'wb') as fid:
    cPickle.dump(classifier, fid)
    
    
    
    # load it again
with open('classifier.pkl', 'rb') as fid:
    classifier= cPickle.load(fid)