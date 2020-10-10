import os
import pickle
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


def get_tweets():
    # aggregate all classified tweets into single list
    if os.path.isfile('filtered.pickle'):
        with open('filtered.pickle', 'rb') as f:
            classified = pickle.load(f)

    return classified


def get_tokens(classified):
    # sort tweets using man_sent and get token categories
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

    # print sentiment percentage data
    print(str(total_tweets) + ' total tweets classified:')
    print('positive -> ' + str(num_pos) + ' (' + str("{:.2f}".format((num_pos / total_tweets) * 100)) + ' %)')
    print('negative -> ' + str(num_neg) + ' (' + str("{:.2f}".format((num_neg / total_tweets) * 100)) + ' %)')
    print('neutral -> ' + str(num_neu) + ' (' + str("{:.2f}".format((num_neu / total_tweets) * 100)) + ' %)')

    return all_tokens, pos_tokens, neg_tokens


def freq_dist(all_tokens, pos_tokens, neg_tokens, num_common):
    # get frequency distributions
    tot_fdist = nltk.FreqDist(all_tokens)
    pos_fdist = nltk.FreqDist(pos_tokens)
    neg_fdist = nltk.FreqDist(neg_tokens)

    # print most common words
    tot_common = tot_fdist.most_common(num_common)
    pos_common = pos_fdist.most_common(num_common)
    neg_common = neg_fdist.most_common(num_common)

    return tot_common, pos_common, neg_common


def common_colloc(all_tokens, pos_tokens, neg_tokens, num_common):
    # get all bigrams
    all_bigram = BigramCollocationFinder.from_words(all_tokens)
    pos_bigram = BigramCollocationFinder.from_words(pos_tokens)
    neg_bigram = BigramCollocationFinder.from_words(neg_tokens)

    # get most common bigrams
    all_colloc = all_bigram.nbest(BigramAssocMeasures.likelihood_ratio, num_common)
    pos_colloc = pos_bigram.nbest(BigramAssocMeasures.likelihood_ratio, num_common)
    neg_colloc = neg_bigram.nbest(BigramAssocMeasures.likelihood_ratio, num_common)

    return all_colloc, pos_colloc, neg_colloc


########################################################################################################################

tweets = get_tweets()

all_tokens, pos_tokens, neg_tokens = get_tokens(tweets)

num_top_words = 20
tot_words, pos_words, neg_words = freq_dist(all_tokens, pos_tokens, neg_tokens, num_top_words)
print('Most common words overall: ', tot_words)
print('Most common positive words: ', pos_words)
print('Most common negative words: ', neg_words)

num_top_bigrams = 15
tot_coll, pos_coll, neg_coll = common_colloc(all_tokens, pos_tokens, neg_tokens, num_top_bigrams)
print('Most common collocations overall: ', tot_coll)
print('Most common positive collocations: ', pos_coll)
print('Most common negative collocations: ', neg_coll)