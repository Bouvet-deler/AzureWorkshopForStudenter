import azure.functions as func
import logging
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def show_dancesongs_in_playlist(playlist, sp):
    dance_playlist =  []
    for i in range(len(playlist["items"])): #Iterating over the playlist to get the tracks
        track = playlist["items"][i]
        track_uri = track["track"]["uri"]
        audio_features = sp.audio_features(track_uri)[0]
        danceability = audio_features["danceability"] # A value of 0.0 is least danceable and 1.0 is most danceable.
        if danceability > 0.75: #find the highest danceability songs
            artist_name = track["track"]["artists"][0]["name"]
            track_name = track["track"]["name"]
            track_id = sp.audio_features(track_uri)[0]["id"]
            dance_playlist.append([artist_name, track_name, track_id])
    return dance_playlist
    

# make prettier
def write_to_playlist(playlist):
    html_string = "<html>\n<head>\n<title>Danceability Playlist with URI</title>\n</head>\n<body>\n<h1>Danceability playlist with URI</h1>\n"
    for item in playlist:
        html_string += f"<p>{str(item)}</p>\n"

    html_string += "</body></html>"
    return html_string


@app.route(route="spotify")
def spotify(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Running the spotify function')

    client_id = "CLIENT_ID" # client id
    client_secret = "CLIENT_SECRET" # client secret
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id, client_secret=client_secret, scope=scope, redirect_uri='REDIRECT_URI'))

    liked_songs_playlist = sp.current_user_saved_tracks() # Get useres current liked songs
    dance_playlist = show_dancesongs_in_playlist(liked_songs_playlist, sp)
    #return func.HttpResponse(f"{dance_playlist}", status_code=200) 

    # ------ To make prettier -------
    prettier_dance_playlist = write_to_playlist(dance_playlist)
    return func.HttpResponse(f"{prettier_dance_playlist}", mimetype='.html', status_code=200 ) 
    # ------------------
