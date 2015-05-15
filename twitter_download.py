import tweepy
#import prediction
#import parse
import json


apikey =  'ICfEPad1r5DjI2JSAMshOGrpY'
apisecret = 'OszGyz2S4E0Vx7EY0x2PWKgj9RN7h581nFwG8zPD75dIQSRXLK'
accesstoken = '72574437-10MG5U0zNIdttVy0Dy2BJHOGEMGd318yrKQfEXtbW'
accessSecret = 'aly5ZsK9mtG4ImxAISvdtCKROKzmW2oNsTrIKH5ZuupGi'

def get_tweets(query,count=10,language='en'):
    auth = tweepy.OAuthHandler(apikey,apisecret)
    auth.set_access_token(accesstoken,accessSecret);
    api = tweepy.API(auth)
    api.search
    tweets =[]
    
    for status in tweepy.Cursor(api.search,q=query,lang=language).items(1000):
        if not u'RT' in status._json['text']:
            tweets.append(status._json);
            count -=1
            if count == 0:
                break
    return tweets


#tweets = get_tweets('CHIvsMIN')

#print len(tweets)

#tweets = parse.parse_tweets(tweets);

#tweets = prediction.predict(tweets)

#print type(tweets)