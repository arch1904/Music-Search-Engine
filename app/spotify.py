import spotipy

spotify=spotipy.Spotify()

def get_playlist(query):
	str1=""
	results=spotify.search(q=query,type='playlist')
	str1=results[u'playlists'][u'items'][2][u'external_urls'][u'spotify']
	return str1

