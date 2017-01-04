# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

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

consumer_key = "xKL89AbnklOEP4W57m5tKAcX6"
consumer_secret = "9CANhecFVkGYDYf3t4nqN5rY2RGN4ZJK0jFPNVblx6v7XTZj8s"
access_token = "801345509252272128-sJJTtLTBTYlYVWjiF2TKb2a5GfA2LYH"
access_token_secret = "U6VvYEPXVFLakbh2Mf1Y1WCEshLSNoGyx13wWS2MquiCG"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#==============================================================================
 
 for tweet in public_tweets:
     print("--------------------------------------")
     print(tweet.text)
 
 user=api.get_user("twitter")
 
 print(user.screen_name)
 print(user.followers_count)
 
 for friend in user.friends():
     print(friend.screen_name)
 
 for friend in tweepy.Cursor(api.friends).items():
     # Process the friend here
     print(friend.screen_name)
 
 page = 1
 while True:
     statuses = api.user_timeline(page=page)
     if statuses:
         for status in statuses:
             # process status here
             print("--------------------------------------")
             print(status.text)
     else:
         # All done
         break
     page += 1  # next page
     
 for status in tweepy.Cursor(api.user_timeline).items():
     # process status here
     print("--------------------------------------")
     print(status.text)
     print("--------------------------------------")
     print(dir(status))
#==============================================================================
    
for status in tweepy.Cursor(api.user_timeline, id="realDonaldTrump").items(30):
    print("--------------------------------------")
    print(status.text)

for status in tweepy.Cursor(api.user_timeline, id="realDonaldTrump").items(30):
    print("--------------------------------------")
    print(status.text)
    

#==============================================================================

# API Twitter Collector + Retweet and basic Pubicity Filter
#
#cpt = 0
#jsonDicos=[]
#query = "culture"
#
#with open("tweets_" + query + ".json", "w") as wFile:
#    c=tweepy.Cursor(api.search, q=query, lang="fr").items(10000)
#    for i in range(10000):
#        try:
#            status= c.next()
#            cpt+=1
#            if('RT @' not in status.text and 'https://' not in status.text):
##                print("--------------------------------------")
##                print(status.created_at)
##                print(status.text)
#                jsonDicos = jsonDicos + [status._json]
#        except tweepy.TweepError:
#            print("Sleeping ! " + str(i))
#            time.sleep(60*15)
#            continue
#        except StopIteration:
#            print("i = " + str(i))
#            break
#    json.dump(jsonDicos, wFile)

#==============================================================================
    
# Subjective Tweets Filter

#sentimentDicosPath = "AFINN.json"
#with open(sentimentDicosPath, "r", encoding='utf-8-sig') as file:
#    jsonData = file.read()
#
#sentimentDicos = json.loads(jsonData)
#
#with open("tweets_" + query + ".json", "r", encoding='utf-8-sig') as rFile:
#    jsonTweets=rFile.read()
#
#tweets=json.loads(jsonTweets)
#
#subjectiveTweets=[]
#
#for tweet in tweets:
#    subjective=False
#    tweetText = re.findall(r"[\w]+", tweet["text"])
#    for sentiment in sentimentDicos:
#        for word in tweetText:
#            if re.search(r"^" + sentiment + r"s?$", word, re.IGNORECASE):
#                subjective = True
#                subjectiveTweets = subjectiveTweets + [tweet]
#                print(sentiment)
#                break
#        if subjective==True:
#            break
#        
#with open("subjTweets_" + query + ".json", "w") as wFile2:
#    json.dump(subjectiveTweets, wFile2)