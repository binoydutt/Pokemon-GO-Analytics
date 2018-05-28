# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 04:19:34 2017
Binoy Dutt
Priya Sanodia
@author: binoy
"""
import Image
import os

files = os.listdir('C:/UTA/Data Science/Project2/Images/android')

for images in files:
    i = 0    
    im = Image.open("images/android/android_image_{}.png".format(i))
    rgb_im = im.convert('RGB')
    rgb_im.save('images/android/file_{}.jpg'.format(i),'JPEG')
    i+=1