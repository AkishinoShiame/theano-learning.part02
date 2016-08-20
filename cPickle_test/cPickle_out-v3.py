# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:30:17 2015

@author: AkishinoShiame
"""

import cPickle, gzip, theano.tensor

### file out put code below
try:
    out1 = open("CR_data-train_set.pic.txt","w")
    out2 = open("CR_data-train_set.lab.txt","w")
    out3 = open("CR_data-valid_set.pic.txt","w")
    out4 = open("CR_data-valid_set.lab.txt","w")
    out5 = open("CR_data-test_set.pic.txt","w")
    out6 = open("CR_data-test_set.lab.txt","w")
except IOError:
    print ("file open error")
### file out put code above


# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
###### above is origional pkl read file


##### below test seprate file to pic and label 
train_set_pic , train_set_lab = train_set
valid_set_pic , valid_set_lab = valid_set
test_set_pic , test_set_lab = test_set
##### above test seprate file to pic and label


out1.write("train set picture\n")
temp1 = train_set_pic[0]
#output train_set picture
for i in range(1):
    for j in range(len(temp1)): #""""""
        out1.write(str(train_set_pic[i][j]))
        out1.write(",")
#output train_set label
out2.write("train set label\n")
for i in range(len(train_set_lab)):
    out2.write(str(train_set_lab[i]))
    out2.write(",")


print ("training set :", train_set_pic)
print ("training set lab :", train_set_lab)

temp2 = valid_set_pic[0]
out3.write("valid set picture\n")
#output valid_set picture
for i in range(1):
    for j in range(len(temp2)):#""""""
        out3.write(str(valid_set_pic[i][j]))
        out3.write(",")
#output valid_set label
out4.write("valid set label\n")
for i in range(len(valid_set_lab)):
    out4.write(str(valid_set_lab[i]),)
    out4.write(",")

print ("valid set :", valid_set_pic)
print ("valid set lab :", valid_set_lab)

temp3 = test_set_pic[0]
#output test_set picture
out5.write("test set\n")
for i in range(1):
    for j in range(len(temp3)): #""""""
        out5.write(str(test_set_pic[i][j]))
        out5.write(",")
#output test_set label
#out6.write(str(test_set_lab.eval()))
for i in range(len(test_set_lab)):
    out6.write(str(test_set_lab[i]))
    out6.write(",")

print type(test_set_lab)
print ("test set :", test_set_pic)
print ("test set lab :", test_set_lab)

### file out put code below
out1.close()
out2.close()
out3.close()
out4.close()
out5.close()
out6.close()
### file out put code above

###### below is origional pkl read file
f.close()