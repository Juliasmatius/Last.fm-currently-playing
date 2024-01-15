import json
import requests
from config import *

def get_recent(user):
    url = f"{api_root}/?method=user.getrecenttracks&user={user}&api_key={API_KEY}&format=json&limit=1"
    request = requests.get(url)
    return json.loads(request.text)["recenttracks"]["track"][0], json.loads(request.text)

def get_song_name(data):
    return data["name"]

def get_artist(data):
    return data["artist"]["#text"]
    
def get_image_url(data):
    
    return data["image"][3]["#text"]

def get_album(data):
    return data["album"]["#text"]

def get_date(raw):
    return raw["recenttracks"]["track"][1]["date"]["uts"]
