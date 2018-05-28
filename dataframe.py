# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:18:47 2017
Binoy Dutt
Priya Sanodia
@author: binoy
"""

import pandas as pd
import pickle
with open('data.pickle','r') as f:
    data = pickle.load(f)   
    


df = pd.DataFrame(data)
print df.head()


df_t = df.transpose()
print df_t.head()
print df_t.describe()

df_t.to_json('raw_data.json')

#
#x =pd.read_csv('data.csv')
#print x.describe()