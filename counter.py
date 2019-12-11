#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:25:37 2019

@author: StephanieWilson
"""

# question: does the racial make up of the ACJ reflect the makeup of
# Allegheny Count at large on June 1, 2019

# 1. package race counts into a dictionary
    # you can package race counts into a dictionary
    # and generate from Data Dictionary
# 2. one date per month
# 3. average age @ booking by race

import csv

file = open("jail_june_2019.csv", newline="")

reader = csv.DictReader(file)


totBlack = 0
totWhite = 0
censusDate = "2019-06-01"

# Date,Gender,Race,Age at Booking,Current Age

for row in reader:
    if row["Date"] == censusDate:
        if row["Race"] == "B":
            totBlack += 1
        elif row["Race"] == "W":
            totWhite +=1
            
file.close()

print("Total white count on June 1, 2019" + str(totWhite))
percWhite = totWhite / (totBlack + totWhite)
print("White percent: " + str(percWhite))
print()
print("Total black count on June 1, 2019" + str(totBlack))
percBlack = totBlack / (totBlack + totWhite)
print("Black percent: " + str(percBlack))
            
        