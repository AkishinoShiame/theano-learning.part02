# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:30:17 2015

@author: AkishinoShiame
"""

import cPickle, gzip, numpy

### file out put code below
try:
    out1 = open("data-train_set_only1.out.txt","w")
    out2 = open("data-valid_set_only1.out.txt","w")
    out3 = open("data-test_set_only1.out.txt","w")
except IOError:
    print ("file open error")
### file out put code above


# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
###### above is origional pkl read file

out1.write("train set\n")
temp1 = train_set[0]
for i in range(1):
    for j in range(len(temp1)): #""""""
        out1.write(str(train_set[i][j]))

#print ("training set :", train_set)

temp2 = valid_set[0]
out2.write("valid set\n")
for i in range(1):
    for j in range(len(temp2)):#""""""
        out2.write(str(valid_set[i][j]))

print ("valid set :", valid_set)

temp3 = test_set[0]
out3.write("test set\n")
for i in range(1):
    for j in range(len(temp3)): #""""""
        out3.write(str(test_set[i][j]))

print ("test set :", test_set)

### file out put code below
out1.close()
out2.close()
out3.close()
### file out put code above

###### below is origional pkl read file
f.close()