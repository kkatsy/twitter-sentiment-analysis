# twitter-sentiment-analysis

1. *Getting the Tweets:* I used the Tweepy library to access the Twitter API and gather tweets. Before storing the queries, I preprocessed the tweet text by removing special characters, numbers, and usernames and lowercasing the text. Additionally, I used Tweepy's get_sentiment function to obtain the sentiment of each tweet, according to Tweepy's corpus.

2. *Tweet Query:* For the topic of my tweets I chose the word 'vaccine,' specifically because it is a hot topic in the media right now with both very strong positive and very strong negative sentiments being expressed.

3. *Further Processing:*
After calling the Twitter API an ample number of times, I gathered a total of 4330 tweets, however, after removing non-english tweets and retweets, there were 2298 tweets remaining. In addition, I manually classified these tweets as 'positive', 'negative', or 'neutral/other'.

4. *Frequency Distributions:*

    **According to my manual sentiment classification:**
    *Sentiment percentage*
    positive -> 454 ( 19.76 % ), negative -> 1066 ( 46.39 % ), neutral -> 778 ( 33.86 % )

    *20 most common words*
    positive -> ('will', 103), ('flu' , 77), ('not'    , 58), ('get', 54), ('can'   , 51), ('people', 45), ('covid', 41), ('coronavirus', 36), ('no'  , 34), ('safe' , 34), ('now', 33), ('countries', 33), ('need', 32), ('vaccines', 32), ('us'  , 31), ('one', 29), ('first', 29), ('virus', 27), ('effective'  , 27), ('available', 27)

    negative -> ('will', 292), ('not', 242), ('people', 177), ('no', 176), ('trump', 146), ('get'  , 123), ('just', 115), ('covid'     , 113), ('flu', 106), ('virus', 98), ('us' , 97), ('take'     , 96), ('can' , 94), ('one'     , 92), ('like', 78), ('now', 69), ('going', 65), ('even' , 62), ('coronavirus', 60), ('make'     , 59)

    **According to my Tweepy's get_sentiment classification:**
    *Sentiment percentage*
    positive -> 1074 (46.74 %), negative -> 558 (24.28 %), neutral -> 666 (28.98 %)

   *20 most common words*
    positive -> ('will', 284), ('not', 188), ('flu', 155), ('people', 141), ('get', 129), ('covid', 124), ('no', 122), ('can', 103), ('just', 94), ('us', 88), ('one', 81), ('now', 79), ('effective', 77), ('virus', 73), ('trump', 73), ('new', 72), ('safe', 72), ('first', 68), ('available', 67), ('take', 66)

    negative -> ('will', 192), ('not', 112), ('people', 92), ('one', 86), ('make', 84), ('coronavirus', 82), ('no', 78), ('get', 74), ('fda', 68), ('election', 68), ('day', 67), ('covid', 62), ('trump', 60), ('virus', 60), ('unlikely', 60), ('standards', 59), ('announce', 57), ('flu', 54), ('tougher', 54), ('just', 53)

    Comparing this data, it is quite clear that the Tweepy get_sentiment classification labeled considerably more tweets as 'positive' than did I manually. I hypothesize that the two main reasons for this is: 1) lack of context and 2)sarcasm. Many of the tweets that I labeled as 'negative' were sarcastically making fun of an original tweet or an opposing viewpoint, and it is not surprising that a non-human classifier would fail to recognize a negative sentiment if a tweet contained enough positive words.

6. *Creating Train Set and Classifying Test Set:*

7. *Sciency Conclusions:*

8. *Further Ruminations:*


**Files:**
- *get_tweets.py*      - something
- **process_tweets.py* - something
- *freq_dist.py*       - something
- *analyze_tweets.py*  - (TODO)
- *test_tweets.py*     - (TODO)
- *store_tweets.py*    - (TODO)


**Sources:**
- [pre-processing + word frequency](https://towardsdatascience.com/keras-challenges-the-avengers-541346acb804)
- [geeks for geeks](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/): twitter api basics
- [simple example](https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/ ): manually classified, nltk, and python
- [nltk stop words](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/)
- [building corpus + good tutorial](https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed)
- [Stopwords source](https://www.ranks.nl/stopwords)


**Misc:**
- [Zipf’s word frequency law in natural language](https://dwulff.github.io/_Naturallanguage/Literature/ZipfLaw2.pdf)
