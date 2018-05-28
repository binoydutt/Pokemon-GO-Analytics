# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:06:37 2017
Binoy Dutt
Priya Sanodia
@author: binoy
"""


import urllib
import pickle

with open('android_image.pickle','r') as f:
    data = pickle.load(f)

image_list = list(data)




for i  in range(len(image_list)):
    print i
    urllib.urlretrieve('http:{}'.format(image_list[i]), "images/android/android_image_{}.png".format(i))