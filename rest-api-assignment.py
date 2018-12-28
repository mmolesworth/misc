import json
import requests_with_caching

def get_movies_from_tastedive(movie_or_music_artist):
    baseurl = 'https://tastedive.com/api/similar'
    params = {'q' : movie_or_music_artist, 'type' : 'movies', 'limit' : 5}
    
    res = requests_with_caching.get(baseurl, params = params)
    data = json.loads(res.text)
    return data

import json
import requests_with_caching
import requests

def get_movies_from_tastedive(movie_or_music_artist):
    baseurl = 'https://tastedive.com/api/similar'
    params = {'q' : movie_or_music_artist, 'type' : 'movies', 'limit' : 5}
    
    res = requests_with_caching.get(baseurl, params = params)
    data = json.loads(res.text)
    return data

def extract_movie_titles(dict):
    return [ movie['Name'] for movie in dict['Similar']['Results'] ]

def get_related_titles(titles_list):
    results = []
    
    for title in titles_list:
        results += extract_movie_titles(get_movies_from_tastedive(title))
        
    return list(set(results))

def get_movie_data(title):
    baseurl = 'http://www.omdbapi.com/'
    params = {'t' : title, 'r' : 'json'}
    
    res = requests_with_caching.get(baseurl, params = params)
    data = json.loads(res.text)
    return data

def get_movie_rating(title):
    ratings = omdb_dict['Ratings']

    for i in ratings:
        if i['Source'] == 'Rotten Tomatoes':
            return int(i['Value'].replace('%', ''))

    return 0

def get_sorted_recommendations(titles):
    for title in titles:
        print(get_movie_data(title))



