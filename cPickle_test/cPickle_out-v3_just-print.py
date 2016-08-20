# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:30:17 2015

@author: AkishinoShiame
"""

import cPickle, gzip, numpy

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
###### above is origional pkl read file


##### below test seprate file to pic and label 
train_set_pic , train_set_lab = train_set
valid_set_pic , valid_set_lab = valid_set
test_set_pic , test_set_lab = test_set
##### above test seprate file to pic and label


print ("train set picture\n")
print train_set_pic
#output train_set label
print ("train set label\n")
print train_set_lab


print ("valid set picture\n")
#output valid_set picture
print valid_set_pic
#output valid_set label
print ("valid set label\n")
print valid_set_lab


#output test_set picture
print ("test set\n")
print test_set_pic
#output test_set label
print (test_set_lab)

###### below is origional pkl read file
f.close()