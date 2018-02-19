from nltk import RegexpTokenizer
from nltk.corpus import stopwords
import multiprocessing

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
stopword_set = set(stopwords.words('english'))

#This function does all cleaning of data using two objects above
def nlp_clean(data):
    new_str = data.lower()
    dlist = tokenizer.tokenize(new_str)
    dlist = list(set(dlist).difference(stopword_set))
    return dlist

class LabeledLineSentence(object):
    def __init__(self, filename1,filename2):
        self.filename1 = filename1
        self.filename2 = filename2
    def __iter__(self):
        for uid, (line1,line2) in enumerate(zip(open(self.filename1),open(self.filename2))):
            yield gensim.models.doc2vec.LabeledSentence(nlp_clean(line1),line2.split())

sentences = LabeledLineSentence('/home/eric/Data/reviewlist','/home/eric/Data/idlist')
import gensim
from gensim.models import Doc2Vec
import os
import logging

logging.basicConfig(level=logging.INFO)
print(os.sched_getaffinity)
os.sched_setaffinity(0, range(4))

assert gensim.models.doc2vec.FAST_VERSION > -1

model = Doc2Vec(sentences, size=300, min_count=10, alpha=0.025, min_alpha=0.001, workers=multiprocessing.cpu_count())  

model.save("/home/eric/Data/doc2vec.model")