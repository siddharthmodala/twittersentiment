import pickle
import pandas as pd
import numpy as np
from random import shuffle
import twokenize as tk
import expand_slang as es
import emoticons as emo
import json
from Learning import  tweet_tokenize, char_reduction
from itertools import groupby
from operator import itemgetter
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier 
from sklearn.feature_extraction.text import TfidfVectorizer

theta_s = pd.read_pickle('theta_s.pickle')

tweets_dummy = [{'token':['happy','sad'],'json':{},'type':"",'location':""},
                {'token':['together',':)'],'json':{},'type':"",'location':""},
                {'token':['alone',':)'],'json':{},'type':"",'location':""}]
td = ["happy sad","sad :(", "alone :)","alone :(", "wassup guys"]

def predict(tweets):
    for tweet in tweets:
        senti = pd.DataFrame()
        for word in tweet['token']:
            if word in theta_s.index:
                senti[word] = theta_s.loc[word]
        
        if not senti.empty:
            tweet['type'] = senti.sum(1).idxmax();
        else:
            tweet['type'] = 'happy'
    return tweets


clf = GaussianNB()
with open('trained_20.pickle', 'rb') as handle:
    clf=pickle.load(handle)

with open('word_list.pickle', 'rb') as handle:
    word_list=pickle.load( handle)

def extract_features(document):
    #document_words = set(document)
    #print document_words
    features = []
    for word in word_list:
        features.append(word in document)
    return features

def predict1(tweets):
    for tweet in tweets:
        f = extract_features(tweet['token'])
        #print len(f)
        tweet['type'] = clf.predict(f)[0]
    return tweets


sgd = SGDClassifier()
with open("sgd.pickle",'rb') as sgdfile:
    sgd= pickle.load(sgdfile)
    
tfv = TfidfVectorizer()
with open("tfv.pickle",'rb') as tfvfile:
    tfv= pickle.load(tfvfile)    
    
def predict2(tweets):
    return sgd.predict(tfv.transform(tweets))

#print predict2(td)

#for tweet in tweets_dummy:
#    print tweet['token'], tweet['type']