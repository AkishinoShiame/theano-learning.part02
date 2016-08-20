# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 11:05:40 2015

@author: mcu
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


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

print("test")
print(pil_im)

