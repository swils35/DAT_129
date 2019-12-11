#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:39:01 2019

@author: StephanieWilson
"""


#open file to read
with open("names.txt", "r") as names:
    formalities = names.read()

        
    formalities_list = formalities.split()
    
    for l in range(len(formalities_list)):
        
        if (l + 1) % 2 == 0:
            lastName = formalities_list[l]
#            print(lastName)
            
        else:
            firstName = formalities_list[l]
#            print(firstName)
            
    print("Good evening Dr. " + lastName + ", would you mind if I called you " 
          + firstName + "?")