# twitter-sentiment-analysis

0. **Project Summary:**

    *(TODO)* add project summary + goals

1. **Tweet Query:**

   For my topic of investigation, I chose to look into tweets containing the word "vaccine." I hoped that, since the creation and usage of vaccines is a hot and ambivalent topic nowadays due to COVID, this query word provide me with tweets of both very positive and very negative sentiment.

2. **Getting the Tweets:**

   I collected tweets using the Twitter API via the [Tweepy](http://docs.tweepy.org/en/latest/api.html#tweepy-api-twitter-api-wrapper) library. All of my tweets were collected over the course of three days mid-September and stored in a single pickle file.

   As tweets were collected, they underwent basic preprocessing: removal of special characters using regex and getting text sentiment using TextBlob's [sentiment property](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.sentiment).

3. **Further Processing:**

   After calling the Twitter API an ample number of times, I gathered a total of 4330 tweets. After removing non-english tweets and retweets, there were 2298 tweets remaining. These tweets underwent further preprocessing: stop words, links, and duplicate tweets were removed.

   In addition, I manually classified the remaining, english-language tweets as 'positive', 'negative', or 'neutral/other' based on their sentiment. Manual classification proved to be a bit of a challenge for a couple of reasons. I did not quite realize how time consuming of a task manual classification would be and how difficult it can be to make a call regarding sentiment. There were moments where I felt like I was slightly redefining what it meant for a tweet to be 'positive' or 'negative' while in the process of classification. Sometimes, a tweet would express negativity in one sentence and positivity in another, and I had to make a call regarding dominant sentiment. Additionally, it was sometimes difficult to tell if a tweet was sarcastic or not without full thread context.

   A note on stopwords: while the removal of stop words is not a necessary practice in modern-day speech processing, I made the decision to remove stopwords since I was planning on using a bag of words vectorization approach. However, I did not use NLTK's list of stopwords but [this one](https://www.ranks.nl/stopwords) instead since I did not want to discard negation words, which are quite important in sentiment analysis.

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

    Comparing this data, it is quite clear that the TextBlob sentiment property labeled considerably more tweets as 'positive' than did I manually. I suspect that the two main reasons for this are: 1) error caused by lack of social and political context and 2) inability to detect sarcasm. Many of the tweets that I labeled as 'negative' were sarcastically making fun of an opposing viewpoint or made reference to individuals/entities that had certain popular connotations.

    Additionally, while I had hoped that this query would provide me with sufficient examples of both sentiments, this percentage breakdown clearly shows an unequal distribution of positive and negative tweets. Compared to the amount of negative tweets, there were very few positive tweets. This inequality creates an issue of unequal class size, which has two solutions: to continue working with a disproportionate amount of negative tweets, or discarding tweets in order to work with smaller but equal sized classes. I chose the latter option, since I did not want my classifier to overfit the dominant class.

5. **Most Common Words**

    I used NLTK's FreqDist to obtain the frequency distributions of words in positive and negative tweets. Some words appear in both samples, since many positive and negative tweets discussed similar topics but from a different sentiment perspective.

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


6. **Most Common Collocations:**

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

    Once again, when comparing the most common collocations for both sentiments, some bigrams commonly appeared in tweets of both positive and negative sentiment, because some topics are discussed with varying sentiments. However, for the collocations that are unique, it is easier to see the sentiment of a collocation out of context than it is with a single word frequency.

7. **Creating Train Set and Test Set:**

   I created two different classification models, one with NLTK's Naive Bayes and another with a Keras Neural Network. I chose to do a bag of words vectorization for both, however I approached splitting the train/test data and vectorization a bit differently for each model for the sake of practice.

   After doing some googling, I noticed that a common recommended split ratio was 80/20; however, many sources recommended using less data for training if the total data set size was small (so as to prevent overfitting). As a result, I decided to do a 70/30 train/test split for both models.

   *For the Naive Bayes model:* I randomly shuffled my data set, then manually split the data into train and test sets. Then, for the vectorization, I got a list of all words in the train set via the NLTK's FreqDist and then created boolean vectors based on what words from the train set were in/not in each tweet.

   *For the Neural Network model:* I used sklearn's train_test_split to split the data and used and CountVectorization to get back a boolean bag of words vector for each tweet.

8. **NLTK and Naive Bayes:**

    I wanted to see if perhaps changing the number of features by adding most common bigrams to the feature vector would affect the Naive Bayes model's accuracy. I ran the model 20 times and averaged the recorded accuracies to obtain an average accuracy for different numbers of bigram BoW features.

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

    However, based on these results, it does not seem that the number of bigram features had any effect on the classification accuracy.

9. **Sklearn, Keras, and NN:**

     As with the Naive Bayes model, I wanted to see if the number of bigram features would have an effect on the NN model's accuracy. Additionally, I wanted to see how the number of epochs would impact the model as well. As a result, I ran the model for 50, 100, and 200 epochs with different numbers of bigram BoW features and recorded the average accuracy of 20 runs.

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

     However, based on these results, it does not seem that either the number of bigram features nor the number of epochs used had a significant effect on the classification accuracy.

     Additionally, when I ran the NN model, I compared the accuracy of the train set to the accuracy of the test set; I generally got around an accuracy in the 90s for the train set and 70s for the test set. This difference in accuracy is an indication of overfitting occurring in the creation of the model, likely another result of having a small data set.

10. **BERT:**

    *(TODO)* create classifier with BERT

11. **LSTM:**

    *(TODO)* create LSTM classifier

12. **Classification Conclusions:**

    Based on my observed results, it seems like there was little to no difference in accuracy in terms of the two models. Generally, one would expect the Neural Network to outperform Naive Bayes. However, even after significantly lowering the learning rate for the Adam optimizer, the NN did not do better than Naive Bayes on average. A likely explanation for this observation: simpler models often perform better than complicated models when dealing with small data sets.

    *(TODO)* Add info about precision, recall, F1 scores

13. **Faults and Flaws:**

    *Small Data Set*: Undoubtedly my biggest issue was my small data set, which led to a myriad of issues, including not having enough train data and overfitting, which caused the neural network to perform badly and likely lead to overall lower accuracy than possible. However, simply adding to the data I originally collected was not an option, since the tweets I collected were specific to the date when I collected them and the current events going on at that time. Adding newer tweets would lead to a larger data sample, but it may also undermine the purpose of the project, which focused more on vaccine sentiment during a specific point in the news cycle than the attitude toward all vaccines in general.

    *Unequal Class Size*: Having many more negative than positive tweets is not necessarily a bad thing (it does show that popular sentiment toward the query "vaccine" is largely more negative), but it did lead me to reduce the size of my already small data set to obtain equal class sizes in order to try to avoid potential overfitting towards the dominant class.

    *Overfitting*: Comparing accuracies of the train and test set for the NN model, it was clear that the model was overfitting the train set. Given the small size of the data set, it is also likely that overfitting occurred for the Naive Bayes model as well. This, of course, is not good, because the model created with the train set ends up being a less accurate predictor of the test set's sentiment.

14. **Potential Methods for Improvement:**

    As I was working on the project and after I had finished the project, I noted several potential improvements that could be implemented that might either address the current models' faults or just lead to overall improvement in classification accuracy.

    *TFIDF Vectorization*: using a vectorization method that relies on compositional semantics rather than just lexical semantics (i.e. what bag of words does) could potentially lead to more accurate classification. The results of the two types of vectorizations would need to compared to determine which provides a better accuracy.

    *Larger Sample*: Having a larger sample may resolve some of the issues that I had encountered. However, as previously mentioned, in order to get a larger sample it would likely be reasonable to get a new data set entirely than to add on to the previously collected tweets.

    *Logistic Regression*: LR is another common, simple classification model. Again, one would have to compare the result of LR with the NN and Naive Bayes to see which model performs best.

    *Data Augmentation:* Additionally, there exist methods to alter existing data to improve the usability of a data set with a smaller size than would be preferred.

15. **Further Ruminations:**
    ...


### Files:
- *get_tweets.py*      - obtaining tweets using Twitter API and Tweepy, basic preprocessing, getting sentiment + polarity using TextBlob, storing results in pickle file
- *process_tweets.py*  - further processing, removing duplicates/retweets and stop words, manual sentiment classification, storing results in pickle file
- *analyze_tweets.py*  - tweet tokenization, finding frequency distributions, gettings bigrams and most common collocations
- *naive_bayes.py*     - creating equal size train/test sets, manual BoW vectorization, nltk NaiveBayes classification
- *keras_nn.py*        - creating train/test sets with sklearn train_test_split, getting Bow vector using sklearn CountVectorizer, keras NN classification
- *bert.py*            - (TODO)
- *lstm.py*            - (TODO)
- *store_tweets.py*    - (TODO) store processed/filtered tweets in a MySQL DB or RedisDB for practice


### Sources:
- [Pre-processing Tweet Data](https://towardsdatascience.com/keras-challenges-the-avengers-541346acb804)
- [Twitter API Basics with Tweepy](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/)
- [Simple NLTK-only Example](https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)
- [Bag of Words + TFIDF Vectorization](https://towardsdatascience.com/selenium-tweepy-to-scrap-tweets-from-tweeter-and-analysing-sentiments-1804db3478ac)
- [NN Implementation + Great Explanations](https://realpython.com/python-keras-text-classification/)


### Misc Reading Materials:
- [Zipf’s Word Frequency Law in NL](https://dwulff.github.io/_Naturallanguage/Literature/ZipfLaw2.pdf)
- [Negation Handling in Sentiment Analysis](http://www.jcomputers.us/vol12/jcp1205-11.pdf)
- [The Disputed Federalist Papers](http://pages.cs.wisc.edu/~gfung/federalist.pdf)
- [Imbalanced classes in Data](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)
- [King – Man + Woman = Queen](https://www.technologyreview.com/2015/09/17/166211/king-man-woman-queen-the-marvelous-mathematics-of-computational-linguistics/)
- [Accuracy decreasing with higher epochs](https://stackoverflow.com/questions/53242875/accuracy-decreasing-with-higher-epochs)
- [Data Augmentation library for text](https://towardsdatascience.com/data-augmentation-library-for-text-9661736b13ff)
- [Data Augmentation techniques for NLP](https://maelfabien.github.io/machinelearning/NLP_8/#)
