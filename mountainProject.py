#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:31:36 2019

@author: StephanieWilson
"""
import requests, json

KEY = 'mpKey.txt'


def main():
    apiURL = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=%s&lon=-%s&maxDistance=10&minDiff=5.6&maxDiff=5.10&key=%s' %(str(38.02), str(81.081), getKey())
    getRouteList(apiURL)
    
def getKey():    
    with open (KEY, 'r') as apiKey:
        keyString = apiKey.read()
        return keyString

        
    
def getRouteList(url):
    req = requests.get(url)
    total = 0
    avg = 0
    
    if (int(req.status_code) == 200): # thanks Eric!
        dictionary = json.loads(req.text)        
        listOfRoutes = dictionary['routes']
        
        for p in listOfRoutes:
            
            print(p['id'], p['name'], str(p['rating'])) 
            
            cleanRoute = str(p['rating']).replace('+','')
            cleanerRoute = cleanRoute.replace('-','')
            squeakyCleanRoute = cleanerRoute.replace('a','')
            veryCleanRoute = squeakyCleanRoute.replace('b','')
            soFreshAndSoClean = veryCleanRoute.replace(' R','')
            couldEatOffThisRoute = soFreshAndSoClean.replace('a/b', '')
            seriouslyThough = couldEatOffThisRoute.replace('/', '')
            cleanestRoute = seriouslyThough.replace('5.','')    
                
           # print(p['id'], p['name'], cleanestRoute)                    
            total += int(cleanestRoute)
            
        avg = (total / len(listOfRoutes)) / 10
        avg = str(avg).replace('0.','')
        print()
        print("The average route rating in this area is: 5."+ avg)
        
        
        
    
    
    
    
main()