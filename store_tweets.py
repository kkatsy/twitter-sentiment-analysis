import pickle
import os
import mysql.connector

# aggregate all preprocessed tweets into single list
# tweet_list = []
# call_num = 0
# while os.path.isfile('processed_tweets_' + str(call_num) + '.pickle'):
#     with open('processed_tweets_' + str(call_num) + '.pickle', 'rb') as f:
#         tweet_batch = pickle.load(f)
#     tweet_list.extend(tweet_batch)
#     call_num += 1

tweet_db = mysql.connector.connect(
  host="localhost",
  user="usrname",
  password="password"
)


print(tweet_db)