import pickle

# see contents of pickled files

FILENAME = "filtered_1.pickle"
pickle_off = open(FILENAME, "rb")
contents = pickle.load(pickle_off)

print(contents)
