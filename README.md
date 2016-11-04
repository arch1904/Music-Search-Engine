# Music Search Engine Project

## Goal
Create a music search engine with the following that allows users to query an artist/song. Must have the following:

1) Wikipedia excerpt<br>
2) Spotify Playlist<br>
3) Twitter tweets about artist<br>
4) Recommendation System<br>

##GET
http://localhost:5000/search?q=(search query) <br>
| Request Parameter   | Value Type | Value                                                    |   
|---------------------|------------|----------------------------------------------------------|
| Artist or Song Name | String     | Wikipedia Summary, Playlist, Tweets and Reccommendations |   
 
##RESPONSE

| Response                                             | Value Type | Value                                                    |
|------------------------------------------------------|------------|----------------------------------------------------------|
| Artist Summary, Tweets Recommendations, and Playlist | String     | Wikipedia Summary, Playlist, Tweets and Reccommendations |
