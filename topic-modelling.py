from config import artists
from gensim.models.tfidfmodel	import	TfidfModel
from gensim.models import LsiModel
from gensim import similarities
import logging
import pickle
from pprint import pprint
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = pickle.load(open('dictionary-2.p', "rb"))
tokenized_lyrics = pickle.load(open('tokenized-lyrics-2.p', "rb"))
document_song_mapping = pickle.load(open('doc-song-mapping-2.p', "rb"))

corpus	=	[dictionary.doc2bow(doc)	for	doc	in	tokenized_lyrics]
tfidf	=	TfidfModel(corpus)
mydict = dictionary.token2id
inverted_dict = dict([[v,k] for k,v in mydict.items()])

#corpus_tfidf = tfidf[corpus]
#lsi = LsiModel(corpus_tfidf, id2word=dictionary, num_topics=5) # initialize an LSI transformation
#corpus_lsi = lsi[corpus_tfidf]
lsi = LsiModel(corpus, id2word=dictionary, num_topics=5) # initialize an LSI transformation
corpus_lsi = lsi[corpus]

#affection_lsi = tfidf[corpus[0]]
#affection_lsi = lsi[tfidf[corpus[0]]]
numb_lsi = lsi[corpus[3]]

#print corpus_tfidf[0]
#print corpus_lsi[0]
#print affection_lsi

index = similarities.MatrixSimilarity(lsi[corpus])
sims = index[numb_lsi]
sims = sorted(enumerate(sims), key=lambda item: -item[1])

sims = sims[:5]
for doc_id, sim in sims:
    print doc_id, document_song_mapping[doc_id], sim

lsi.print_topics(5)
#print affection_lsi
#print lsi[corpus[15]]
#print sims
#
#print index
#sims = index[tfidf[corpus[0]]]
#print(list(enumerate(sims)))
#for word_id, weight in affection:
#    print inverted_dict[word_id], weight