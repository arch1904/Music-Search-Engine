import spotipy
import spotipy.util as util
from spotipy import oauth2

spotify=spotipy.Spotify()
'''PORT_NUMBER=5000
SPOTIPY_CLIENT_ID='14fd0be1567e4eec8c141b0057521d59'
SPOTIPY_CLIENT_SECRET='f6ac807d3ab64e00a87f363553078596'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'
sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
token_info = sp_oauth.get_cached_token()
access_token = token_info['access_token']
sp = spotipy.Spotify(access_token)

'''
def get_playlist(query):
	str1=""
	results=spotify.search(q=query,type='playlist')
	str1=results[u'playlists'][u'items'][2][u'external_urls'][u'spotify']
	return str1

def generate_recommendations(query):
	artist_list=[]
	track_list=[]
	artist=spotify.search(q=query,type='artist')
	song=spotify.search(q=query,type='track')
	temp=artist[u'artists'][u'items'][2][u'external_urls'][u'spotify']
	artist_list.append(temp)
	temp=song[u'tracks'][u'items'][2][u'external_urls'][u'spotify']
	track_list.append(temp)
	recommendation=spotify.recommendations(seed_artists=artist_list,seed_genres=[],seed_tracks=track_list,limit=20,country=None,**kwargs)
	return recommendations


#print generate_recommendations('Eminem')