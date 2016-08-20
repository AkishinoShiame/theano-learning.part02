# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:19:01 2015

@author: AkishinoShiame
"""

import cPickle, gzip

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
"""
print ("training set :", train_set)
print ("valid set :", valid_set)
print ("test set :", test_set)
"""
print (train_set)
print (valid_set)
print (test_set)
f.close()