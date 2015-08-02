import tweepy
import time

consumer_key = "bBuhDHozTBgDfl51Zo28mSsdV"
consumer_secret = "Pk1zZg5XT3MqnNHUecuQZffBgfBuRnqeXbEAOrMY3TCyH7V9m9"
access_token = "3398529563-5Si4sjrY7ADW6KYxQEvjWy7baWM5iuGNAlJEY2F"
access_token_secret = "crdN41t7KSr4I9nZyGjT7mrO2bAzDPc8ixIw8XDxYK01c"
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

	def dump_tweets_to_file(self):
		with open('tmp.txt', 'w') as f:
			for tweet in self.tweets:
				f.write(tweet.text.encode('utf-8').strip())
				f.write('\n')


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
