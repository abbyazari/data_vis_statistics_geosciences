'''
externalfunctions.py

- Written on 3/6/2018 for CLaSP 405 by Lab TA A. Azari. 
Purpose:
- To import OMNI data, and run metrics on said data.

'''

def loadOmniData(filepath):
    '''
    This function loads into Python as a Pandas dataframe
    and cleans the data. Warning - this only works
    for columns as specified in the following order:
    
    ['YEAR', 'DOY', 'Hour', 'BX', 'BY', 'BZ', 'FlowPressure', 'Ey', 'Kp', 
    'SunspotNumber', 'Dst', 'f10.7_index']

    '''
    import datetime as dt
    import pandas as pd
    import numpy as np
    
    colNames = ['YEAR', 'DOY', 'Hour', 'BX', 'BY', 'BZ', 'FlowPressure', 'Ey', 'Kp', 
            'SunspotNumber', 'Dst', 'f10.7_index']

    data = pd.read_csv('./Data/omni2_Hourly1980_2018.lst', sep = '\s+', names = colNames,
                          parse_dates = {'Datetime': colNames[0:3]}, keep_date_col = 'True')

    data.index = pd.to_datetime(data['Datetime'], infer_datetime_format = False, 
                                   format = '%Y %j %H')
    
    data[['BX', 'BY', 'BZ', 'f10.7_index']] = data[[
        'BX', 'BY', 'BZ', 'f10.7_index']].replace(to_replace = 999.9, value = np.nan)

    data['FlowPressure'] = data['FlowPressure'].replace(
        to_replace = 99.99, value = np.nan)

    data['Ey'] = data['Ey'].replace(
        to_replace = 999.99, value = np.nan)

    data[['SunspotNumber', 'Kp']] = data[['SunspotNumber', 'Kp']].replace(
        to_replace = 999, value = np.nan)
    
    return(data)

def calcPOD(H, M):
    '''
    Takes in the hits, and misses, and returns the probability of detection. 
    '''
    
    return((H / (1.0*(H + M))))

def calcPFD(F, N):
    '''
    Takes in the hits, and misses, and returns the prob. of false detection. 
    '''
    
    return((F / (1.0*(F + N))))