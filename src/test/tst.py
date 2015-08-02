from sklearn.feature_extraction.text import TfidfVectorizer
import operator
import io
import random
import numpy as np
from numpy import arange
import nltk
from nltk import word_tokenize
def tweets2tags(text,hasht):
        tx=[]
        for line in text:
            tokens=word_tokenize(line)
                tags=nltk.pos_tag(tokens)

                text= [s[0] for s in tags if s[1].startswith('NN')]
                tx.extend(text)

        vectorizer = TfidfVectorizer(stop_words="english",min_df=1)
        X = vectorizer.fit_transform(tx)
        idf = vectorizer.idf_
        size=len(idf)
        idf[:size/5]=2
        idf[size/5:2*size/5]=3
        idf[2*size/5:3*size/5]=4
        idf[3*size/5:4*size/5]=5
        idf[4*size/5:]=7
        tags =  dict(zip(vectorizer.get_feature_names(), idf))
        for i in hasht:
            tags[i] = 6
        return tags
