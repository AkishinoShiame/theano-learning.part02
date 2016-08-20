# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:10:08 2015

@author: winpython
"""
import os
import sys, getopt
import time
import numpy as np
from cnn_training_computation import fit, predict

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from PIL import Image
import cPickle



def run():
    print '... loading data'
    """
    temp_line = np.zeros([784],dtype=np.float64)
    
    pil_im = Image.open( "test.jpg" )
    plt.show()
            
    pil_im = Image.open( "test.jpg" ).convert('L')
    #imshow(np.asarray(pil_im)) # before resize
    pil_im = pil_im.resize((28, 28), Image.BILINEAR )
    pil_im = np.array(pil_im)
    plt.imshow(pil_im, cmap='gray')
    plt.show()
    
    cr = 0
            
    print "Read line",
    for k in range(28):
        for l in range(28):
            temp_line[cr]= pil_im[k][l]/225.
            print " in ", cr, "...",                
            cr += 1
    
    # Load the dataset
    """
    #test_set = temp_line
    f = file("training_data.pkl", 'rb')
    final_output, final_label = cPickle.load(f)
    f.close()
    test_set = final_output
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
    
    rv = predict(test_set)



    # UNDO argmax and save results x 2
    r = rv
    N = len(r)
    res = np.zeros((N, 10))
    for i in range(N):
        res[i][r[i]] = 1
    
    print res
    np.savetxt("test.predict", res, fmt='%i')
    
    print "finished predicting."
   


if __name__ == '__main__':
    run()