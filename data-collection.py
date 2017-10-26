from utils import *
from config import artists

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
lyrics_folder = 'lyrics2/'

for artist in artists:
    print artist
    a = search(artist, client_access_token)
    song_infos = map(lambda t: (t[2], t[3]), a)
    os.mkdir(lyrics_folder + artist)

    for song_name, url in song_infos:
        print song_name
        lyrics = get_lyrics(url, client_access_token)
        if re.search(r"Instrumental", lyrics):
            continue
        f = open(lyrics_folder + artist + "/" + song_name, 'wb')
        f.write(lyrics.encode("utf8"))
        f.close()

