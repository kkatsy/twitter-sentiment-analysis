import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
import pickle
import os
import random

# aggregate all classified tweets into single list
classified = []
call_num = 1
while os.path.isfile('filtered_' + str(call_num) + '.pickle'):
    with open('filtered_' + str(call_num) + '.pickle', 'rb') as f:
        tweet_batch = pickle.load(f)
    classified.extend(tweet_batch)
    call_num += 1

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


# nltk + naive bayes

# np + keras + nn
