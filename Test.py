import json
import numpy as np
from random import shuffle
import pickle
from sklearn.naive_bayes import GaussianNB



happy = [':-)',':)',':D',':o)',':]',':3',':c)',':>','=]','8)','=)',':}',
         ':^)',':?)',':-D','8-D','8D','x-D','xD','X-D','XD','=-D','=D',
         '=-3','=3','B^D',':-))',":'-)",":')",';-)',';)',':-P',':P','\o/']

sad = ['>:[',':-(',':(',':-c',':c',':-<',':?C',':<',':-[',':[',':{',';(',":'-(",":'("]

angry = ['X-(','X(',':-@',':@','>:(','>:-(','-_-+',':-t','>-(','D<',':-||','b (','>:\\','>:/',':-/']

shocked = ['=O','=0','=o',':-o',':-O',':-0','>:O','8-0','O_O', 'o-o','O_o',
           'o_O','o_o','O-O','(+_+)','{:o','(:)o)','*.*','(*.*)',':-()','l8^O']


all_emo = happy + sad + angry + shocked
clf = GaussianNB()
test_set=[]
word_list=[]
def remove_test_emo(data):
   
    result_data=[]
    for d in data:
        d['token'] = [x for x in d['token'] if x not in all_emo]
        result_data.append(d)
        
    return result_data

def extract_features(document):
    #document_words = set(document)
    #print document_words
    features = []
    for word in word_list:
        features.append(word in document)
            
    return features



val=["20"]
for e in val:
    with open('newpickle/test_set_'+str(e) + '.pickle', 'rb') as handle:
        test_set=pickle.load(handle)
            
    with open('newpickle/trained_'+str(e) + '.pickle', 'rb') as handle:
        clf=pickle.load(handle)
    
    with open('newpickle/word_list.pickle', 'rb') as handle:
        word_list=pickle.load( handle)
    
   
    print len(word_list)
    
    print len(test_set)
    print test_set[0]
    
    
    
    test_set = remove_test_emo(test_set)
    print "no emo " + str(test_set[0])
    test_data=[]
    sentiment = []
    start = 0
    result = 0
    counter = 0
    tp=0.0
    tn=0.0
    fp=0.0
    fn=0.0
    final_sentiment=[]
    final_result = []
    
    while start < len(test_set):
        limit = start+500
        if (start + 500) > len(test_set):
            limit = len(test_set)
        for t in test_set[start:limit]:
            f = extract_features(t['token'])
            test_data.append(f)
            sentiment.append(t['type'])
            final_sentiment.append(t['type'])
        
        result= clf.predict(test_data)
        final_result.extend([x for x in result])
        for i,senti in enumerate(sentiment):
            if senti =='happy' and result[i]==senti:
                tp+=1
            elif senti =='happy' and result[i]!=senti:
                fn+=1
            elif senti =='sad' and result[i]==senti:
                tn+=1
            elif senti =='sad' and result[i]!=senti:
                fp+=1
                
        
        start=limit
        test_data=[]
        sentiment = []
        counter +=1
        result =[]
        print start
    with open('newpickle/actual_value_'+ e + '.pickle', 'wb') as handle:
      pickle.dump(final_sentiment, handle)  
    with open('newpickle/pred_value_'+ e + '.pickle', 'wb') as handle:
      pickle.dump(final_result, handle)   
    print e
    print "\n For Happy"
    print 'accuracy is : ' + str((tn+tp)/(tn+tp+fn+fp))
    print 'precision is :' + str(tp/(tp+fp))
    print 'recall is : ' + str(tp/(tp+fn))
    print "\n For Sad"
    print 'accuracy is : ' + str((tn+tp)/(tn+tp+fn+fp))
    print 'precision is :' + str(tn/(tn+fn))
    print 'recall is : ' + str(tn/(tn+fp))