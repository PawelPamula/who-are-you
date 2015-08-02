import tweepy
import time
from sklearn.feature_extraction.text import TfidfVectorizer
import operator
import io
import random
import numpy as np
from numpy import arange
import nltk
from nltk import word_tokenize

consumer_key = "8mKBl6nwbtS6x1TSx4dTtDkII"
consumer_secret = "3QaNrMQuo4iCAmreULcozhHKIq3tNZm4ODRYLguuTkibgCViMx"
access_token = "3400051325-NhjNdftHlObWJgWoQznebzsZq1FY3grCgbTqaxQ"
access_token_secret = "HNtzxvxo99m8EVrbUegMRi2pDs3pILWUw576enLgJRLoM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class TwitterUser(object):
    """
    This class takes as an input the username of the Twitter user,
    the number of tweets to fetch and a variable to check if the account being
    accessed is the base user or not. The "is_follower" boolean variable is a
    work-around to prevent infinite recursion when the friends_list methos is called.
    """
    def __init__(self, username, count, is_follower=False):
            self.raw_user = api.get_user(username)
            self.tweets = [Tweet(tweet) for tweet in api.user_timeline(username, count=count)]
            self.count = count

            self.description = self.raw_user.description
            self.profile_image_url = self.raw_user.profile_image_url
            self.location = self.raw_user.location
            self.name = self.raw_user.name
            self.id = self.raw_user.id
            self.lang = self.raw_user.lang
            self.url = self.raw_user.url
            self.friends_ids = api.friends_ids(username)
            # self.friends_list = (self._get_friends(self.friends_ids)
            # 					 if not is_follower else None)

    def _get_friends(self, friends_ids, count=1):
        return [TwitterUser(friend_id, count, True) for friend_id in friends_ids]


class Tweet(object):
    """This class contains the attributes for a tweet object.
    This includes the text itself, an id, the location where the tweet was posted and time.
    Also, there are methods for retrieving the hashtags and users mentioned in the tweet
    """
    def __init__(self, tweet):
            self.text = tweet.text
            self.id = tweet.id
            self.geo = tweet.geo
            self.created_at = tweet.created_at

            self.hashtags = self._parse_tweet(self.text, char='#')
            self.referrals = self._parse_tweet(self.text, char='@')

    def _parse_tweet(self, text, char='#'):
        return map(lambda word: word.replace(char, ''),
                filter(lambda word: word.startswith(char),
                    text.split(' ')))

def tweets2tags(text, hasht):
    tx=[]
    for line in text:
        tokens=word_tokenize(line)
        tags=nltk.pos_tag(tokens)
        text= [s[0] for s in tags if s[1].startswith('NN')]
        tx.extend(text)
    vectorizer = TfidfVectorizer(stop_words="english",min_df=1)
    X = vectorizer.fit_transform(tx)
    idf = vectorizer.idf_
    size=len(idf)
    idf[:size/5]=2
    idf[size/5:2*size/5]=3
    idf[2*size/5:3*size/5]=4
    idf[3*size/5:4*size/5]=5
    idf[4*size/5:]=7
    tags =  dict(zip(vectorizer.get_feature_names(), idf))
    for i in hasht:
        tags[i] = 6
    return tags
