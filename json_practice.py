#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:18:16 2019

@author: StephanieWilson
"""

#json practice

import json

# simplest example of writing to a file.
with open('sampleJSONout.txt', 'w') as j_dump:
    
    j_dump.write(json.dumps({'student-count': 12, 'teacher-count': 1}))
    
# simplest example of reading in JSON
#testing = json.load('{"numbers":[4,3,2,1,3456], "first name": "steph", "hello":"world"}')
#print(testing)

with open('sampleJSONout.txt', 'r') as j_load:
    testing = json.load(j_load)
    print(testing)
    
#with open('searchCriteria.txt', 'r') as filter:
#    print(json.load(filter)