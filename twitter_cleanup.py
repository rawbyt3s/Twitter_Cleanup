#!/usr/bin/env python
import tweepy
from datetime import datetime, timedelta

#Auth Stuff
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# options
test_mode = False
verbose = False
delete_tweets = True
delete_favs = True
days_to_keep = 7
tweets_to_save = [

]
favs_to_save = [

]

#API test
#
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)


# set cutoff date, use utc to match twitter
cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)
 
# delete old tweets
if delete_tweets:
    # get all timeline tweets
    print ("Retrieving timeline tweets")
    timeline = tweepy.Cursor(api.user_timeline).items()
    deletion_count = 0
    ignored_count = 0
 
    for tweet in timeline:
        # where tweets are not in save list and older than cutoff date
        if tweet.id not in tweets_to_save and tweet.created_at < cutoff_date:
            if verbose:
                print (f"Deleting {tweet.id}: [{tweet.created_at}] {tweet.text}")
            if not test_mode:
                api.destroy_status(tweet.id)
             
            deletion_count += 1
        else:
            ignored_count += 1
 
    print (f"Deleted {deletion_count} tweets, ignored {ignored_count}")
else:
    print ("Not deleting tweets")
     
# unfavor old favorites
if delete_favs:
    # get all favorites
    print ("Retrieving favorite tweets")
    favorites = tweepy.Cursor(api.favorites).items()
    unfav_count = 0
    kept_count = 0
 
    for tweet in favorites:
        # where tweets are not in save list and older than cutoff date
        if tweet.id not in favs_to_save and tweet.created_at < cutoff_date:
            if verbose:
                print (f"Unfavoring {tweet.id}: [{tweet.created_at}] {tweet.text}")
            if not test_mode:
                api.destroy_favorite(tweet.id)
             
            unfav_count += 1
        else:
            kept_count += 1
 
    print (f"Unfavored {unfav_count} tweets, ignored {kept_count}")
else:
    print ("Not unfavoring tweets")