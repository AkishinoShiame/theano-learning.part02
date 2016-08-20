# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:01:54 2015

@author: winpython
"""

import os
import sys, getopt
import time
import numpy as np
from cnn_training_computation import fit, predict
import pickle, cPickle



def run():
    print '... loading data'
    # Load the dataset
    f = file("training_data.pkl", 'rb')
    train = cPickle.load(f)
    f.close()
    
    train_set, train_label = train
    
    data = train_set
    labels = train_label
    
    # Load the dataset
    f = file("testsets.pkl", 'rb')
    test_set, label = cPickle.load(f)
    f.close()
    
    
    
    """
    # read the data, labels
    data = np.genfromtxt("data/mnist_train.data")
    print ". .",
    test_data = np.genfromtxt("data/mnist_test.data")
    print ". .",
    valid_data = np.genfromtxt("data/mnist_valid.data")
    labels = np.genfromtxt("data/mnist_train.solution")
    """
    print ". . finished reading"
    
    # DO argmax
    labels = np.argmax(labels, axis=1)
    print labels
    
    """    
    # normalization
    amean = np.mean(data)
    data = data - amean
    astd = np.std(data)
    data = data / astd
    # normalise using coefficients from training data
    test_data = (test_data - amean) / astd
    valid_data = (valid_data - amean) / astd
    """
    
    #fit(data, labels)
    
    rv = predict(test_set)



    # UNDO argmax and save results x 2
    r = rv
    N = len(r)
    res = np.zeros((N, 10))
    for i in range(N):
        res[i][r[i]] = 1
    
    np.savetxt("test.predict", res, fmt='%i')
    
    print "finished predicting."
   


if __name__ == '__main__':
    run()