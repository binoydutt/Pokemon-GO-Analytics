# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 01:15:26 2017
Binoy Dutt
Priya Sanodia
https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/
@author: binoy
"""
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.cross_validation import  cross_val_score, cross_val_predict
from datetime import datetime
from pandas.stats.api import ols
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df =pd.read_csv('data.csv')
lst = df[u'Unnamed: 0']
dates = []
for a in lst:
    dates.append(datetime.strptime(a, "%Y-%m-%d %H:%M:%S"))
    
time = []
for date in dates:
    time.append(((date- dates[0]).total_seconds())/60)
p_time = ((datetime.strptime('2016/11/01 23:50:00', "%Y/%m/%d %H:%M:%S") - dates[0]).total_seconds())/60
summary = {}
def android(df):
    col = df.copy()
    col.drop(labels=['android_total_ratings'], axis=1, inplace=True)
    
    col.drop(labels=['Unnamed: 0'], axis=1, inplace=True)
    col.drop(labels=['android_file_size'], axis=1, inplace=True)
    #col.drop(labels=['android_avg_rating'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_1'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_2'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_3'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_4'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_5'], axis=1, inplace=True)
    col.drop(labels=['ios_all_ratings'], axis=1, inplace=True)
    #col.drop(labels=['ios_current_ratings'], axis=1, inplace=True)
    col.drop(labels=['ios_file_size'], axis=1, inplace=True)
    
    col.insert(loc=0, column='Time', value=time)
    col.head()
    
    y = df['android_total_ratings']
    ridgeregress(col,y, 'Android')
    lassoreg(col,y,'Android')
    linearreg(col,y,'Android')
    elasticnetreg(col,y, 'Android')
    
def ios(df):
    col = df.copy()
    #col.drop(labels=['android_total_ratings'], axis=1, inplace=True)
    
    col.drop(labels=['Unnamed: 0'], axis=1, inplace=True)
    col.drop(labels=['android_file_size'], axis=1, inplace=True)
    col.drop(labels=['android_avg_rating'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_1'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_2'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_3'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_4'], axis=1, inplace=True)
    #col.drop(labels=['android_rating_5'], axis=1, inplace=True)
    col.drop(labels=['ios_all_ratings'], axis=1, inplace=True)
    #col.drop(labels=['ios_current_ratings'], axis=1, inplace=True)
    col.drop(labels=['ios_file_size'], axis=1, inplace=True)
    
    col.insert(loc=0, column='Time', value=time)
    col.head()
    
    y = df['ios_all_ratings']
    ridgeregress(col,y, 'ios')
    lassoreg(col,y,'ios')
    linearreg(col,y,'ios')
    elasticnetreg(col,y, 'ios')
def ridgeregress(col, y, platform):
    model = Ridge(alpha = 0.001)
    scoring1 = 'r2'
    results_r2 = cross_val_score(model, col, y, cv=10, scoring=scoring1)
    predicted = cross_val_predict(model, col, y, cv=10)
    print results_r2.mean()
    scoring2 = 'mean_squared_error'
    results_mse = cross_val_score(model, col, y, cv=10, scoring=scoring2)
    print results_mse.mean()
    lst = col.tail(1)
    lst['Time'] = p_time
    model.fit(col,y)
    pred = model.predict(lst)
    print pred
    fig, ax = plt.subplots()
    ax.scatter(y, predicted)
    plt.suptitle('Ridge Regression')
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()
    summary['Ridge Regression {}'.format(platform)] = {' Mean Square Error':results_mse.mean(), 
                                    'R Square': results_r2.mean(),
                                     'Prediction': pred}
    

def lassoreg(col, y, platform):
    model = Lasso(alpha = 0.001, normalize = True)
    scoring1 = 'r2'
    results_r2 = cross_val_score(model, col, y, cv=10, scoring=scoring1)
    predicted = cross_val_predict(model, col, y, cv=10)
    print results_r2.mean()
    scoring2 = 'mean_squared_error'
    results_mse = cross_val_score(model, col, y, cv=10, scoring=scoring2)
    print results_mse.mean()
    lst = col.tail(1)
    lst['Time'] = p_time
    model.fit(col,y)
    pred = model.predict(lst)
    print pred
    fig, ax = plt.subplots()
    ax.scatter(y, predicted)
    plt.suptitle('Lasso')    
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    
    plt.show()
    summary['Lasso Regression {}'.format(platform)] = {' Mean Square Error':results_mse.mean(), 
                                    'R Square': results_r2.mean(),
                                     'Prediction': pred}

def linearreg(col,y, platform):
    model = LinearRegression()
    scoring1 = 'r2'
    results_r2 = cross_val_score(model, col, y, cv=10, scoring=scoring1)
    predicted = cross_val_predict(model, col, y, cv=10)
    print results_r2.mean()
    scoring2 = 'mean_squared_error'
    results_mse = cross_val_score(model, col, y, cv=10, scoring=scoring2)
    print results_mse.mean()
    lst = col.tail(1)
    lst['Time'] = p_time
    model.fit(col,y)
    pred = model.predict(lst)
    print pred
    fig, ax = plt.subplots()
    ax.scatter(y, predicted)
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    plt.suptitle('Linear Regression')
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()
    summary['Linear Regression {}'.format(platform)] = {' Mean Square Error':results_mse.mean(), 
                                    'R Square': results_r2.mean(),
                                     'Prediction': pred}
    
def elasticnetreg(col,y, platform):
    model = ElasticNet(alpha =0.01,fit_intercept= True,l1_ratio=0.7)
    scoring1 = 'r2'
    results_r2 = cross_val_score(model, col, y, cv=10, scoring=scoring1)
    predicted = cross_val_predict(model, col, y, cv=10)
    print results_r2.mean()
    scoring2 = 'mean_squared_error'
    results_mse = cross_val_score(model, col, y, cv=10, scoring=scoring2)
    print results_mse.mean()
    lst = col.tail(1)
    lst['Time'] = p_time
    model.fit(col,y)
    pred = model.predict(lst)
    print pred
    fig, ax = plt.subplots()
    ax.scatter(y, predicted)
    plt.suptitle('Elastic Net')
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()
    summary['Elastic Net {}'.format(platform)] = {' Mean Square Error':results_mse.mean(), 
                                    'R Square': results_r2.mean(),
                                     'Prediction': pred}
    
ios(df)
android(df)
data = pd.DataFrame(summary)
data_t =data.transpose()
data_t.to_excel('Summary.xlsx')
