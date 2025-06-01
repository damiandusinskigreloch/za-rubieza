import requests
import spotipy
from .utils import get_all_episodes
from .utils import search_episodes

from spotipy.oauth2 import SpotifyClientCredentials  # ← TO BYŁO POTRZEBNE
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404


# Create your views here.



def search(request):

    query = request.GET.get('q', '')
    print(query)

    filtred_orginal = search_episodes(query)
    filtered = filtred_orginal[::-1]
    total_episodes = len(filtered)
    return render(request, 'finder/index.html', {'episodes': filtered, 'query': query, 'total': total_episodes})







def home(request):
    response = requests.get("https://...")
    if response.status_code != 200:
        raise Http404("Nie udało się pobrać danych z API.")

    data = response.json()
    return render(request, "index.html", {"odcinki": data})

