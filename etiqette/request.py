import urllib.request,json
from .models import Movie
from django.conf import Settings, settings
from datetime import date, datetime

api_key = settings.TMDB_API_KEY
base_url = settings.MOVIE_API_BASE_URL
single_movie_url = settings.SINGLE_MOVIE_API_BASE_URL

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)      

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results


def get_movie(movie_id):
    get_movie_details_url = single_movie_url.format(movie_id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_item = json.loads(movie_details_data)

        movie_object = None
        if movie_item   :
            movie_id = movie_item.get('id')
            adult = movie_item.get('adult')
            backdrop_path = movie_item.get('backdrop_path')
            title = movie_item.get('title')
            overview = movie_item.get('overview')
            poster_path = movie_item.get('poster_path')
            vote_average = movie_item.get('vote_average')
            vote_count = movie_item.get('vote_count')
            release_date = movie_item.get('release_date')
            runtime = movie_item.get('runtime')
            original_language = movie_item.get('spoken_languages')
            genres = movie_item.get('genres')
            videos = movie_item.get('videos')

            language = original_language[0]['english_name']
            trailer_url=''
            if videos['results']:
                trailers = videos['results']
                for trailer in trailers:
                    if trailer['site']=='YouTube' and trailer['type']=='Trailer':
                        trailer_url = 'https://www.youtube.com/watch?v='+trailer['key']
                        break

            if genres:
                genre = genres[0]['name']

            release_date_obj = datetime.strptime(release_date, '%Y-%m-%d')

            movie_object = Movie(movie_id, adult, backdrop_path, overview, poster_path, title, vote_average, vote_count, release_date_obj, runtime, language, genre, trailer_url)

                

    return movie_object




def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        movie_id = movie_item.get('id')
        adult = movie_item.get('adult')
        backdrop_path = movie_item.get('backdrop_path')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster_path = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        release_date = movie_item.get('release_date')
        runtime = movie_item.get('runtime')
        original_language = movie_item.get('original_language')
        release_date_obj = datetime.strptime(release_date, '%Y-%m-%d')

        if poster_path:
            movie_object = Movie(movie_id, adult, backdrop_path, overview, poster_path, title, vote_average, vote_count, release_date_obj, runtime, original_language, [], '')
            movie_results.append(movie_object)

    return movie_results

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results