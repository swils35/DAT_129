#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:45:32 2019

@author: StephanieWilson
"""

import numpy  # array instead of list
import pandas as pd
import matplotlib
import csv

from pandas import DataFrame, Series # dataframe = table, series = column

seriesObj = Series([80000, 60000, 34000, 2100000],['Indian', 'Greek', 'Latin', 'Chili'])

print(seriesObj)
print(seriesObj.mean())
print(seriesObj.sum())

#with open('usaPowerSources2001-2018.csv') as csvfile:
#    reader = csv.DictReader(csvfile, delimiter=',')
#    energy = [row for row in reader]
#
#energyDF = DataFrame(energy)
#print(energyDF)
#
#print(energyDF.astype({'coal':'float64'}).describe())

energySourcesPD = pd.read_csv('usaPowerSources2001-2018.csv', index_col='Month')
print(energySourcesPD.dtypes)
print(energySourcesPD.describe())
print(energySourcesPD.plot())


    

