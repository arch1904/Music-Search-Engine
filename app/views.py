from flask import Flask, request
from app import app
import twitter
import spotify
import wiki_search
# static url
@app.route('/')
def index():
    return "<h1/>Welcome to music search engine"



@app.route('/search',methods=['GET'])
def search():
    tweets=""
    wiki=""
    playlist=""
    recs=""
    if 'q' in request.args:
        wiki=wiki_search.search(request.args['q'])
        playlist="<a href="+spotify.get_playlist(request.args['q'])+">here</a>"
        tweets=twitter.search(request.args['q'])
        return "<h2/>Summary:<br/></h2/>"+wiki+ "<br/><br/><h2/>For Playlist Click "+playlist+ "</h2/><br/><br/><h2/>TWEETS:<br/></h2/>"+ tweets+"<br/><br/><h2/>RECCOMENDED FOR YOU</h2/>"+recs 
    return "WRONG"

