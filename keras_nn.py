import os, pickle, random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras import layers
from tensorflow import keras
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


def get_from_file():
    # aggregate all classified tweets into single list
    classified = []
    if os.path.isfile('filtered.pickle'):
        with open('filtered.pickle', 'rb') as f:
            classified = pickle.load(f)

    return classified


def get_equal_class(classified):
    # sort tweets into pos and neg
    pos_tweets = []
    neg_tweets = []
    for tweet in classified:
        if tweet['man_sent'] == 'positive':
            pos_tweets.append((' '.join(tweet['word_list']), tweet['man_sent']))
        if tweet['man_sent'] == 'negative':
            neg_tweets.append((' '.join(tweet['word_list']), tweet['man_sent']))

    # get list with equal sized classes
    max_num = min(len(pos_tweets), len(neg_tweets))
    equal_class = random.sample(pos_tweets, max_num) + random.sample(neg_tweets, max_num)
    random.shuffle(equal_class)

    return equal_class


def get_feature_vector(train_set, num_bigrams):
    # get string of all words in tweets
    train = (' '.join(train_set.tolist()))
    all_words = train.split(' ')

    # get all word features in train set
    word_list = nltk.FreqDist(all_words)
    word_features = list(word_list.keys())

    # get select bigram features in train set
    bigram = BigramCollocationFinder.from_words(all_words)
    top_bigrams = list(bigram.nbest(BigramAssocMeasures.likelihood_ratio, num_bigrams))
    bigram_features = [(colloc[0] + ' ' + colloc[1]) for colloc in top_bigrams]

    return word_features + bigram_features


def extract_features(x_vals, y_vals, features):
    # bag of words vectorization of tokens
    bow_vectorizer = CountVectorizer(vocabulary=features, lowercase=False, ngram_range=(1, 2))
    x = bow_vectorizer.fit_transform(x_vals).toarray()

    # get boolean val of sentiment
    y_list = [1 if sent == 'positive' else 0 for sent in y_vals.tolist()]
    y = np.asarray(y_list)

    return x, y


def get_ready_data(data, num_bigrams, test_size):
    # create data frame from list of tuples
    tweet_df = pd.DataFrame(data, columns=['tokens', 'sentiment'])

    # split into test,train of given size
    X_train, X_test, Y_train, Y_test = train_test_split(tweet_df['tokens'], tweet_df['sentiment'], test_size=test_size)

    # get word_ bigram features for train set
    feature_vec = get_feature_vector(X_train, num_bigrams)

    # get vectorized x and boolean y
    x_train, y_train = extract_features(X_train, Y_train, feature_vec)
    x_test, y_test = extract_features(X_test, Y_test, feature_vec)

    return x_train, x_test, y_train, y_test


def run_nn(x_train, x_test, y_train, y_test, epochs, batch_size):
    # get number of features/words
    input_dim = x_train.shape[1]

    # create sequential model
    model = Sequential()
    model.add(layers.Dense(10, input_dim=input_dim, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    opt = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    # model.summary()

    # fit model and set params
    history = model.fit(x_train, y_train, epochs=epochs, verbose=False,
                        batch_size=batch_size, validation_split=0.2)

    # get classification accuracies
    _, train_accuracy = model.evaluate(x_train, y_train, verbose=False)
    _, test_accuracy = model.evaluate(x_test, y_test, verbose=False)

    return train_accuracy, test_accuracy


########################################################################################################################

tweets = get_from_file()

equal_tweets = get_equal_class(tweets)

test_size = 0.2
num_bigrams_features = 10
x_train, x_test, y_train, y_test = get_ready_data(equal_tweets, num_bigrams_features, test_size)

train_acc, test_acc = run_nn(x_train, x_test, y_train, y_test, 50, 10)

print("Training Accuracy:  {:.2f}".format(train_acc * 100))
print("Testing Accuracy:  {:.2f}".format(test_acc * 100))
