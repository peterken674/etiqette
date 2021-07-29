from django.shortcuts import render
from .request import get_movies
from django.conf import settings

def index(request):

    movies = get_movies('now_playing')

    context = {'movies':movies}

    return render(request, 'etiqette/index.html', context)

def single_movie(request):

    return render(request, 'etiqette/movie.html')

def single_cinema(request):

    return render(request, 'etiqette/cinema.html')

def book_ticket(request):

    return render(request, 'etiqette/book.html')



