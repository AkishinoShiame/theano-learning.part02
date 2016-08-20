# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 10:45:27 2015

@author: AkishinoShiame
"""

import PIL
from PIL import Image

basewidth = 28
img = Image.open('lurofan.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('resized_lurofan.jpg')