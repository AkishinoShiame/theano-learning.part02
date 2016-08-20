# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:44:52 2015

@author: winpython
"""

import cPickle

f = file("training_data.pkl", 'rb')
final = cPickle.load(f)
f.close()
final_output, final_label = final
print final

print "pic"
print final_output
print "label"
print final_label