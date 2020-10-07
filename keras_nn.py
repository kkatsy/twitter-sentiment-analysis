import os, pickle, random
import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def get_from_file():
    # aggregate all classified tweets into single list
    classified = []
    call_num = 1
    while os.path.isfile('filtered_' + str(call_num) + '.pickle'):
        with open('filtered_' + str(call_num) + '.pickle', 'rb') as f:
            tweet_batch = pickle.load(f)
        classified.extend(tweet_batch)
        call_num += 1
    return classified


def get_equal_class(classified):
    # sort tweets into pos and neg
    # get df with equal sized classes
    pos_tweets = []
    neg_tweets = []
    for tweet in classified:
        if tweet['man_sent'] == 'positive':
            pos_tweets.append((tweet['word_list'], tweet['man_sent']))
        if tweet['man_sent'] == 'negative':
            neg_tweets.append((tweet['word_list'], tweet['man_sent']))

    max_num = min(len(pos_tweets), len(neg_tweets))
    equal_class = random.sample(pos_tweets, max_num) + random.sample(neg_tweets, max_num)
    random.shuffle(equal_class)
    df = DataFrame(equal_class, columns=['tokens', 'sentiment'])
    return df


#######################################################################################################################

tweets = get_from_file()
tweets_df = get_equal_class(tweets)
