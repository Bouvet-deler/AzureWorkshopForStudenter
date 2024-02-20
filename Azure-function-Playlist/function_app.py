import azure.functions as func
import logging
import datetime as dt
import json
import mimetypes
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def show_dancesongs_in_playlist(playlist, sp):
    dance_playlist =  []
    for i in range(len(playlist["items"])): #Iterating over the playlist to get the tracks
        track = playlist["items"][i]
        track_uri = track["track"]["uri"]
        danceability = sp.audio_features(track_uri)[0]["danceability"] # A value of 0.0 is least danceable and 1.0 is most danceable.
        if danceability > 0.75: #find the highest danceability songs
            artist_name = track["track"]["artists"][0]["name"]
            track_name = track["track"]["name"]
            track_id = sp.audio_features(track_uri)[0]["id"]
            dance_playlist.append([artist_name, track_name, track_id])
    return dance_playlist
    

# make prettier
def write_to_playlist(playlist):
    string_with_text = "<html>\n<head>\n<title> \nOutput Data in an HTML file\n \
           </title>\n</head> <body> <h1>Danceability playlist with Track URIs </h1>\n \
           </body></html>"
    
    for i in range(len(playlist)):
        string_with_text += "<html><p> " + str(playlist[i]) + " </p></html>"
    return string_with_text


@app.route(route="azure_function_guide")
def spotify(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Running the spotify function')

    client_id = "YOUR_CLIENT_ID" # client id
    client_secret = "YOUR_CLIENT_SECRET" # client secret
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret=client_secret, scope=scope, redirect_uri='YOUR_LOCAL_HOST'))


    
    liked_songs_playlist = sp.current_user_saved_tracks() # Get users current liked songs
    dance_playlist = show_dancesongs_in_playlist(liked_songs_playlist, sp)
    
    #return func.HttpResponse(f"{dance_playlist}", status_code=200) 
                                            


    # ------ To make prettier -------
    prettier_dance_playlist = write_to_playlist(dance_playlist)
    return func.HttpResponse(f"{prettier_dance_playlist}", mimetype='.html', status_code=200 ) 
    # ------------------