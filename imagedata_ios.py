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

error_ios_image = []

folders = os.listdir('C:\UTA\Data Science\Project2\pokemon_5378\data')

ios_images = set()

for folder in folders:
    print '{} - Start'.format(folder) 
    filenames = os.listdir('C:\UTA\Data Science\Project2\pokemon_5378\data\{}'.format(folder))
    for files in filenames:
        
        if files.endswith('ios.html'):
                s = urllib.urlopen('file:///C:/UTA/Data%20Science/Project2/pokemon_5378/data/{}/{}'.format(folder,files)).read()
                soup1 = BeautifulSoup(s, "lxml")
                ios_image_links = soup1.find_all("img", {"class":"portrait","itemprop":"screenshot"})
                try:                
                    for image in ios_image_links:
                        try:
                            ios_images.add(image['src'])
                        except:
                            error_ios_image.append('{}/{}'.format(folder,files))
                            print 'Image URL not found {}/{}'.format(folder,files)
                except:
                    error_ios_image.append('{}/{}'.format(folder,files))
                    print 'No images found {}/{}'.format(folder,files) 
                    
    print '{} - End'.format(folder)
    
error_list = {
'error_ios_image':error_ios_image,
'Total_error_ios_image': len(error_ios_image)
}


with open('error_image_ios.json','w') as f:
    json.dump(error_list,f,indent =4)
                

with open('ios_image.pickle','w') as f:
    pickle.dump(ios_images,f)                
