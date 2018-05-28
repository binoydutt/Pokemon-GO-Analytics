# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 14:14:14 2017
Binoy Dutt
Priya Sanodia
@author: binoy
"""
from bs4 import BeautifulSoup
import urllib
import os
import json
import pickle

error_a_image =[]

folders = os.listdir('C:\UTA\Data Science\Project2\pokemon_5378\data')

a_images = set()

for folder in folders:
    print '{} - Start'.format(folder) 
    filenames = os.listdir('C:\UTA\Data Science\Project2\pokemon_5378\data\{}'.format(folder))
    for files in filenames:
 
        if files.endswith('android.html'):
                r = urllib.urlopen('file:///C:/UTA/Data%20Science/Project2/pokemon_5378/data/{}/{}'.format(folder,files)).read()
                soup = BeautifulSoup(r, "lxml")
                a_image_links = soup.find_all("img",{"class":"full-screenshot"})                
                try:                
                    for image in a_image_links:
                        try:
                            a_images.add(image['src'])
                        except:
                            error_a_image.append('{}/{}'.format(folder,files))
                            print 'Image URL not found {}/{}'.format(folder,files)
                except:
                    error_a_image.append('{}/{}'.format(folder,files))
                    print 'No images found {}/{}'.format(folder,files)
        
    print '{} - End'.format(folder)
    
error_list = {
'error_a_image':error_a_image,
'Total_error_a_image': len(error_a_image),
}


with open('error_image_android.json','w') as f:
    json.dump(error_list,f,indent =4)
                
with open('android_image.pickle','w') as f:
    pickle.dump(a_images,f)    
