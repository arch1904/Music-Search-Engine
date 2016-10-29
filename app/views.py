from flask import Flask, request
from app import app
import twitter
import spotify
import wiki_search
# static url
@app.route('/')
def index():
    return None



@app.route('/search',methods=['GET'])
def search():
    tweets=""
    wiki=""
    playlist=""
    if 'q' in request.args:
        wiki=wiki_search.search(request.args['q'])
        playlist=spotify.get_playlist(request.args['q'])
        tweets=twitter.search(request.args['q'])
        return "Summary:<br/>"+wiki+ "<br/><br/>Playlist at:<br/>"+playlist+ "<br/><br/>TWEETS:<br/>"+ tweets
    return "WRONG"


