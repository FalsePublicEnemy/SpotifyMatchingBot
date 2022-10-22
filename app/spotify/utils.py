import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from app.spotify.config import SCOPES


def get_auth(username: str) -> str:
    return SpotifyOAuth(
        redirect_uri=os.environ['SPOTIPY_REDIRECT_URI'],
        username=username,
        scope=SCOPES,
        open_browser=True,
    )


def get_client(username: str):
    auth_manager = get_auth(username)
    return spotipy.Spotify(oauth_manager=auth_manager)
