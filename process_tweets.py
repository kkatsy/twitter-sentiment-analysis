import os
import pickle
import langid
import re

# aggregate all preprocessed tweets into single list
tweet_list = []
if os.path.isfile('processed_tweets.pickle'):
    with open('processed_tweets.pickle', 'rb') as f:
        tweet_list = pickle.load(f)

length_b = len(tweet_list)

# remove leftover special chars and links
for tweet in tweet_list:
    tweet['text'] = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet['text'], flags=re.MULTILINE)
    special_free = [word for word in tweet['word_list'] if word.isalnum()]
    tweet['word_list'] = special_free

# remove non-english and duplicates
duplicate_check = []
clean_list = []
for tweet in tweet_list:
    guess = (langid.classify(' '.join(tweet['word_list'])))[0]
    if (tweet['lang'] == 'en') or (guess == 'en'):
        if tweet['text'] not in duplicate_check:
            clean_list.append(tweet)
            duplicate_check.append(tweet['text'])

tweet_list = clean_list

length_a = len(tweet_list)
print('tweets removed: ' + str(length_b - length_a))

# get stopwords
with open('stopwords.pickle', 'rb') as f:
    stop_words = pickle.load(f)

# filter stopwords
for tweet in tweet_list:
    filtered = []
    for word in tweet['word_list']:
        if word not in stop_words:
            filtered.append(word)
    tweet['filtered'] = filtered

# manually classify tweets
classified_num = 0
sentiment_batch = []
for tweet in tweet_list:
    print(tweet['text'])
    sentiment = input("get sentiment: ")

    if sentiment == 'p':
        tweet['man_sent'] = 'positive'
    elif sentiment == 'n':
        tweet['man_sent'] = 'negative'
    else:
        tweet['man_sent'] = 'neutral'
    classified_num += 1
    print('classified ' + str(classified_num) + ' out of ' + str(len(tweet_list)) + ' tweets')
    sentiment_batch.append(tweet)

    if (classified_num % 100 == 0) or (classified_num == len(tweet_list)):
        with open('filtered_' + str(int(classified_num/100)) + '.pickle', 'wb') as file:
            pickle.dump(sentiment_batch, file)
        sentiment_batch = []

# aggregate all classified tweets into single list
classified = []
call_num = 1
while os.path.isfile('filtered_' + str(call_num) + '.pickle'):
    with open('filtered_' + str(call_num) + '.pickle', 'rb') as f:
        tweet_batch = pickle.load(f)
    classified.extend(tweet_batch)
    call_num += 1

# create file and store pulled tweets
with open('filtered.pickle', 'wb') as f:
    pickle.dump(classified, f)

#######################################################################################################################
