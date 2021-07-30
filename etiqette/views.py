from django.shortcuts import render, redirect
from .my_request import get_movies, get_movie
from django.conf import settings
from . import models
import string
import random

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

def book_ticket(request, session_id):
    session = models.Session.objects.get(id=session_id)

    if request.method == 'POST':
        num_tickets = request.POST.get('noTickets')

        new_ticket = models.Ticket(ticket_number=generate_ticket_num(), movie_id=session.movie.movie_id, num_of_seats=num_tickets, user=request.user.profile, session=session, cinema=session.cinema)

        new_ticket.save()

        return redirect('index')

    else:
        new_ticket = models.Ticket(ticket_number=generate_ticket_num())
    
    context = {
        'session':session,
        "new_ticket":new_ticket,
    }

    return render(request, 'etiqette/book.html', context)

def generate_ticket_num():
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
    return str(ran)



