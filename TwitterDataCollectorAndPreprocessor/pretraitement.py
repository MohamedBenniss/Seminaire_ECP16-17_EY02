
## API Twitter Collector + Retweet and basic Pubicity Filter

from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import codecs
from pprint import pprint
import re
import time

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")

cpt = 0
query = "culture"

#==============================================================================
    
# Subjective Tweets Filter

sentimentDicosPath = "AFINN.json"
with open(sentimentDicosPath, "r", encoding='utf-8-sig') as file:
    jsonData = file.read()

sentimentDicos = json.loads(jsonData)

with open("tweets_" + query + ".json", "r", encoding='utf-8-sig') as rFile:
    jsonTweets=rFile.read()

tweets=json.loads(jsonTweets)

subjectiveTweets=[]

for tweet in tweets:
    subjective=False
    tweetText = re.findall(r"[\w]+", tweet["text"])
    for sentiment in sentimentDicos:
        for word in tweetText:
            if re.search(r"^" + sentiment + r"s?$", word, re.IGNORECASE):
                subjective = True
                subjectiveTweets = subjectiveTweets + [tweet]
                print(sentiment)
                break
        if subjective==True:
            break
        
with open("subjTweets_" + query + ".json", "w") as wFile2:
    json.dump(subjectiveTweets, wFile2)