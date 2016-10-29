from flask import Flask, request
from app import app
import twitter
import spotify
# static url
@app.route('/')
def index():
    return None

# api with endpoint for hashtag
@app.route('/hashtag', methods=['GET'])
def hashtag():
    l=[]
    if 'hash' in request.args:
        return twitter.search('hash')
    return "Wrong!"

#api with endpoint for KeyWord
@app.route('/word', methods=['GET'])
def key_word():
    l=[]
    if 'word' in request.args:
        return twitter.search('word')
    return "Wrong!"

#api with endpoint for GeoLocation
@app.route('/location', methods=['GET'])
def location():
    l=[]
    if 'location' in request.args:
        return twitter.search('location')
    return "Wrong"

@app.route('/playlist',methods=['GET'])
def playlist():
    l=[]
    if 'artist' in request.args:
        return spotify.search(artist)
    return "Wrong"

