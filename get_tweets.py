import os
import pickle
import re
import time
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

# max num tweet queries per 15 minutes
LIMIT = 300

# file containing unprocessed tweets
TWEETS_FILENAME = 'processed_tweets.pickle'


class Twitter(object):
    """
    Twitter class for tweet extraction and preprocessing
    """

    def __init__(self):
        # keys and tokens from the Twitter Dev Console
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)

            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)

            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):

        # remove special chars, links, and @usernames
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+) ", " ", tweet).split())

    def get_sentiment(self, tweet):

        # get sentiment index between -1 and 1
        blob = TextBlob(tweet)
        polarity = blob.sentiment.polarity

        # get sentiment
        if polarity > 0.0:
            sentiment = 'positive'
        elif polarity == 0.0:
            sentiment = 'neutral'
        else:
            sentiment = 'negative'

        return sentiment, polarity

    def get_data(self, tweet):

        # dict of tweet data
        tweet_data = {}

        # get text of tweet
        if 'RT' in tweet.full_text:
            tweet_data['text'] = tweet.retweeted_status.full_text
        else:
            tweet_data['text'] = tweet.full_text

        # get list of separated words in tweet
        tweet_data['word_list'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+) ", " ",
                                         tweet_data['text']).lower().split()
        # get language to make sure can analyze english-only
        tweet_data['lang'] = tweet.lang

        # see if can get full tweet or not

        # get sentiment of tweet
        tweet_data['sentiment'], tweet_data['polarity'] = self.get_sentiment(' '.join(tweet_data['word_list']))

        return tweet_data

    def get_tweets(self, query, count):

        # store processed tweet data dicts in list
        processed_tweets = []

        while count > 0:
            if count >= LIMIT:
                # if still need more than limit, get limit
                single_call = self.api.search(q=query, count=LIMIT, tweet_mode='extended')
            else:
                # if need less the limit, get what is left
                single_call = self.api.search(q=query, count=count)

            count -= LIMIT

            # get full text and process single tweet
            for single_tweet in single_call:
                full_tweet = self.api.get_status(single_tweet.id, tweet_mode='extended')
                processed_tweets.append(self.get_data(full_tweet))

            # can get 300 tweets every 15 mins
            if count > 0:
                time.sleep(15.2 * 60)

        return processed_tweets


# creating object of Twitter Class
api = Twitter()

# if file exists and has preexisting data
tweets = []
if os.path.isfile(TWEETS_FILENAME):
    with open(TWEETS_FILENAME, 'rb') as f:
        tweets = pickle.load(f)
else:
    # calling function to get tweets
    processed = api.get_tweets(query='vaccine', count=10)

    # create file and store pulled tweets
    with open(TWEETS_FILENAME, 'wb') as f:
        pickle.dump(processed, f)
