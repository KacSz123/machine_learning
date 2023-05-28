# import sklearn
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GroupShuffleSplit
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import pickle
# a,b = load_svmlight_file("./data/brexit/TextBrexit2_text.txt")
import numpy as np
''' Pobranie danych i stworzenie jednorodnego zbioru uczacego/testowego'''
def load_file(filename, headNames=None):
    return pd.read_csv(filename, sep='\t',names=headNames)
##### upload data from file
# data=load_file("./data/brexit/TextBrexit2_text.txt", headNames=["classifier", "text"]) #
def NaiveBayesBoWCross(filename="./data/brexit/TextBrexit2_text.txt", save=None):
    cross_data = load_file(filename, headNames=["classifier", "text"]) 

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
    for train_index, test_index in split.split(cross_data, cross_data["classifier"]):
        data = cross_data.loc[train_index]
        test = cross_data.loc[test_index]
    ##### BoW
    count_vect = CountVectorizer(ngram_range=(4,4))
    X_text_counts = count_vect.fit_transform(data.text)
    # print(X_text_counts)
    # train_set, test_set = train_test_split(a, test_size=0.3, random_state=42)
    ######  TF ######
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_text_counts)
    X_text_tf = tf_transformer.transform(X_text_counts)
    print(X_text_tf.shape)

    ####### TF - IDF ########
    tfidf_transformer = TfidfTransformer()
    X_text_tfidf = tfidf_transformer.fit_transform(X_text_counts)
    # print(X_text_tfidf.shape)

    ####### naive bayes
    clf = MultinomialNB().fit(X_text_tfidf, data.classifier)
    docs_new = test.text
    X_new_counts = count_vect.transform(docs_new)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict(X_new_tfidf)
    print()
    print(np.mean(predicted==test.classifier))
    print()
    # print(predicted)
    ''''''
    print(metrics.classification_report(test.classifier, predicted))
    if save!=None:
        pickle.dump(clf, open("naive_bayes_model.sav",'wb'))
    #################################################################################################<
    #################################################################################################<
    #################################################################################################<
def NaiveBayesBoWTrain( train_file="./data/brexit/TextBrexit2_text.txt", test_file = None, _headNames=["classifier", "text"]):
    
    if test_file==None:
        cross_data = load_file(train_file, headNames=_headNames) 
        split = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
        for train_index, test_index in split.split(cross_data, cross_data["classifier"]):
            data = cross_data.loc[train_index]
            test = cross_data.loc[test_index]
    else:
        data=load_file(train_file, _headNames)
        test=load_file(test_file, _headNames)
    ##### BoW
    count_vect = CountVectorizer()
    X_text_counts = count_vect.fit_transform(data.text)
    # train_set, test_set = train_test_split(a, test_size=0.3, random_state=42)
    ######  TF ######
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_text_counts)
    X_text_tf = tf_transformer.transform(X_text_counts)
    print(X_text_tf.shape)

    ####### TF - IDF ########
    tfidf_transformer = TfidfTransformer()
    X_text_tfidf = tfidf_transformer.fit_transform(X_text_counts)
    # print(X_text_tfidf.shape)

    ####### naive bayes
    clf = MultinomialNB().fit(X_text_counts, data.classifier)
    docs_new = test.text
    X_new_counts = count_vect.transform(docs_new)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = clf.predict(X_new_tfidf)
    print()
    print(np.mean(predicted==test.classifier))
    print()
    # print(predicted)
    ''''''
    print(metrics.classification_report(test.classifier, predicted,target_names=['against','neutral', 'for']))
    ''''''''''''''''''''


NaiveBayesBoWCross()
    # count_vect1 = CountVectorizer()
    # X_train_counts = count_vect1.fit_transform(strat_train_set.text)
    # tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    # X_train_tf = tf_transformer.transform(X_train_counts)
    # print(X_train_tf.shape)

# ###### tf
# tf_transformer1 = TfidfTransformer(use_idf=False).fit(X_train_counts)
# X_train_tf = tf_transformer1.transform(X_train_counts)

# ####### TF - IDF ########
# tfidf_transformer1 = TfidfTransformer()
# X_train_tfidf = tfidf_transformer1.fit_transform(X_train_counts)


# ##### naive bayes
# clf1 = MultinomialNB().fit(X_train_tfidf, strat_train_set.classifier)
# docs_test = strat_test_set.text
# docs_test = ['brexit', 'referendum', 'britains']
# X_test_counts = count_vect.transform(docs_test)
# # X_test_tfidf = tfidf_transformer.transform(X_train_counts)

# predicted = clf1.predict(X_test_counts)