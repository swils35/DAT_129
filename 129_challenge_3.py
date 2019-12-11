#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:50:14 2019

@author: StephanieWilson
"""

# slice the string so it only outputs every other character

string = "askaliceithinkshe'llknow"

list = string.split(" ")

for i in range(1, len(list), 2):
    print(list[i])

