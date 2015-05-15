import pickle
import twokenize as tk
import expand_slang as es
import emoticons as emo
from itertools import groupby
from operator import itemgetter
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier 


# In[34]:

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


# In[35]:

def tweet_tokenize(tweet_text):
    tweet_token = tk.tokenize(tweet_text)
    tweet_token =[char_reduction(tok) for tok in tweet_token]
    tweet_token = [t for tok in tweet_token for t in es.expand(tok) if (not (('@' in t) or (tk.Url_RE.search(t)) or (not emo.Emoticon_RE.search(t) and tk.Punct_re.search(t))))]    
    return tweet_token

tfv = TfidfVectorizer(tokenizer=tweet_tokenize,use_idf=True)
clf = SGDClassifier(alpha= 0.000001,n_iter= 50,penalty= 'elasticnet')
clfpickle = "sgd.pickle"
tfvpickle = "tfv_sgd.pickle"
# In[19]:

def newfit():
    with open('tfidfMat.pickle','rb') as tfvfile:
        tfidfMat = pickle.load(tfvfile)
    
    with open(tfvpickle,'rb') as tfvfile:
        tfv = pickle.load(tfvfile)    
    

def fit():
    files = {'happy' :'data/tweets_happy.txt','sad' :'data/tweets_sad.txt'}
    data = []
    target = []
    location = []
    ids=[]
    lang=[]
    for key,loc in files.iteritems():
        json_file = open(loc)
        json_str = json_file.readlines()
        for s in json_str:
            try:
                tweet = json.loads(s)
                data.append(tweet['text'])
                ids.append(tweet['id'])
                lang.append(tweet['lang'])
                location.append(tweet['place']['country'] if tweet['place'] != None else None)
                target.append(key)
            except Exception as ex:
                print ex.message
    
    datadict = {}
    datadict['data'] = data
    datadict['target'] = target
    datadict['location'] = location
    datadict['lang'] = lang
    datadict['ids'] = ids
    
    print 'data loaded'
    
    # In[150]:

    tfidfMat = tfv.fit_transform(datadict["data"])
    print 'tfidf vector created'
    with open('tfidfMat.pickle','wb') as tfvfile:
        pickle.dump(tfidfMat,tfvfile)
    
    with open(tfvpickle,'wb') as tfvfile:
        pickle.dump(tfv,tfvfile)
    
    clf.fit(tfidfMat,datadict['target'])
    
    print 'classifier built'
    
    with open(clfpickle,'wb') as tfvfile:
        pickle.dump(clf,tfvfile)

def test():
    testX = testX + datadict['data'][45000:45010]
    testY = testY + datadict['target'][45000:45010]
    
    print clf.predict(tfv.transform(testX))


# In[141]:



