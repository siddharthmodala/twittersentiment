import os
import json
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash , send_from_directory,jsonify
import twitter_download as td
from Learning import tweet_tokenize, char_reduction
from sklearn.linear_model import SGDClassifier 
from sklearn.feature_extraction.text import TfidfVectorizer
import parse
import prediction


#configuration
STATIC_FOLDER = os.curdir + '/static/html'
#DEBUG=True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD  = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def index():
	return send_from_directory ( app.config["STATIC_FOLDER"],"index.html");

@app.route("/getResults",methods=['POST'])
def getResults():
	if request.method == 'POST':
		q = json.loads(request.data.decode());
		result = {}
		try:
			print q['query'],q['lang']
			tweets = td.get_tweets(q['query'],50,q['lang'])
			tweet_text = []
			for tweet in tweets:
				tweet_text.append(tweet["text"])
			tweets = parse.parse_tweets(tweets)
			if(len(tweets) != 0):
				output = prediction.predict2(tweet_text)
				i=0;
				for o in output:
					tweets[i]["type"] = o
					i+=1
				#tweets = prediction.predict1(tweets)
				result = {'result':tweets}
			else:
				result={'error':'Could not download enough number of tweets for the search tag'}
			
		except Exception as ex:
			result = {'error':'Error processing the data'}
			if(app.config['DEBUG']):
				result['message'] = ex.message
		
		return jsonify(result);


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5001)
