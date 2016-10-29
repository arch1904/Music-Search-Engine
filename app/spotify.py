import spotipy
import json


spotify=spotipy.Spotify()

def search_track(query):
	results=spotify.search(q=query,type='track')
	str1=json.dumps(results)
	return str1

def search_artist(query):
	results=spotify.search(q=query,type='artist')
	str1=json.dumps(results)
	return str1

