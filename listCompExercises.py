#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:54:46 2019

@author: StephanieWilson
"""

#res = [x + x + x for x in "KABOOM"]
#print(str(res))
#
#list = [i for i in range(10, -1, -1)]
#print(list)
#
lines = [line.rstrip().replace('\'', '') for line in open('example.txt') if 'Purple' in line or 'purple' in line]
print(lines)