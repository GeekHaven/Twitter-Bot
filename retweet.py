from credentials import *
import tweepy
from time import sleep

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Add usernames of all accounts that need to be retweeted/favourted/followed here
account_list = ['sitepointdotcom','ConsenSys','gsoc','WSJ','observer','mashable','TechCrunch','WIRED','outreachy','WomenWhoCode','Topcoder','github','TheNextWeb','tech2eets','verge','DigitalTrends','arstechnica','npmjs','mozilla']

while True:
    for target in account_list:
        print("Getting data for " + target)
        item = api.get_user(target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        if not item.following:
            item.follow()
            print('Followed the user')

        tweets = api.user_timeline( id=target, count = 1)
        for tweet in tweets:
            try:
                tweet.retweet()
                print('Retweeted the tweet')

                tweet.favorite()
                print('Favorited the tweet')
                sleep(7200) #after every 2 hours

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break