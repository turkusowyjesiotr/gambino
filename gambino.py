import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# both client_id and client_secret are available after setting up project on Spotify Developers Dashboard
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="{your client id here}",
                                               client_secret="{your client secret here}",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="playlist-modify-public, playlist-modify-private, user-library-read"))

username = '{your username here}'
track_ids = []
title = 1
song_title = title
offset_value = 0
song_found = False
for i in range(3006):
    if len(track_ids) == 100:
        sp.playlist_add_items(playlist_id='74VT8PisvlVMJu8rJynftd', items=track_ids)
        track_ids = []
    else:
        while song_found is not True and offset_value < 1000:
            search_result = sp.search(q="{}".format(song_title), type='track', limit=50, market="PL", offset=offset_value)
            print("offset_value equals: " + str(offset_value))
            print("song_title equals: " + str(song_title))
            for j in range(len(search_result['tracks']['items'])):
                if search_result['tracks']['items'][i]['name'] == str(song_title):
                    print(search_result['tracks']['items'][i]['name'])
                    print(search_result['tracks']['items'][i]['uri'])
                    song_uri = search_result['tracks']['items'][i]['uri']
                    just_the_uri = song_uri.replace('spotify:track:', '')
                    track_ids.append(just_the_uri)
                    print(just_the_uri)
                    print('Success!')
                    song_found = True
                    offset_value = 0
                    break
            offset_value += 50
        song_title += 1
        song_found = False
        offset_value = 0
        time.sleep(15)
        print("song_title = " + str(song_title))

sp.playlist_add_items(playlist_id='74VT8PisvlVMJu8rJynftd', items=track_ids)
