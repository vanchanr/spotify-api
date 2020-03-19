import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def pprint(jsonObj):
    print(json.dumps(jsonObj, indent=2))

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + config['auth']['bearerToken']
}

with open('Singer.json', 'r') as f:
    singerDSP = json.load(f)

url = "https://api.spotify.com/v1/search/"
albumIds = set()
for item in singerDSP[::-1]:
    params = {
        "q": item['Film'],
        "type": "album",
        "market": "IN",
        "limit": 10
    }
    response = requests.get(url, params=params, headers=headers).json()
    results = response['albums']['items']
    for result in results:
        if(result['artists'][0]['name'] == "Devi Sri Prasad"):
            albumIds.add(result['id'])
            break

url = "https://api.spotify.com/v1/albums/{}/tracks"
dspUris = []
for albumId in albumIds:
    response = requests.get(url.format(albumId), params={}, headers=headers).json()
    for track in response['items']:
        for artist in track['artists']:
            if (artist['name'] == "Devi Sri Prasad"):
                dspUris.append(track['uri'])
                break

url = "https://api.spotify.com/v1/me/playlists"
playlistName = "Singer Devi"
response = requests.post(url, json={"name": playlistName}, headers=headers).json()
playlistId = response['id']

url = "https://api.spotify.com/v1/playlists/{}/tracks"
requests.post(url.format(playlistId), json={"uris": dspUris}, headers=headers)