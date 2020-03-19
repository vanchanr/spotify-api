## *scopes*
    user-library-read  
    user-library-modify  
    user-top-read  
    user-follow-read  
    user-follow-modify  
    user-read-playback-state  
    user-read-currently-playing  
    user-read-recently-played  
    user-read-privateuser-read-email  
    user-modify-playback-state  
    playlist-read-private  
    playlist-read-collaborative  
    playlist-modify-public  
    playlist-modify-private  

## *objects*
    AlbumObject  
    ArtistObject  
    AudioFeaturesObject  
    CategoryObject  
    ContextObject  
    CurrentlyPlayingObject  
    CursorObject  
    CursorPagingObject  
    DeviceObject  
    DevicesObject  
    ExternalIdObject  
    PagingObject  
    PlayHistoryObject  
    PlaylistObject  
    PlaylistTrackObject  
    PrivateUserObject  
    PublicUserObject  
    RecommendationSeedObject  
    RecommendationsResponseObject  
    SavedAlbumObject  
    SavedTrackObject  
    SimplifiedAlbumObject  
    SimplifiedTrackObject  
    TrackObject  
    TuneableTrackObject  

### PublicUserObject  
```python
url = "https://api.spotify.com/v1/users/du3mgfx147m71ptm0uvet8gj9"
pprint(requests.get(url, params={}, headers=headers).json())

{
  "display_name": "vanchanr",
  "external_urls": {
    "spotify": "https://open.spotify.com/user/du3mgfx147m71ptm0uvet8gj9"
  },
  "followers": {
    "href": null,
    "total": 0
  },
  "href": "https://api.spotify.com/v1/users/du3mgfx147m71ptm0uvet8gj9",
  "id": "du3mgfx147m71ptm0uvet8gj9",
  "images": [],
  "type": "user",
  "uri": "spotify:user:du3mgfx147m71ptm0uvet8gj9"
}
```

### PrivateUserObject 
```python
url = "https://api.spotify.com/v1/me"
pprint(requests.get(url, params={}, headers=headers).json())

{
  "country": "IN",
  "display_name": "vanchanr",
  "email": "rahul.vanchanagiri@gmail.com",
  "explicit_content": {
    "filter_enabled": false,
    "filter_locked": false
  },
  "external_urls": {
    "spotify": "https://open.spotify.com/user/du3mgfx147m71ptm0uvet8gj9"
  },
  "followers": {
    "href": null,
    "total": 0
  },
  "href": "https://api.spotify.com/v1/users/du3mgfx147m71ptm0uvet8gj9",
  "id": "du3mgfx147m71ptm0uvet8gj9",
  "images": [],
  "product": "open",
  "type": "user",
  "uri": "spotify:user:du3mgfx147m71ptm0uvet8gj9"
}
```