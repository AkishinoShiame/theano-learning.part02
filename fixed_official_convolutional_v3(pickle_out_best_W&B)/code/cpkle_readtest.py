# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 01:36:53 2015

@author: winpython
"""

import cPickle, gzip

#load the datasets about weight and bias in for layer
dataset = gzip.open('../data/best_training.pkl.gz','rb')
layer0_w, layer0_b, layer1_w, layer1_b, layer2_w, layer2_b, layer3_w, layer3_b = cPickle.load(dataset)

print ("datasets 0: ", layer0_w, layer0_b )
print ("datasets 1: ", layer1_w, layer1_b )
print ("datasets 2: ", layer2_w, layer2_b )
print ("datasets 3: ", layer3_w, layer3_b )

dataset.close()