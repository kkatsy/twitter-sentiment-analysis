import os, pickle, random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras import layers
from tensorflow import keras


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


def get_ready_data(data):
    # create data frame from list of tuples
    tweet_df = pd.DataFrame(data, columns=['tokens', 'sentiment'])

    # bag of words vectorization of tokens
    bow_vectorizer = CountVectorizer(lowercase=False)
    x = bow_vectorizer.fit_transform(tweet_df['tokens']).toarray()

    # get boolean val of sentiment
    tweet_df['sentiment'] = tweet_df['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)
    y = tweet_df['sentiment'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

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
    model.summary()

    # fit model and set params
    history = model.fit(x_train, y_train, epochs=epochs, verbose=False,
                        batch_size=batch_size, validation_data=(x_test, y_test))

    # get classification accuracies
    _, train_accuracy = model.evaluate(x_train, y_train, verbose=False)
    _, test_accuracy = model.evaluate(x_test, y_test, verbose=False)

    return train_accuracy, test_accuracy


########################################################################################################################

tweets = get_from_file()

equal_tweets = get_equal_class(tweets)

x_train, x_test, y_train, y_test = get_ready_data(equal_tweets)

train_acc, test_acc = run_nn(x_train, x_test, y_train, y_test, 50, 10)

print("Training Accuracy:  {:.2f}".format(train_acc * 100))
print("Testing Accuracy:  {:.2f}".format(test_acc * 100))
