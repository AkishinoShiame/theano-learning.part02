# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 12:16:19 2015

@author: AkishinoShiame
"""

import numpy as np
a = np.array([1,2,3])
print a[0], a[1], a[2]
b = a
print b[0], b[1], b[2]

b[2] = 1000
print a 
print b