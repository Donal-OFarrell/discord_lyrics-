import requests 
import json 



def ping_musix(artist_name,track_name):
    ''' 
    pings the musixmatch db for song lyrics
    thanks again to https://github.com/iannase/musixmatch-python-api/blob/master/lyrics.py 
    for api query syntax
    '''
    base_url = "https://api.musixmatch.com/ws/1.1/"
    lyrics_matcher = "matcher.lyrics.get"
    format_url = "?format=json&callback=callback"
    artist_search_parameter = "&q_artist="
    artist_name = artist_name.title()
    track_search_parameter = "&q_track="
    track_name=track_name.title()
    api_key = "&apikey=9bca67959d247006cf9e67a435f59c1b"
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    request = requests.get(api_call)
    
    data = request.json()
    
    status= data['message']['header']['status_code'] # status is located here in JSONic type nested data
    

    if status == 404: # if the url for those lyrics don't exist 
        return 'error' # return an error
    else:
        lyrics = data['message']['body']['lyrics']['lyrics_body'] # otherwise break into the lyrics 
        return lyrics # and return 