from sklearn.feature_extraction.text import TfidfVectorizer
import operator
import numpy as np
from nltk.tag import StanfordNERTagger
from nltk.tag import pos_tag
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') 
f = open('temp.txt', 'r')
text = f.readlines()
#text=text[:50]
text = map(lambda word: word.replace('@', ''), text)
text=map(lambda word : word.replace('#',''),text)
print(pos_tag(text[0].split()))
vectorizer = TfidfVectorizer(stop_words="english",min_df=1)
X = vectorizer.fit_transform(text)
idf = vectorizer.idf_

idfdict =  dict(zip(vectorizer.get_feature_names(), idf))
#idfdict =  dict(zip(vectorizer.get_feature_names(), idf[np.where(idf>4)]))
sorted_x=sorted(idfdict.items(), key=operator.itemgetter(1))
###############

#print st.tag(vectorizer.get_feature_names())
#,vectorizer.get_feature_names()) 
