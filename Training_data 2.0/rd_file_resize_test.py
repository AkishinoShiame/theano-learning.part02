# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 18:46:28 2015

@author: winpython
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cPickle

temp_line = np.zeros(784)
final_output = np.empty((200,784),dtype=np.float32)
final_label = np.ones((200),dtype=np.int64)

cd = 0
for i in range(10):
    for j in range (20):
        print "i", i , " j", j
        pil_im = Image.open( str(i) + "_" + str(j) + ".jpg" ).convert('L')
        imshow(np.asarray(pil_im)) # before resize
        pil_im = pil_im.resize((28, 28), Image.BILINEAR )
        pil_im = np.array(pil_im)
        fig = plt.figure()
        plotwindow = fig.add_subplot()
        plt.imshow(pil_im, cmap='gray')
        plt.show()
        
        #print("test")
        #print(pil_im)
        
        cr = 0
        
        print "Read line", cd ,
        for k in range(28):
            for l in range(28):
                temp_line[cr]= pil_im[k][l]/225.
                print " in ", cr, "..."                
                cr += 1
                
        print "Combine line"
        final_output[cd] = temp_line
        cd += 1
        
print "Finished Picture..."
print "Starting label"
cntddd = 0
for i in range(10):
    for j in range (20):
        final_label[cntddd] = i
        cntddd += 1
        
print "Finished Labeling..."

print "Starting cpickle"
outputandlabel = final_output, final_label
f = file("training_data.pkl", 'wb')
cPickle.dump(outputandlabel, f, protocol=cPickle.HIGHEST_PROTOCOL)
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