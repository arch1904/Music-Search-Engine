import wikipedia
import json
import urllib2
class wiki:
	def __init__(self):
		wiki_search=""
	def search(self,query):
		wiki_search = wikipedia.summary(query)
		return wiki_search
