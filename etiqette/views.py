from django.shortcuts import render
from .request import get_movies, get_movie
from django.conf import settings

def index(request):

    movies = get_movies('now_playing')

    context = {'movies':movies}

    return render(request, 'etiqette/index.html', context)

def single_movie(request, movie_id):

    movie = get_movie(movie_id)
    context = {
        'movie':movie
    }

    return render(request, 'etiqette/movie.html', context)

def single_cinema(request):

    return render(request, 'etiqette/cinema.html')

def book_ticket(request):

    return render(request, 'etiqette/book.html')



