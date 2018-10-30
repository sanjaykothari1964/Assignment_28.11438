# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:19:07 2018

@author: Zakir
"""

from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stopwords.words('english')

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)

#convert that text into tokens by splitting 
tokens = [t for t in text.split()]
#tokens = word_tokenize(text)
clean_tokens = tokens[:] 
sr = stopwords.words('english') 
for token in tokens: 
    if token in stopwords.words('english'): 
        clean_tokens.remove(token) 

#calculate the frequency of those tokens using Python NLTK.
freq = nltk.FreqDist(tokens) 
for key,val in freq.items(): 
    print (str(key) + ' : ' + str(val))
    
#PHP is the highest frequency word- (55 times)
