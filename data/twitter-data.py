import tweepy

consumer_key = "NCrukgPm4iLNljTvQcCI2MQt9"
consumer_secret = "OkMA7kldr9Te3KOoLZ8vDZLWjUqSUMaOCpgjvWo7JoomeeWbJw"
access_token = "3398529563-5Si4sjrY7ADW6KYxQEvjWy7baWM5iuGNAlJEY2F"
access_token_secret = "crdN41t7KSr4I9nZyGjT7mrO2bAzDPc8ixIw8XDxYK01c"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class TwitterUser(object):
	def __init__(self, username, count, is_follower=False):
		self.rawUser = api.get_user(username)
		self.rawTimeline = [Tweet(tweet) for tweet in api.user_timeline(username, count=count)]
		self.count = count

		self.description = self.rawUser.description
		self.profile_image_url = self.rawUser.profile_image_url
		self.location = self.rawUser.location
		self.name = self.rawUser.name
		self.id = self.rawUser.id
		self.lang = self.rawUser.lang
		self.url = self.rawUser.url
		self.friends_ids = api.friends_ids(username)
		# self.friends_list = (self._get_friends(self.friends_ids)
		#					 if not is_follower else None)

	def _get_friends(self, friends_ids, count=10):
		return [TwitterUser(friend_id, , True) for friend_id in friends_ids]


class Tweet(object):
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
