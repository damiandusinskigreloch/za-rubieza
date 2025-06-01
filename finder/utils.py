from spotipy import Spotify

from spotipy.oauth2 import SpotifyClientCredentials  # ← TO BYŁO POTRZEBNE
from django.http import HttpResponse


def get_all_episodes(sp, podcast_id):
    episodes = []
    limit = 50
    offset = 0

    while True:
        response = sp.show_episodes(podcast_id, limit = limit, offset = offset)
        episodes.extend(response['items'])

        if response['next'] is None:
            break
        offset += limit

    return episodes


def search_episodes(query):
    sp = Spotify(auth_manager=SpotifyClientCredentials(
        client_id='8e82f12f9f0b412d9ba605cb58841615',
        client_secret='87d1f2989aab46c9bfbc0fc4d50d9fac'
    ))
    podcast_id = '7mYVKGQdIPmuwzfH7ySUQ4'
    episodes = get_all_episodes(sp, podcast_id)
    if query:
        query = query.lower().strip()
        filtered = [ep for ep in episodes if query in ep['name'].lower()]
    else:
        filtered = []


    return filtered 

