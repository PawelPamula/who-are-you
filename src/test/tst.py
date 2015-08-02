from sklearn.feature_extraction.text import TfidfVectorizer
import operator
import io
import random
import numpy as np
from numpy import arange
from nltk.tag import StanfordNERTagger
import nltk
from nltk import word_tokenize
def tweets2tags(text,hasht):
#	hasht = ["#imaginecup", "#winner", "#holographicAcademy", "#UpgradeYourWorld"]
#	f = io.open('temp.txt', 'r', encoding='utf-8')
#	text = f.readlines()
#	text = map(lambda word: word.replace('@', ''), text)
#	text = map(lambda word: word.replace('#', ''), text)
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
		
#	tags=sorted(idfdict.items(), key=operator.itemgetter(1))
#	print("rand",random.sample(sorted_x[size-70:], 3))
#	print(tags)
#idfdict =  dict(zip(vectorizer.get_feature_names(), idf[np.where(idf>7.4)]))

	
