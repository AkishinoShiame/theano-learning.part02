# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 19:26:31 2015

@author: AkishinoShiame
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import pickle, cPickle, gzip

### file out put code below
try:
    out = gzip.open('pictest.pkl.gz', 'wb')
except IOError:
    print ("file open error")
### file out put code above


pil_im = Image.open( "sample01.jpg" )
#f = open("pic1.txt", "r")

imshow(np.asarray(pil_im)) # before resize
pil_im = pil_im.resize((28, 28), Image.BILINEAR )


pil_im = np.array(pil_im)

#print(np.array(pil_im))
#imshow(np.asarray(pil_im))

fig = plt.figure()
plotwindow = fig.add_subplot()
plt.imshow(pil_im, cmap='gray')
plt.show()


print(" ")
print("Origional :")
print(" ")
print(pil_im)

print(" ")
release_final = np.zeros((4,784),dtype=np.float32)


print ("revert & mixmal")
for i in range(4):
    cout = 0
    for j in range(28):
        for k in range(28):
            print ((255 - pil_im[j][k])/255.),
            release_final[i][cout]=((255 - pil_im[j][k])/255.)
            cout += 1
print (release_final)

lab_list = np.array([1,1,4,1], dtype=np.int64)
print lab_list

End_final_out = release_final, lab_list

print ("output to file...")
pickle.dump(End_final_out , out)
print ("Finished output!")

out.close()

print ("#################################################################")
#print pickle file for test
f = gzip.open('pictest.pkl.gz', 'rb')
sets = cPickle.load(f)
picset , labset = sets

print ("ALL")
print (sets)

print ("seperated pic(in 1)")

for i in range(784):
    print picset[0][i], ",",
    
print ("seperated lab")
print labset

f.close()




