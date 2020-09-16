import os
import pickle
import re
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import OAuthHandler
from textblob import TextBlob

# max num tweet queries per 15 minutes
LIMIT = 300
# file containing unprocessed tweets
TWEETS_FILENAME = 'raw_tweets.pickle'


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

    def get_tweets(self, query, count):
        # figure out how many times need to call api to fetch
        raw_tweets = []
        try:
            while count > 0:
                if count >= LIMIT:
                    # if still need more than limit, get limit
                    single_call = self.api.search(q=query, count=LIMIT)
                else:
                    # if need less the limit, get what is left
                    single_call = self.api.search(q=query, count=count)

                count -= LIMIT
                raw_tweets.append(single_call)

                # can get 300 tweets every 15 mins
                if count > 0:
                    time.sleep(15.5 * 60)

            return raw_tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

    def get_sentiment(self, tweet):

        blob = TextBlob(tweet)
        polarity = blob.sentiment.polarity

        # get sentiment
        if polarity > 0:
            sentiment = 'positive'
        elif polarity == 0:
            sentiment = 'neutral'
        else:
            sentiment = 'negative'

        return sentiment, polarity

    def preprocess(self, tweet):

        parsed_tweet = {}

        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        # parse tweet
        parsed_tweet['word_list'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+) ", " ", tweet).split()
        # saving sentiment of tweet
        parsed_tweet['sentiment'], parsed_tweet['polarity'] = self.get_sentiment(''.join(parsed_tweet['word_dict']))

        return tweet


# creating object of Twitter Class
api = Twitter()

# if file exists and has preexisting data
raw_tweets = []
if os.path.isfile(TWEETS_FILENAME):
    with open(TWEETS_FILENAME, 'rb') as f:
        raw_tweets = pickle.load(f)
else:
    # calling function to get tweets
    raw_tweets = api.get_tweets(query='vaccine', count=1500)

    with open(TWEETS_FILENAME, 'wb') as f:
        pickle.dump(raw_tweets, f)

processed = []
for tweet in raw_tweets:
    processed.append(api.preprocess(tweet))

with open('clean_tweets.pickle', 'wb') as f:
    pickle.dump(processed, f)