# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 04:57:36 2017
Binoy Dutt
Priya Sanodia
@author: binoy
"""
import pandas as pd
df =pd.read_json('raw_data.json')

for key in df:
    lst = df[key]
    if lst[0] ==0:
        lst[0]= lst[1]

    for i in range(1,len(lst)-1):
        if lst[i]== 0 and lst[i+1]== 0:
            lst[i] = lst[i-1]
        elif lst[i] == 0:
            lst[i] = (lst[i-1]+lst[i+1])/2
        else:
            continue
    if lst[-1] ==0:
        lst[-1] = lst[-2]
    df[key] == lst

print df.describe()

df.to_excel('data.xlsx')
df.to_json('data.json')
df.to_csv('data.csv')
