import pickle

# see contents of pickled files
FILENAME = "raw_tweets.pickle"
pickle_off = open(FILENAME,"rb")
contents = pickle.load(pickle_off)

print(contents)