# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:03:15 2017
Binoy Dutt
Priya Sanodia
@author: binoy
"""
from __future__ import division
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates



df =pd.read_csv('data.csv')
print df.describe()
dates =[]
array = np.asarray(df)
x = array[:,0]
for a in x:
    dates.append(datetime.strptime(a, "%Y-%m-%d %H:%M:%S"))

y = array[:,[3,4,5,6,7]]

#http://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib
#http://stackoverflow.com/questions/14632729/matplotlib-make-x-axis-longer
fig, ax = plt.subplots(1, figsize = (15,5))
fig.autofmt_xdate()
plt.tight_layout()
plt.plot(dates, array[:,3], label = 'Android 1 rating')
plt.plot(dates, array[:,4], label = 'Android 2 rating')
plt.plot(dates, array[:,5], label = 'Android 3 rating')
plt.plot(dates, array[:,6], label = 'Android 4 rating')
plt.plot(dates, array[:,7], label = 'Android 5 rating')
plt.xlabel('Date and Time')
plt.ylabel('Ratings')
plt.legend(loc = 'upper left')
fig.subplots_adjust(bottom=0.3)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.savefig('Android_Rating_Plot.png')
plt.show()


fig, ax = plt.subplots(1, figsize = (15,5))
fig.autofmt_xdate()
plt.tight_layout()
plt.plot(dates, array[:,1], label = 'Average Rating')
plt.xlabel('Date and Time')
plt.ylabel('Average Rating')
plt.legend(loc = 'upper left')
fig.subplots_adjust(bottom=0.3)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.savefig('Android_Average_Rating_Plot.png')
plt.show()


fig, ax = plt.subplots(1, figsize = (15,5))
fig.autofmt_xdate()
plt.tight_layout()
plt.plot(dates, array[:,11], label = 'ios file size')
plt.plot(dates, array[:,2], label = 'Android File size')
plt.xlabel('Date and Time')
plt.ylabel('File Size')
plt.legend(loc = 'upper left')
fig.subplots_adjust(bottom=0.3)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.savefig('File Size.png')
plt.show()

fig, ax = plt.subplots(1, figsize = (15,5))
fig.autofmt_xdate()
plt.tight_layout()
plt.plot(dates, array[:,10], label = 'ios Current Ratings')
plt.xlabel('Date and Time')
plt.ylabel('Ratings')
plt.legend(loc = 'upper left')
fig.subplots_adjust(bottom=0.3)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.savefig('IOS Current Ratings.png')
plt.show()


fig, ax = plt.subplots(1, figsize = (15,5))
fig.autofmt_xdate()
plt.tight_layout()
plt.plot(dates, array[:,9], label = 'ios All Ratings')
plt.xlabel('Date and Time')
plt.ylabel('Ratings')
plt.legend(loc = 'upper left')
fig.subplots_adjust(bottom=0.3)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.savefig('IOS All Ratings.png')
plt.show()


fig, ax = plt.subplots(1, figsize = (15,5))
fig.autofmt_xdate()
plt.tight_layout()
plt.plot(dates, array[:,8], label = 'Android Total Ratings')
plt.xlabel('Date and Time')
plt.ylabel('Ratings')
plt.legend(loc = 'upper left')
fig.subplots_adjust(bottom=0.3)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.savefig('Android All Ratings.png')
plt.show()


array = np.asarray(df)
coeff = {}
#
#sns.pairplot(df)
#plt.show()
#plt.savefig("scatter_Matrix.pdf")

sns_plot = sns.pairplot(df)
sns_plot.savefig("output.png")

for i in range(1, 12):
    key1 = df.columns[i]
    for j in range(i+1,12):
        key2 = df.columns[j]
        coeff['{} + {}'.format(key1,key2)] ={'Pearsons Coefficient':np.corrcoef(array[:,i].astype('float64'), array[:,j].astype('float64'))[0][1]}

data = pd.DataFrame(coeff)

data.transpose().to_excel('Pearson.xlsx')