import os
import pickle
import nltk

# aggregate all classified tweets into single list
classified = []
call_num = 1
while os.path.isfile('filtered_' + str(call_num) + '.pickle'):
    with open('filtered_' + str(call_num) + '.pickle', 'rb') as f:
        tweet_batch = pickle.load(f)
    classified.extend(tweet_batch)
    call_num += 1

# get info + tokens for each type of tweet, using man_sent
total_tweets = len(classified)
num_pos, num_neg, num_neu = 0, 0, 0
pos_tokens, neg_tokens, neu_tokens = [], [], []
all_tokens = []
for tweet in classified:
    if tweet['man_sent'] == 'positive':
        num_pos += 1
        for word in tweet['filtered']:
            if word != 'vaccine':
                pos_tokens.append(word)
                all_tokens.append(word)
    elif tweet['man_sent'] == 'negative':
        num_neg += 1
        for word in tweet['filtered']:
            if word != 'vaccine':
                neg_tokens.append(word)
                all_tokens.append(word)
    else:
        num_neu += 1
        for word in tweet['filtered']:
            if word != 'vaccine':
                neu_tokens.append(word)
                all_tokens.append(word)

print(str(total_tweets) + ' total tweets classified:')
print('positive -> ' + str(num_pos) + ' (' + str("{:.2f}".format((num_pos/total_tweets)*100)) + ' %)')
print('negative -> ' + str(num_neg) + ' (' + str("{:.2f}".format((num_neg/total_tweets)*100)) + ' %)')
print('neutral -> ' + str(num_neu) + ' (' + str("{:.2f}".format((num_neu/total_tweets)*100)) + ' %)')

# get frequency distributions
tot_fdist = nltk.FreqDist(all_tokens)
pos_fdist = nltk.FreqDist(pos_tokens)
neg_fdist = nltk.FreqDist(neg_tokens)

print( tot_fdist.most_common(20))
print(pos_fdist.most_common(20))
print( neg_fdist.most_common(20))

