# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 18:28:05 2015

@author: AkishinoShiame
"""

from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


pil_im = Image.open( "sample_02.jpg" )
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