import json
import re
import matplotlib.pyplot as plt
import twokenize as tk
import emoticons as emo
import expand_slang as es
from itertools import groupby
from operator import itemgetter
import pandas as pd
import collections
from collections import defaultdict
import pickle

#reduce more than 2 repetition to 2
def char_reduction(token):
    result = []
    for k,v in groupby(enumerate(token),key=itemgetter(1)):
        result.append(next(v))
       
    result_string = ''
    previous_index = 0
    for current_index,v in result:
        diff_index = current_index - previous_index
        if diff_index > 2:
	    result_string +=(token[previous_index]*2)
        else:
            result_string += (token[previous_index]*(diff_index))
        previous_index = current_index
    
    
    #for last value
    diff_index= len(token)- previous_index
    if diff_index > 2:
        result_string += token[previous_index]*2
    else:
        result_string += token[previous_index]*diff_index
    
    return result_string   


def parse_tweets(tweets):
    parsed_tweets =[]
    for tweet_json in tweets:
	try:
	    #tweet_json = json.loads(tweet_str);
	    tweet_text = tweet_json['text'];
	    if u'RT' in tweet_text:	
		tweet_text = tweet_text[0:tweet_text.index(u'RT') -1]
		
	    tweet_token = tk.tokenize(tweet_text)
	    tweet_token =[char_reduction(tok) for tok in tweet_token]
	    tweet_token = [t for tok in tweet_token for t in es.expand(tok) if (not (('@' in t) or (tk.Url_RE.search(t)) or (not emo.Emoticon_RE.search(t) and tk.Punct_re.search(t))))]
	    
	    if tweet_token != []:
		tweet_obj = {"token":tweet_token,"location" : tweet_json['place']['country'] if tweet_json['place'] != None else None,"json":tweet_json,"type" :""}
		parsed_tweets.append(tweet_obj)
	except Exception as e:
	    print e
	    
    return parsed_tweets
'''
f = open('token_list2.txt', 'w')
for val in token_list:
    write_json = json.dumps(val)
    f.write(write_json + '\n')    
'''

'''    
#print statistics
df = pd.DataFrame()

df['text'] = text #map(lambda tweet: tweet['text'], twitter_data)
df['lang'] = lang #map(lambda tweet: tweet['lang'], twitter_data)
df['country']  = country #map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, twitter_data)
df['type'] = types_count
tweets_by_lang = df['lang'].value_counts()
tweets_by_type = df['type'].value_counts()
fig,(ax,bx) = plt.subplots(1,2)

ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
ax.set_xlabel('languages',fontsize=15)
ax.set_ylabel('counts',fontsize=15)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)

bx.set_title('Types', fontsize=15, fontweight='bold')
bx.set_xlabel('Type',fontsize=15)
bx.set_ylabel('counts',fontsize=15)
bx.tick_params(axis='x', labelsize=15)
bx.tick_params(axis='y', labelsize=10)


tweets_by_lang[:5].plot(ax=ax,kind='bar',color='red')
tweets_by_type.plot(ax=bx,kind='bar',color='blue')

plt.show()
'''
#print "total number of tweets  = " + str(len(token_list))



        
        


