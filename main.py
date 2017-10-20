from utils import *
from collections import Counter
from gensim.corpora.dictionary	import	Dictionary

artists = ["cigarettes after sex", "eric clapton", "damien rice", "dire straits", \
           "the black keys", "Eminem", "Porcupine tree", "Northlane", \
           "incubus", "radiohead"]

'''
song_name = "Lose yourself"
a = search(song_name, client_access_token)
a = a[0]
url = a[3]
lyrics = get_lyrics(url, client_access_token)
lyrics = clean_lyrics(lyrics)
f = open('lose-yourself', 'wb')
f.write(lyrics.encode("utf8"))
f.close()
'''
client_access_token = "wP-X9-H4IzwidnKGW7-zqd6ARMlJpisjYSi-OQpVi_gEyfmKRNfDjJUjJs6f8ZCu"

tokenized_lyrics = []
for artist in artists:
    print artist
    a = search(artist, client_access_token)
    song_infos = map(lambda t: (t[2], t[3]), a)
    os.mkdir('lyrics/' + artist)

    for song_name, url in song_infos:
        print song_name
        lyrics = get_lyrics(url, client_access_token)
        f = open('lyrics/' + artist + "/" + song_name, 'wb')
        f2 = open('lyrics/' + artist + "/" + song_name + "-cleaned", 'wb')
        f.write(lyrics.encode("utf8"))
        lyrics = clean_raw_data(lyrics)
        f2.write(lyrics.encode("utf8"))

        tokens = text_preprocessing(lyrics)
        tokenized_lyrics.append(tokens)

        f.close()
        f2.close()

dictionary = Dictionary(tokenized_lyrics)
print dictionary.token2id
#bow_simple = Counter(tokens)
#print(bow_simple.most_common(10))

#print tokens
#print len(tokens)