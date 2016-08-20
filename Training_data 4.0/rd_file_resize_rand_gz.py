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

thelist = np.array(['8_7', '11_1', '2_8', '13_4', '18_5', '7_1', '0_3', '1_0', '19_7', '3_3', '5_0',
                    '7_5', '7_3', '12_7', '6_4', '10_0', '10_1', '5_1', '10_8', '12_9', '8_2', '19_8',
                    '4_5', '14_9', '7_9', '19_2', '18_3', '15_1', '3_1', '6_1', '14_2', '7_4', '17_0',
                    '19_0', '5_4', '14_8', '15_5', '15_8', '7_6', '16_2', '8_3', '1_8', '13_8', '3_8',
                    '8_1', '11_8', '11_3', '17_5', '8_0', '8_6', '12_0', '18_2', '17_2', '17_8', '9_9',
                    '4_1', '11_0', '18_6', '13_3', '19_3', '10_5', '4_6', '5_3', '16_1', '12_3', '15_6',
                    '7_7', '17_4', '1_1', '4_7', '10_3', '3_6', '1_5', '11_4', '16_8', '9_3', '3_7',
                    '8_9', '13_9', '5_9', '11_9', '4_3', '0_2', '19_9', '2_0', '0_0', '10_9', '13_0',
                    '0_8', '8_5', '13_5', '8_8', '19_6', '12_1', '0_1', '4_8', '9_6', '0_4', '9_4',
                    '6_2', '19_5', '1_3', '17_3', '4_0', '19_4', '0_6', '9_0', '2_5', '14_5', '12_2',
                    '15_3', '18_4', '1_7', '11_5', '1_2', '1_4', '12_6', '18_8', '15_2', '16_7', '12_5',
                    '16_5', '10_2', '14_6', '5_8', '4_4', '15_4', '13_6', '16_4', '3_4', '19_1', '14_4',
                    '4_9', '6_8', '0_9', '1_6', '15_0', '5_7', '14_7', '2_3', '5_6', '14_0', '2_4',
                    '10_6', '17_6', '11_7', '13_2', '6_3', '0_5', '2_1', '3_2', '11_2', '2_9', '14_3',
                    '16_3', '17_9', '5_2', '18_1', '12_8', '6_5', '9_7', '9_8', '9_1', '6_6', '11_6',
                    '7_2', '8_4', '9_2', '5_5', '18_7', '16_0', '3_5', '14_1', '2_7', '13_7', '4_2',
                    '6_9', '3_0', '13_1', '1_9', '18_9', '7_8', '17_7', '16_6', '17_1', '9_5', '3_9',
                    '0_7', '18_0', '6_0', '6_7', '2_6', '15_9', '15_7', '10_4', '10_7', '16_9', '7_0',
                    '12_4', '2_2'])

final_output = np.zeros((200,147456),dtype=np.float32)
final_label = np.array([8, 11, 2, 13, 18, 7, 0, 1, 19, 3, 5, 7, 7, 12, 6, 10, 10, 5, 10, 12, 8, 19, 4, 14, 7, 19, 18, 15, 3, 6, 14, 7, 17, 19, 5, 14, 15, 15, 7, 16, 8, 1, 13, 3, 8, 11, 11, 17, 8, 8, 12, 18, 17, 17, 9, 4, 11, 18, 13, 19, 10, 4, 5, 16, 12, 15, 7, 17, 1, 4, 10, 3, 1, 11, 16, 9, 3, 8, 13, 5, 11, 4, 0, 19, 2, 0, 10, 13, 0, 8, 13, 8, 19, 12, 0, 4, 9, 0, 9, 6, 19, 1, 17, 4, 19, 0, 9, 2, 14, 12, 15, 18, 1, 11, 1, 1, 12, 18, 15, 16, 12, 16, 10, 14, 5, 4, 15, 13, 16, 3, 19, 14, 4, 6, 0, 1, 15, 5, 14, 2, 5, 14, 2, 10, 17, 11, 13, 6, 0, 2, 3, 11, 2, 14, 16, 17, 5, 18, 12, 6, 9, 9, 9, 6, 11, 7, 8, 9, 5, 18, 16, 3, 14, 2, 13, 4, 6, 3, 13, 1, 18, 7, 17, 16, 17, 9, 3, 0, 18, 6, 6, 2, 15, 15, 10, 10, 16, 7, 12, 2],dtype=np.int64)

for i in range(200):
    print "reading", i, "..."
    pil_im = Image.open( "training_font_transparent/" + thelist[i] + ".jpg" ).convert('L')
    #imshow(np.asarray(pil_im)) # before resize
    pil_im = pil_im.resize((512, 288), Image.BILINEAR )
    pil_im = np.array(pil_im)
    fig = plt.figure()
    plotwindow = fig.add_subplot()
    plt.imshow(pil_im, cmap='gray')
    plt.show()
    #print("test")
    #print(pil_im)
    note = 0
    for j in range(288):
        for k in range(512):
            final_output[i][note]= ((255 - pil_im[j][k])/225.)
            note += 1

print " "
print "Finished Picture..."
print "Starting label"
  
print "Finished Labeling..."

print "Starting cpickle"
outputandlabel = final_output, final_label
f = gzip.open("training_data_200v4.pkl.gz", 'wb')
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