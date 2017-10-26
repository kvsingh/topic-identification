from config import artists
from gensim.corpora.dictionary	import	Dictionary
from utils import *
import pickle, os

#contains mapping from document id => (artist, song)
document_song_mapping = {}
tokenized_lyrics = []
token_song_mapping = {}
lyrics_folder = 'lyrics2/'
doc_id = 0

for artist in artists:
    print artist
    song_names = [x for x in os.listdir(lyrics_folder + "/" + artist) if not x.endswith("cleaned")]
    for song_name in song_names:
        f = open(lyrics_folder + artist + "/" + song_name, 'rb')
        f2 = open(lyrics_folder + artist + "/" + song_name + "-cleaned", 'wb')
        lyrics = ''
        for sentence in f.readlines():
            this_sentence = sentence.decode('utf-8')
            lyrics += this_sentence
        lyrics = clean_raw_data(lyrics)
        f2.write(lyrics.encode("utf8"))
        tokens = text_preprocessing(lyrics)
        for token in tokens:
            this_token_songs = token_song_mapping.get(token, [])
            this_token_songs.append(song_name)
            token_song_mapping[token] = this_token_songs
        tokenized_lyrics.append(tokens)
        document_song_mapping[doc_id] = (artist, song_name)
        doc_id += 1

        f.close()
        f2.close()


dictionary = Dictionary(tokenized_lyrics)
#corpus	=	[dictionary.doc2bow(doc)	for	doc	in	tokenized_lyrics]
#tfidf	=	TfidfModel(corpus)
#print dictionary.token2id
pickle.dump(dictionary, open('dictionary-2.p', "wb"))
pickle.dump(tokenized_lyrics, open('tokenized-lyrics-2.p', "wb"))
pickle.dump(document_song_mapping, open('doc-song-mapping-2.p', "wb"))
pickle.dump(token_song_mapping, open('token-song-mapping-2.p', 'wb'))