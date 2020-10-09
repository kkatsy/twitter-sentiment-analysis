# twitter-sentiment-analysis


1. **Tweet Query:**
    For the topic of my tweets I chose the word 'vaccine,' specifically because it is a hot topic in the media right now, and I hoped that I would be able to observe both very strong positive and very strong negative sentiments.


2. **Getting the Tweets:**
    I used the Tweepy library to access the Twitter API and gather tweets. Before storing the queries, I preprocessed the tweet text by removing special characters, numbers, and usernames and lowercasing the text. Additionally, I used Tweepy's get_sentiment function to obtain the sentiment of each tweet, according to Tweepy's corpus.

3. **Further Processing:**
    After calling the Twitter API an ample number of times, I gathered a total of 4330 tweets, however, after removing non-english tweets and retweets, there were 2298 tweets remaining. In addition, I manually classified these tweets as 'positive', 'negative', or 'neutral/other'.

4. **Frequency Distributions:**

    <table>
    <tr><th>Tweepy's get_sentiment classification:</th><th>My manual sentiment classification:</th></tr>
    <tr><td>

    |sentiment|tweet #|percentage|
    |---------|:-----:|----------|
    |positive|1074|46.74 %|
    |negative|558|24.28 %|
    |neutral|666|28.98 %|

    </td><td>

    |sentiment|tweet #|percentage|
    |---------|:-----:|----------|
    |positive|454|19.76 %|
    |negative|1066|46.39 %|
    |neutral|778|33.86 %|

    </td></tr> </table>

    Comparing this data, it is quite clear that the Tweepy get_sentiment classification labeled considerably more tweets as 'positive' than did I manually. I hypothesize that the two main reasons for this is: 1) lack of context and 2) sarcasm. Many of the tweets that I labeled as 'negative' were sarcastically making fun of an original tweet or an opposing viewpoint, and it is not surprising that a non-human classifier would fail to recognize a negative sentiment if a tweet contained enough positive words.
    A more tangible example of this: when examining the frequency distributions of positive tweets, the Tweepy sample labeled 'trump' as one of the top 20 most common words (with around 80 occurrences), while the manual sample did not. Having manually classified the tweets, I observed that very few tweets containing the word 'trump' had a positive sentiment, while the rest had a negative sentiment conveyed with sarcasm.


    20 most common words from the manually classified sample:

    | rank  | positive  | negative  |
    |---|:---:|---:|
    | 1  | 'will', 103  |  'will', 292 |
    | 2 |  'flu', 77 |  'not', 242 |
    | 3  |  'not', 58 | 'people', 177  |
    |  4 | 'get', 54)  | 'no', 176  |
    |  5 |  'can', 51 |  'trump', 146 |
    |  6 | 'people', 45  | 'get' , 123  |
    | 7  | 'covid', 41  | 'just', 115  |
    | 8  | 'coronavirus', 36  | 'covid', 113  |
    |  9 |  'no', 34 | 'flu', 106  |
    | 10 | 'safe', 34  |  'virus', 98 |
    | 11  | 'now', 33  | 'us', 97  |
    | 12  | 'countries', 33  |  'take', 96 |
    |  13 | 'need', 32  |  'can' , 94 |
    |  14 | 'vaccines', 32  | 'one', 92  |
    | 15  | 'us', 31  | 'like', 78  |
    |  16 |  'one', 29 | 'now', 69  |
    | 17  |  'first', 29 | 'going', 65  |
    |  18 | 'virus', 27  |  'even', 62 |
    |  19 | 'effective', 27  | 'coronavirus', 60  |
    | 20  |  'available', 27 | 'make', 59  |


5. **Most Common Collocations:**

    <table>

    <tr><td>

    | Most common positive collocations:|
    |:---:|
    |'herd immunity'|
    |'156 countries'|
    |'announce tougher'|
    |'tougher standards'|
    |'cleared election'|
    |'yellow fever'|
    |'safe effective'|
    |'freedom choice'|
    |'flu shot'|
    |'important ever'|
    |'election day'|
    |'allocation deal'|
    |'make unlikely'|
    |'medical freedom'|
    |'covax facility'|

    </td><td>

    | Most common negative collocations:  |
    |:---:|
    |'herd immunity'|
    |'bill gates'|
    |'6 months'|
    |'announce tougher'|
    |'tougher standards'|
    |'flu shot'|
    |'cleared election'|
    |'election day'|
    |'cdc scandal'|
    |'make unlikely'|
    |'public health'|
    |'wear mask'|
    |'unlikely one'|
    |'big pharma'|
    |'death toll'|

    </td></tr> </table>

6. **Creating Train Set and Test Set:**

7. **NLTK and Naive Bayes:**
   *Bag of Words Vectorization:*
- Initial accuracy:                   0.7458563535911602
- With top ten collocations:          0.7821229050279329

8. **Sklearn, Keras, and NN:**

9. **Classification Conclusions:**

10. **Faults and Flaws:**

11. **Further Ruminations:**


### Files:
- *get_tweets.py*      - obtaining tweets using Twitter API, basic preprocessing, getting sentiment + polarity using Tweepy library
- *process_tweets.py*  - processing further, removing duplicates/retweets and stopwords, manual sentiment classification
- *analyze_tweets.py*  - tweet tokenization, finding frequency distributions, gettings bigrams and most common collocations
- *naive_bayes.py*     - creating equal size train/test sets, BoW vectorization, plus collocations, nltk NaiveBayes classification
- *keras_nn.py*        - (TODO)
- *store_tweets.py*    - (TODO)


### Sources:
- [pre-processing + word frequency](https://towardsdatascience.com/keras-challenges-the-avengers-541346acb804)
- [geeks for geeks](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/): twitter api basics
- [simple example](https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/ ): manually classified, nltk, and python
- [nltk stop words](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/)
- [building corpus + good tutorial](https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed)
- [Stopwords source](https://www.ranks.nl/stopwords)
- [Bag of Words + TF-IDF](https://towardsdatascience.com/selenium-tweepy-to-scrap-tweets-from-tweeter-and-analysing-sentiments-1804db3478ac)
- [NN Implementation + Explanations](https://realpython.com/python-keras-text-classification/)

### Misc Reading Material:
- [Zipf’s word frequency law in natural language](https://dwulff.github.io/_Naturallanguage/Literature/ZipfLaw2.pdf)
- [Negation handling in sentiment analysis](http://www.jcomputers.us/vol12/jcp1205-11.pdf)
- [The Disputed Federalist Papers](http://pages.cs.wisc.edu/~gfung/federalist.pdf)
- [Imbalanced classes in data set](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)
- [King – Man + Woman = Queen](https://www.technologyreview.com/2015/09/17/166211/king-man-woman-queen-the-marvelous-mathematics-of-computational-linguistics/)
- [Accuracy decreasing with higher epochs](https://stackoverflow.com/questions/53242875/accuracy-decreasing-with-higher-epochs)