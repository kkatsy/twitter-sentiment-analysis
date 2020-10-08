from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
import nltk
import pickle, os, random

# aggregate all classified tweets into single list
classified = []
if os.path.isfile('filtered.pickle'):
    with open('filtered.pickle', 'rb') as f:
        classified = pickle.load(f)

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

train = equal_class[:int(max_num * 2 * 0.8)]
len_train = len(train)
test = [tweet for tweet in equal_class if tweet not in train]
len_test = len(test)

all_words = []
for tweet in train:
    all_words.extend(tweet[0])
word_list = nltk.FreqDist(all_words)
word_features = word_list.keys()

bigram = BigramCollocationFinder.from_words(all_words)
bi_colloc = bigram.nbest(BigramAssocMeasures.likelihood_ratio, 10)


# trigram = TrigramCollocationFinder.from_words(all_words)
# tri_colloc = trigram.nbest(TrigramAssocMeasures.likelihood_ratio, 5)

def get_features(text):
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in text)

    joined = ' '.join(text)
    for colloc in bi_colloc:
        colloc = ' '.join(colloc)
        features['contains(%s)' % colloc] = (colloc in joined)

    # for colloc in tri_colloc:
    #     colloc = ' '.join(colloc)
    #     features['contains(%s)' % colloc] = (colloc in joined)

    return features


train_set = nltk.classify.apply_features(get_features, train)
classifier = nltk.NaiveBayesClassifier.train(train_set)

correct = 0
for tweet in test:
    pred = classifier.classify(get_features(tweet[0]))
    if pred == tweet[1]:
        correct += 1

    print('Text: ', tweet[0])
    print('Prediction: ', pred)
    print('Actual: ', tweet[1])

print('Accuracy: ', (correct / len(test)))


#######################################################################################################################
