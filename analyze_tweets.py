import os
import pickle
import re
import time
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

# file containing unprocessed tweets
TWEETS_FILENAME = 'processed_tweets.pickle'

with open(TWEETS_FILENAME, 'rb') as f:
    friend_graph = pickle.load(f)