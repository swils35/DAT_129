#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:07:51 2019

@author: StephanieWilson
"""

from bs4 import BeautifulSoup
from time import sleep #thanks go here: https://www.dataquest.io/blog/web-scraping-beautifulsoup/
from random import randint #thanks go here: https://www.dataquest.io/blog/web-scraping-beautifulsoup/
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
import random
from textblob import TextBlob
import nltk
import pandas as pd

# only need to run these downloads the first time you run the program
# nltk.download('stopwords')
# nltk.download('names')

from nltk.corpus import stopwords
from nltk.corpus import names



def main():  
    # asking user to input the search phrase they want to send to request 
    # to tedTalks and the number of pages they'd like to retrieve results from.   
    term = input("Please enter a search term: ")
    count = int(input("How many pages would you like to search? "))
    count += 1
    
    pages = [str(i) for i in range(1, count)]
    
    readySetGo(term, count, pages)
    
    
    
def readySetGo(term, count, pages):                
    for page in pages:
                
        # cast the results of the request and retrieval of the HTML from the
        # specified URL to the variable 'page'
        page = getURL(page, term)
    
        # staggering the timing of requests so as not to overtax servers.
        sleep(randint(3,6))
    
        # parsing the HTML in 'page' inTo something you can work with
        soup = BeautifulSoup(page, 'html.parser')
        # find all instances of the specified div class and cast to 'talks'
        talks = soup.find_all('div', 'media__message')  
        
        try:
            results(talks)   
        # if more pages are requested than actually exist, the program throws
        # a keyError.
        except KeyError:
            print("Sorry, there aren't any more search results.")
            break            

             
        
def results(talks):
    speakers = []
    videos = []
    dictionary = {}
        
    # iterating through 'talks' to grab the speaker name and title
    # of their talk       
    for heading in talks:
        speaker = heading.find('h4', 'h12 talk-link__speaker').text
        speakers.append(speaker)
        
        video = heading.find('h4', 'f-w:700 h9 m5').text
        video = video.replace('\n','')
        videos.append(video)
        
        genderAnalysis = genderClassifier(speakers)
        sentimentAnalysis = sentiment(videos)      
        
        dictionary = {'speaker_name':speakers, 'speaker_gender': genderAnalysis,
                  'talk_title': videos, 'talk_sentiment': sentimentAnalysis} 
                  
    df = pd.DataFrame(dictionary)    
    print(df)
    print(df.groupby('speaker_gender').mean())

#    df.to_csv("talkAnalysis.csv", sep=',', index = False)



# analyze the sentiment of the tedTalk titles. 
# citation:
# Deitel, P. J., & Dietal, H. (2020). Intro to Python for computer science and 
# data science: learning to program with Ai, big data and the cloud. 
# New York: Pearson Education, Inc.
def sentiment(videos):
    sentimentpol = []
    
    for title in videos:
        stops = stopwords.words('english')
        blob = TextBlob(title)
        [word for word in blob.words if word not in stops]
               
        sentimentpol.append(blob.sentiment.polarity)
        
    return sentimentpol


        
# thanks go to https://www.geeksforgeeks.org/python-gender-identification-by-name-using-nltk/
def gender_features(word):
    
    if len(word) == 0:
        return None
    else:
        return {'last_letter':word[-1]} 
    
    
    
def genderClassifier(speakers):  
    # preparing a list of examples and corresponding class labels. 
    labeled_names = ([(name, 'male') for name in names.words('male.txt')]+
             [(name, 'female') for name in names.words('female.txt')]) 
  
    random.shuffle(labeled_names) 
  
    # use the feature extractor to process the names data. 
    featuresets = [(gender_features(n), gender)
               for (n, gender)in labeled_names] 
  
    # Divide the resulting list of feature 
    # sets into a training set and a test set. 
    train_set, test_set = featuresets[500:], featuresets[:500] 
  
    # The training set is used to  
    # train a new "naive Bayes" classifier. 
    classifier = nltk.NaiveBayesClassifier.train(train_set) 

    # split the first and last names into lists and specify which one is the first 
    # name to use for gender classification.
    gender = []
    
    for name in speakers:
        list = name.split(' ')
        firstName = list[0]
        if (firstName.isalpha()) == True:
            lastLetter = gender_features(firstName)
        
            if lastLetter:
                gender.append(classifier.classify(gender_features(firstName)))
                
        else:
            gender.append('Unknown')
               
    return gender    
    


# specify the URL                                     
def getURL(page, string):
    try: 
        url = urlopen('https://www.ted.com/talks?page=%s&q=%s' % (page, str(string)))
        
    except HTTPError:
        print('The page could not be found!')

    except URLError:
        print('The server could not be found!')
    
    else:        
        return url 

main()   