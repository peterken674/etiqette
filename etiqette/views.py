from django.shortcuts import render
from .request import get_movies, get_movie
from django.conf import settings
from . import models

def index(request):

    sessions = models.Session.objects.all()

    context = {'sessions':sessions}

    return render(request, 'etiqette/index.html', context)

def single_movie(request, session_id):

    session = models.Session.objects.get(id=session_id)
    cinemas = models.Cinema.objects.all()
    sessions = models.Session.objects.filter(movie_id=session.movie_id)
    context = {
        'session':session,
        'cinemas':cinemas,
        'sessions':sessions,
    }

    return render(request, 'etiqette/movie.html', context)

def single_cinema(request):

    movies = get_movies('now_playing')

    context = {'movies':movies}

    return render(request, 'etiqette/cinema.html', context)

def book_ticket(request):

    return render(request, 'etiqette/book.html')



