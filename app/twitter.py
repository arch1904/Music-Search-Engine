import json
import tweepy
import sys
reload(sys)
sys.setdefaultencoding('utf8')
f= open('../Twitter_Keys.txt','r')
key1=f.readline().strip('\n')
key2=f.readline().strip('\n')
key3=f.readline().strip('\n')
key4=f.readline().strip('\n')
def get_authenticated_API():
    auth = tweepy.OAuthHandler(key1, key2)
    auth.set_access_token(key3,key4)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

api = get_authenticated_API()

def search(query):
    l=""   
    for tweet in tweepy.Cursor(api.search, q=query).items(20):
        l+=tweet.text+'/<br/>'
    return l

print search('Eminem')