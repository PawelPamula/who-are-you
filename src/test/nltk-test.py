# From http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford

from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') 
print st.tag('Rami Eid is studying at Stony Brook University in NY. And he wants to work at CERN in Switzerland in Europe .'.split()) 
