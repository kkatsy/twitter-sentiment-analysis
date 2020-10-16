# twitter-sentiment-analysis


1. **Tweet Query:**
    For my topic of investigation, I chose to look into tweets containing the word "vaccine." I hoped that, since the creation and usage of vaccines is a hot and ambivalent topic nowadays, this query word provide me with tweets of both very positive and very negative sentiments.

2. **Getting the Tweets:**

    I collected tweets using the Twitter API via the [Tweepy](http://docs.tweepy.org/en/latest/api.html#tweepy-api-twitter-api-wrapper) library. All of my tweets were collected over the course of three days mid-September and stored in a single pickle file. As tweets were collected, they underwent basic preprocessing: removal of special characters using regex and getting text sentiment using TextBlob's [sentiment property](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.sentiment).

3. **Further Processing:**
    After calling the Twitter API an ample number of times, I gathered a total of 4330 tweets. After removing non-english tweets and retweets, there were 2298 tweets remaining. These tweets underwent further preprocessing: stop words, links, non-english, and duplicates tweets were removed. In addition, I manually classified the remaining, english-language tweets as 'positive', 'negative', or 'neutral/other'.

    A note on stopwords: while the removal of stop words is not a necessary practice in modern-day speech processing, I made the decision to remove stopwords so that I could reduce the number features in my humbly sized data sample.

4. **Frequency Distributions:**

    <table>
    <tr><th>TextBlob's sentiment property:</th><th>Manual sentiment classification:</th></tr>
    <tr><td>

    |sentiment|tweet #|percentage|
    |:-------:|:-----:|:--------:|
    |positive|1074|46.74 %|
    |negative|558 |24.28 %|
    |neutral |666 |28.98 %|

    </td><td>

    |sentiment|tweet #|percentage|
    |:-------:|:-----:|:--------:|
    |positive|454 |19.76 %|
    |negative|1066|46.39 %|
    |neutral |778 |33.86 %|

    </td></tr> </table>

    Comparing this data, it is quite clear that the TextBlob sentiment property labeled considerably more tweets as 'positive' than did I manually. I hypothesize that the two main reasons for this is: 1) error caused lack of social and political context and 2) inability to detect sarcasm. Many of the tweets that I labeled as 'negative' were sarcastically making fun of an opposing viewpoint or made reference to individuals/entities that had certain popular connotations.

    **20 most common words from the manually classified sample:**

    | rank  | positive  | negative  |
    |:-----:|:---------:|:---------:|
    | 1   | 'will', 103  |  'will', 292 |
    | 2   |  'flu', 77 |  'not', 242 |
    | 3   |  'not', 58 | 'people', 177  |
    |  4  | 'get', 54  | 'no', 176  |
    |  5  |  'can', 51 |  'trump', 146 |
    |  6  | 'people', 45  | 'get' , 123  |
    | 7   | 'covid', 41  | 'just', 115  |
    | 8   | 'coronavirus', 36  | 'covid', 113  |
    |  9  |  'no', 34 | 'flu', 106  |
    | 10  | 'safe', 34  |  'virus', 98 |
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
    |:---------------------------------:|
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
    |:-----------------------------------:|
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
- 70/30 test split
- BoW vectorization
- for nltk: manually shuffle then partition, create boolean vec
- for keras: sklearn's train_test_split + Count Vectorizer
- 
7. **NLTK and Naive Bayes:**

| # of bigram features | average accuracy  |
|:--------------------:|:-----------------:|
| 1 bigram    | 0.7215  |
| 5 bigrams   | 0.7184  |
| 10 bigrams  | 0.7256  |
| 15 bigrams  | 0.7145  |
| 20 bigrams  |  0.7156 |
| 30 bigrams  | 0.7195  |
| 40 bigrams  | 0.7115  |
| 50 bigrams  | 0.7173  |

8. **Sklearn, Keras, and NN:**

**Accuracy with 50 epochs:**

| # of bigram features | average accuracy  |
|:--------------------:|:-----------------:|
| 1 bigram    | 0.7205 |
| 5 bigrams   | 0.7275 |
| 10 bigrams  | 0.7278 |
| 15 bigrams  | 0.7273 |
| 20 bigrams  | 0.7057 |
| 30 bigrams  | 0.7205 |
| 40 bigrams  | 0.7179 |
| 50 bigrams  | 0.7095 |

**Accuracy with 100 epochs:**

| # of bigram features | average accuracy  |
|:--------------------:|:-----------------:|
| 1 bigram    | 0.7236 |
| 5 bigrams   | 0.7168 |
| 10 bigrams  | 0.7278 |
| 15 bigrams  | 0.7214 |
| 20 bigrams  | 0.7198 |
| 30 bigrams  | 0.7264 |
| 40 bigrams  | 0.7310 |
| 50 bigrams  | 0.7300 |

**Accuracy with 200 epochs:**

| # of bigram features | average accuracy  |
|:--------------------:|:-----------------:|
| 1 bigram    | 0.7238 |
| 5 bigrams   | 0.7214 |
| 10 bigrams  | 0.7005 |
| 15 bigrams  | 0.7064 |
| 20 bigrams  | 0.7137 |
| 30 bigrams  | 0.7178 |
| 40 bigrams  | 0.7143 |
| 50 bigrams  | 0.7125 |

9. **Classification Conclusions:**

10. **Faults and Flaws:**

- small data sample, can't add new data because would mess with curr data

11. **Further Ruminations:**


### Files:
- *get_tweets.py*      - obtaining tweets using Twitter API and Tweepy, basic preprocessing, getting sentiment + polarity using TextBlob, storing results in pickle file
- *process_tweets.py*  - processing further, removing duplicates/retweets and stop words, manual sentiment classification, storing results in pickle file
- *analyze_tweets.py*  - tweet tokenization, finding frequency distributions, gettings bigrams and most common collocations
- *naive_bayes.py*     - creating equal size train/test sets, manual BoW vectorization, nltk NaiveBayes classification
- *keras_nn.py*        - creating train/test sets with sklearn train_test_split, getting Bow vector using sklearn CountVectorizer, keras NN classification
- *store_tweets.py*    - (TODO) store processed/filtered tweets in a MySQL DB or RedisDB


### Sources:
- [Pre-processing Tweet Data](https://towardsdatascience.com/keras-challenges-the-avengers-541346acb804)
- [Twitter API Basics with Tweepy](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/)
- [Simple NLTK-only Example](https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)
- [Non-NLTK Stop Words Source](https://www.ranks.nl/stopwords)
- [Bag of Words + TF-IDF Vectorization](https://towardsdatascience.com/selenium-tweepy-to-scrap-tweets-from-tweeter-and-analysing-sentiments-1804db3478ac)
- [NN Implementation + Great Explanations](https://realpython.com/python-keras-text-classification/)


### Misc Reading Material:
- [Zipf’s Word Frequency Law in NL](https://dwulff.github.io/_Naturallanguage/Literature/ZipfLaw2.pdf)
- [Negation Handling in Sentiment Analysis](http://www.jcomputers.us/vol12/jcp1205-11.pdf)
- [The Disputed Federalist Papers](http://pages.cs.wisc.edu/~gfung/federalist.pdf)
- [Imbalanced classes in Data](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)
- [King – Man + Woman = Queen](https://www.technologyreview.com/2015/09/17/166211/king-man-woman-queen-the-marvelous-mathematics-of-computational-linguistics/)
- [Accuracy decreasing with higher epochs](https://stackoverflow.com/questions/53242875/accuracy-decreasing-with-higher-epochs)