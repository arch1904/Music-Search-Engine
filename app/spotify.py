import spotipy
import spotipy.util as util

spotify=spotipy.Spotify()

'''export SPOTIPY_CLIENT_ID='14fd0be1567e4eec8c141b0057521d59'
export SPOTIPY_CLIENT_SECRET='f6ac807d3ab64e00a87f363553078596'
export SPOTIPY_REDIRECT_URI='http://localhost:5000'

token = util.prompt_for_user_token('archit.941','user-library-read' )
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
	recs=spotify.recommendations(seed_artists=artist_list,seed_genres=[],seed_tracks=track_list,limit=20)
	return recs 


#print generate_recommendations('Eminem')