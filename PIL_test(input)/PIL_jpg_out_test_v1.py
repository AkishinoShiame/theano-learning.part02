# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 18:24:04 2015

@author: AkishinoShiame
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

### file out put code below
try:
    out = open("Trans01pic.txt","w")
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
temp_a_line = list()
release_final = list()
print ("revert & mixmal")
for i in range(28):
    temp_a_line = list()
    for j in range(28):
        print ((255 - pil_im[i][j])/255.)
        temp_a_line.append((255 - pil_im[i][j])/255.)
    release_final.append(temp_a_line)
print (release_final)

print ("output to file...")
out.write(str(release_final))
print ("Finished output!")

out.close()