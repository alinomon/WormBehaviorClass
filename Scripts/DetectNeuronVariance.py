import mat73
import numpy as np 
import pandas as pd
from scipy.io import loadmat
import scipy.io as sio
from sklearn.preprocessing import PolynomialFeatures
from IPython.display import display
import os
import glob
import math

"""
calculate the standard deviation of every neuron, named or unnamed, in a given dataset
NOTE: In the final implementation, this file is now exclusively being used as a helper
Nothing needs to be run here. All calls to these functions are executed in the main Jupyter Notebook

Usage:
    stand_dev = standard_deviation_calc(df)

Arguments:
    df: the dataframe that will be parsed

Returns:
    stand_dev: List containing n tuples, where n is the number of neurons in the given dataset. index 0 of tuple
    contains the standard deviation, index 1 contains the column
"""
def standard_deviation_calc(df):
    dfNoAction = df.drop('Action', axis=1)
    stand_dev = []
    for col in dfNoAction:
        vals = dfNoAction[col].values # x
        N = len(vals) #Length of the column
        mean = (sum(vals) / N)
        P = 0

        #Subtract the mean from each data point
        #Absolute value
        #Square it
        #Add to P (The numerator of the equation)
        for i in vals:
            temp = abs(i - mean) ** 2
            P += temp
        
        #Divide by N (col length)

        P = P / N
        sigmoid = math.sqrt(P)

        stand_dev.append((sigmoid, col))

    return stand_dev

#variance = standard_deviation_calc(df)

"""
Calculate which neurons have the largest and smallest degree of standard deviation

Usage:
    high10, low10 = calculate_high_low(stand_dev)

Arguments:
    stand_dev: the output of the standard_deviation_calc function. requires a list of tuples

Returns:
    largest10: List containing the 10 neurons with largest degree of variation
    smallest10: List containing the 10 neurons with smallest degree of variation
"""

def calculate_high_low(stand_dev):
    largestToSmallest = sorted(stand_dev, reverse=True)
    largest10 = largestToSmallest[:10]
    print("Largest:\n")
    for i, num in enumerate(largest10):
        print(f"{i+1}. {num}")
    print("\n\n")

    smallest10 = []
    count = 0
    for i in sorted(stand_dev):
        if i[0] != 0:
            smallest10.append(i)
        
        if len(smallest10) == 10:
            break

    print("Smallest:\n")
    for i, num in enumerate(smallest10):
        print(f"{i+1}. {num}")

    return largest10, smallest10

#large10, small10 = calculate_high_low(variance)

"""
writes two CSV's with the neurons with largest and smallest degrees of standard deviation removed respectively

Usage:
    write_altered_csv(df, high10, low10, testFileName)

Arguments:
    df: the unaltered, vanilla dataset
    high10: List containing the 10 neurons with largest level of variation
    low10: List containing the 10 neurons with smallest level of variation
    testFileName: 

Returns:
    Nothing. Creates two new CSV files in TestData Folder
"""

def write_altered_csv(df, large, small, dataset):
    dfLargest = df.copy()
    dfSmallest = df.copy()

    for entry in large:
        dfLargest[entry[1]] = 0

    for entry in small:
        dfSmallest[entry[1]] = 0

    filenameLarge = os.path.join('.', 'TestData', dataset + '_LargestRemoved' + '.csv')
    dfLargest.to_csv(filenameLarge, index=False)

    filenameSmall = os.path.join('.', 'TestData', dataset + '_SmallestRemoved' + '.csv')
    dfSmallest.to_csv(filenameSmall, index=False)

#write_altered_csv(df, largest10, smallest10, dataset)

