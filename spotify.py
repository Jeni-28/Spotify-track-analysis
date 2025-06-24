import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='9063813afecb4d48849e49f52cbffef2',
    client_secret='0c5de184b8824bcebc2672c1b5cd851f'
))

track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)
track = sp.track(track_id)

track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': round(track['duration_ms'] / 60000, 2)
}

df = pd.DataFrame([track_data])
df.to_csv('spotify_track_data.csv', index=False)

plt.bar(['Popularity', 'Duration'], [track_data['Popularity'], track_data['Duration (minutes)']], color='skyblue')
plt.title(f"{track_data['Track Name']} Metrics")
plt.savefig("track_popularity_chart.png")
plt.show()
