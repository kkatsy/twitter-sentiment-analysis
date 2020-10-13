from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import nltk
import pickle, os, random


def get_from_file():
    # aggregate all classified tweets into single list
    classified = []
    if os.path.isfile('filtered.pickle'):
        with open('filtered.pickle', 'rb') as f:
            classified = pickle.load(f)

    return classified


def get_equal_class(classified):
    # sort tweets into pos and neg
    pos_tweets, neg_tweets = [], []
    for tweet in classified:
        if tweet['man_sent'] == 'positive':
            pos_tweets.append((tweet['word_list'], tweet['man_sent']))
        if tweet['man_sent'] == 'negative':
            neg_tweets.append((tweet['word_list'], tweet['man_sent']))

    # get list with equal sized classes
    max_num = min(len(pos_tweets), len(neg_tweets))
    equal_class = random.sample(pos_tweets, max_num) + random.sample(neg_tweets, max_num)
    random.shuffle(equal_class)

    return equal_class


def get_train_test(equal_class, test_size, num_bigrams):
    # split equal classes into test and train data
    train = equal_class[:int(len(equal_class) * (1 - test_size))]
    test = [tweet for tweet in equal_class if tweet not in train]

    # get word + bigram features for train set
    word_features, bigram_features = get_tweet_features(train, num_bigrams)

    # get bag of words feature vector for train set
    train_set = []
    for a_tweet in train:
        features = extract_features(a_tweet[0], word_features, bigram_features)
        train_set.append((features, a_tweet[1]))

    # get bag of words feature vector for test set
    test_set = []
    for a_tweet in test:
        features = extract_features(a_tweet[0], word_features, bigram_features)
        test_set.append((features, a_tweet[1]))

    return train_set, test_set


def get_tweet_features(train, num_bigrams):
    # get all word features in train set
    all_words = []
    for tweet in train:
        all_words.extend(tweet[0])
    word_list = nltk.FreqDist(all_words)
    word_features = word_list.keys()

    # get specified num of bigram features in train set
    bigram = BigramCollocationFinder.from_words(all_words)
    bigram_features = bigram.nbest(BigramAssocMeasures.likelihood_ratio, num_bigrams)

    return word_features, bigram_features


def extract_features(text, word_features, bigram_features):
    # get BoW word vec
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in text)

    # get BoW bigram vec
    joined = ' '.join(text)
    for colloc in bigram_features:
        colloc = ' '.join(colloc)
        features['contains(%s)' % colloc] = (colloc in joined)

    return features


def run_naive_bayes(train, test):
    # create naive bayes classifier
    classifier = nltk.NaiveBayesClassifier.train(train)

    # run classifier on test set
    correct = 0
    for tweet in test:
        pred = classifier.classify(tweet[0])
        if pred == tweet[1]:
            correct += 1

    # print classification accuracy
    accuracy = correct / len(test)

    return accuracy


########################################################################################################################

tweets = get_from_file()

equal_tweets = get_equal_class(tweets)

test_size = 0.2
num_bigram_features = 10
train, test = get_train_test(equal_tweets, test_size, num_bigram_features)

accuracy = run_naive_bayes(train, test)
print("Testing Accuracy:  {:.2f}".format(accuracy * 100))
