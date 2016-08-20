# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:37:01 2015

@author: AkishinoShiame
"""

import os
import sys, getopt
import time
import numpy as np
from cnn_training_computation import fit, predict
import pickle, cPickle, gzip



def run():
    print '... loading data'

    # Load the dataset
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    
    
    train_set_x, train_set_y = train_set
    valid_set_x, valid_set_y = valid_set
    test_set_x, test_set_y = test_set
    
    data = train_set_x
    valid_data = valid_set_x
    test_data = test_set_x
    labels = train_set_y
    
    
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
    """
    # DO argmax
    labels = np.argmax(labels, axis=1)
    print labels
    """
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
    
    print "finished training"
    rv = predict(valid_data)
    rt = predict(test_data)



    # UNDO argmax and save results x 2
    r = rv
    N = len(r)
    res = np.zeros((N, 10))
    for i in range(N):
        res[i][r[i]] = 1
    
    np.savetxt("mnist_valid.predict", res, fmt='%i')
    
    r = rt
    N = len(r)
    res = np.zeros((N, 10))
    for i in range(N):
        res[i][r[i]] = 1
    
    np.savetxt("mnist_test.predict", res, fmt='%i')
    print "finished predicting."
   


if __name__ == '__main__':
    run()