# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 04:03:19 2015

@author: winpython
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cPickle, pickle
import gzip

thelist = np.array(['8_7', '1_12', '2_8', '3_15', '8_16', '7_1', '0_3', '1_0', '9_18', '3_3', '5_0',
                    '7_5', '7_3', '2_18', '6_4', '0_11', '0_12', '5_1', '0_19', '2_10', '8_2', '9_19',
                    '4_5', '4_10', '7_9', '9_13', '8_14', '5_12', '3_1', '6_1', '4_13', '7_4', '7_11',
                    '9_11', '5_4', '4_19', '5_16', '5_19', '7_6', '6_13', '8_3', '1_8', '3_19', '3_8',
                    '8_1', '1_19', '1_14', '7_16', '8_0', '8_6', '2_11', '8_13', '7_13', '7_19', '9_9',
                    '4_1', '1_11', '8_17', '3_14', '9_14', '0_16', '4_6', '5_3', '6_12', '2_14', '5_17',
                    '7_7', '7_15', '1_1', '4_7', '0_14', '3_6', '1_5', '1_15', '6_19', '9_3', '3_7',
                    '8_9', '3_10', '5_9', '1_10', '4_3', '0_2', '9_10', '2_0', '0_0', '0_10', '3_11',
                    '0_8', '8_5', '3_16', '8_8', '9_17', '2_12', '0_1', '4_8', '9_6', '0_4', '9_4',
                    '6_2', '9_16', '1_3', '7_14', '4_0', '9_15', '0_6', '9_0', '2_5', '4_16', '2_13',
                    '5_14', '8_15', '1_7', '1_16', '1_2', '1_4', '2_17', '8_19', '5_13', '6_18', '2_16',
                    '6_16', '0_13', '4_17', '5_8', '4_4', '5_15', '3_17', '6_15', '3_4', '9_12', '4_15',
                    '4_9', '6_8', '0_9', '1_6', '5_11', '5_7', '4_18', '2_3', '5_6', '4_11', '2_4',
                    '0_17', '7_17', '1_18', '3_13', '6_3', '0_5', '2_1', '3_2', '1_13', '2_9', '4_14',
                    '6_14', '7_10', '5_2', '8_12', '2_19', '6_5', '9_7', '9_8', '9_1', '6_6', '1_17',
                    '7_2', '8_4', '9_2', '5_5', '8_18', '6_11', '3_5', '4_12', '2_7', '3_18', '4_2',
                    '6_9', '3_0', '3_12', '1_9', '8_10', '7_8', '7_18', '6_17', '7_12', '9_5', '3_9',
                    '0_7', '8_11', '6_0', '6_7', '2_6', '5_10', '5_18', '0_15', '0_18', '6_10', '7_0',
                    '2_15', '2_2'])

final_output = np.zeros((200,784),dtype=np.float32)
final_label = np.array([8, 1, 2, 3, 8, 7, 0, 1, 9, 3, 5, 7, 7, 2, 6, 0, 0, 5, 0, 2, 8, 9, 4, 4, 7, 9, 8, 5, 3, 6, 4, 7, 7, 9, 5, 4, 5, 5, 7, 6, 8, 1, 3, 3, 8, 1, 1, 7, 8, 8, 2, 8, 7, 7, 9, 4, 1, 8, 3, 9, 0, 4, 5, 6, 2, 5, 7, 7, 1, 4, 0, 3, 1, 1, 6, 9, 3, 8, 3, 5, 1, 4, 0, 9, 2, 0, 0, 3, 0, 8, 3, 8, 9, 2, 0, 4, 9, 0, 9, 6, 9, 1, 7, 4, 9, 0, 9, 2, 4, 2, 5, 8, 1, 1, 1, 1, 2, 8, 5, 6, 2, 6, 0, 4, 5, 4, 5, 3, 6, 3, 9, 4, 4, 6, 0, 1, 5, 5, 4, 2, 5, 4, 2, 0, 7, 1, 3, 6, 0, 2, 3, 1, 2, 4, 6, 7, 5, 8, 2, 6, 9, 9, 9, 6, 1, 7, 8, 9, 5, 8, 6, 3, 4, 2, 3, 4, 6, 3, 3, 1, 8, 7, 7, 6, 7, 9, 3, 0, 8, 6, 6, 2, 5, 5, 0, 0, 6, 7, 2, 2],dtype=np.int64)

for i in range(200):
    print "reading", i, "..."
    pil_im = Image.open( thelist[i] + ".jpg" ).convert('L')
    #imshow(np.asarray(pil_im)) # before resize
    pil_im = pil_im.resize((28, 28), Image.BILINEAR )
    pil_im = np.array(pil_im)
    fig = plt.figure()
    plotwindow = fig.add_subplot()
    plt.imshow(pil_im, cmap='gray')
    plt.show()
    #print("test")
    #print(pil_im)
    note = 0
    for j in range(28):
        for k in range(28):
            final_output[i][note]= ((255 - pil_im[j][k])/225.)
            note += 1
            print " in ", note, "...",
        
print " "
print "Finished Picture..."
print "Starting label"
  
print "Finished Labeling..."

print "Starting cpickle"
outputandlabel = final_output, final_label
f = gzip.open("training_data.pkl.gz", 'wb')
cPickle.dump(outputandlabel, f)
f.close()
print "Finished cPickle..."
print "\ ! congradulation ! /" 
       
#f = open("pic1.txt", "r")
'''
imshow(np.asarray(pil_im)) # before resize
pil_im = pil_im.resize((28, 28), Image.BILINEAR )


pil_im = np.array(pil_im)

#print(np.array(pil_im))
#imshow(np.asarray(pil_im))

fig = plt.figure()
plotwindow = fig.add_subplot()
plt.imshow(pil_im, cmap='gray')
plt.show()

print("test")
print(pil_im)

'''