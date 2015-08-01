import tweepy

consumer_key = "NCrukgPm4iLNljTvQcCI2MQt9"
consumer_secret = "OkMA7kldr9Te3KOoLZ8vDZLWjUqSUMaOCpgjvWo7JoomeeWbJw"
access_token = "3398529563-GAWe8AI25YThzdE3PwusmuQPF3a15WBg1KYQT8F"
access_token_secret = "TzUMDRrtU2tz3pXtRLNoVr9XLtPCJK9I5r7h0gyajNmfg"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

