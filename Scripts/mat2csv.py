#DONT FORGET pip install mat73
import mat73
import numpy as np 
import pandas as pd
from scipy.io import loadmat
import scipy.io as sio
from sklearn.preprocessing import PolynomialFeatures
from IPython.display import display
import os


"""
NOTE: This entire file has been pre run and saved for all possible data in DatasetsTest Folder

If running this file for the sake of testing functionality, please:

    1. Uncomment which dataset you are currently working with
    3. Press play
    4. Files should appear in the DatasetsTest Folder

"""
#NOTE: UNCOMMENT HERE
dataset = 'AVA_HisCl'
#dataset = 'WT_Stim'

path = os.path.join('.', 'MAT_Files', dataset + '.mat')

traceDict = mat73.loadmat(path)

tableName, key = list(traceDict.items())[0]
states = key['States']
ids = key['IDs']
traces = key['traces_raw']

for i in range(len(ids)):
    for j in range(len(ids[i])):
        #If entry is a list convert to string
        if isinstance(ids[i][j], list):
            if len(ids[i][j]) == 0 or all(item is None for item in ids[i][j]):
                ids[i][j] = '[]'
            else:
                #Join table cells containing more than one neuron
                ids[i][j] = '/'.join(filter(None, ids[i][j])) 
        elif ids[i][j] is None:
            ids[i][j] = '[]'

for i in range(len(ids)):
    for j in range(len(ids[i])):
        if isinstance(ids[i][j], str) == False:
            print('we have a problem')
            print(i)
            print(j)

"""
An attempt at ensuring columns do not have the same name by numbering them

    - Helper function

Usage:
    uniqueIDs = unique_column_names(ids)

Arguments:
    ids: list of neuron names

Returns:
    newIDs: list of neuron names, instead any unnamed neuron is now denoted "[]_{number}:
"""

def unique_column_names(ids):
    countDict = {}
    newIDs = []
    for i in ids:
        if i not in countDict:
            countDict[i] = 0
        else:
            countDict[i] += 1

        if countDict[i] == 0:
            newIDs.append(i)
        else:
            newIDs.append(i + '_' + str(countDict[i]))

    return newIDs

"""
Creates a dataframe object for each dataset in a particular year's study (e.g. Kato 2015) and then converts
them individually into CSV format

Usage:
    df_2_csv(ids, traces, states, dataset)

Arguments:
    ids: list of neuron names
    traces: list of trace data
    states: list of states (recorded behavior)
    dataset: The name of the dataset being worked on

Returns:
    None: Creates new CSV files in DatasetsTest Folder
"""

def df_2_csv(ids, traces, action, dataset):
    count = 1
    for i in range(len(ids)):
        uniqueIDs = unique_column_names(ids[i])
        df = pd.DataFrame(traces[i], columns=uniqueIDs)
        #Pad columns if size less than 134
        if df.shape[1] <= 134:
            for j in range(df.shape[1], 134):
                df['[]_' + str(j)] = 0.0
        #Remove extra columns if size is greater than 134
        if df.shape[1] > 134:
            toBeRemoved = []
            limiter = df.shape[1] - 134
            for col in enumerate(reversed(df.columns)):
                if len(toBeRemoved) < limiter:
                    if df.shape[1] > 134 and col[1].startswith('[]'):
                        toBeRemoved.append(col[0])
            
            for index in toBeRemoved:
                value = (df.shape[1] - index) - 1
                df.rename(columns={df.columns[value]: 'remove'}, inplace=True)

            
            df = df.drop(columns=['remove'], axis=1)
            
        
        df['Action'] = action[i]
        filename = os.path.join('.', 'DatasetsTest', dataset + str(count) + '.csv')
        df.to_csv(filename, index=False)
        count += 1

    
df_2_csv(ids, traces, states, dataset)
