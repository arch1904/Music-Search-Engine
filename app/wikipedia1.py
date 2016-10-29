import wikipedia
import json
import urllib2

def wiki(query):
	stuff = ""
	wiki_search = wikipedia.summary(query)
	return wiki_search
