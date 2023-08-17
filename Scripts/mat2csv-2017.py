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
NOTE: This file does the exact same thing mat2csv.py does, rather instead, for the Nichols 2017 data

Due to his naming convention and file structure, a new, slightly different script needed to be implemented

No new functions

All operate similarly
    
"""

dataset = 'n2_let'
#dataset = 'n2_prelet'

path = os.path.join('.', 'MAT_Files', dataset + '.mat')

traceDict = mat73.loadmat(path)

tableName, key = list(traceDict.items())[0]
statesTuple = key['FourStates']
states = []

for tup in statesTuple:
    _, vals = list(tup.items())[0]
    states.append(vals)


ids = key['IDs']
#print(len(ids[0]))
#print(ids)
traces = key['traces']


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


def df_2_csv(ids, traces, action, dataset):
    count = 1
    for i in range(len(ids)):
        uniqueIDs = unique_column_names(ids[i])
        df = pd.DataFrame(traces[i], columns=uniqueIDs)
        #Pad columns if size less than 105
        if df.shape[1] <= 105:
            for j in range(df.shape[1], 105):
                df['[]_' + str(j)] = 0.0
        #Remove extra columns if size is greater than 105
        if df.shape[1] > 105:
            toBeRemoved = []
            limiter = df.shape[1] - 105
            for col in enumerate(reversed(df.columns)):
                if len(toBeRemoved) < limiter:
                    if df.shape[1] > 105 and col[1].startswith('[]'):
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