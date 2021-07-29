from django.shortcuts import render

def index(request):

    return render(request, 'etiqette/index.html')

def single_movie(request):

    return render(request, 'etiqette/movie.html')

def single_cinema(request):

    return render(request, 'etiqette/cinema.html')
