from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from .my_request import get_movies, get_movie
from django.conf import settings
from . import models
import string
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from . email import send_welcome_email, send_ticket_email

def index(request):

    sessions = models.Session.objects.all()

    context = {'sessions':sessions}

    return render(request, 'etiqette/index.html', context)

def single_movie(request, session_id):

    session = models.Session.objects.get(id=session_id)
    cinemas = models.Cinema.objects.all()
    sessions = []
    context = {
        'session':session,
        'cinemas':cinemas,
        'sessions':sessions,
    }

    return render(request, 'etiqette/movie.html', context)

def single_cinema(request, cinema_id):
    cinema = models.Cinema.objects.get(id=cinema_id)
    sessions = []
    movies = []

    context = {
        'movies': movies,
        'cinema': cinema,
        'sessions':sessions
        }

    return render(request, 'etiqette/cinema.html', context)

def book_ticket(request, session_id):
    session = models.Session.objects.get(id=session_id)

    if request.method == 'POST':
        num_tickets = request.POST.get('noTickets')

        new_ticket = models.Ticket(ticket_number=generate_ticket_num(), movie_id=session.movie.movie_id, num_of_seats=num_tickets, user=request.user.profile, session=session, cinema=session.cinema)

        new_ticket.save()

        name = request.user.first_name.capitalize()
        receiver = request.user.email
        ticket = new_ticket.ticket_number
        num_seats = int(num_tickets)
        movie = get_movie(new_ticket.movie_id)

        cost = int(new_ticket.session.cost) * num_seats

        send_ticket_email(name, receiver, ticket, num_seats, cost, session, movie)


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

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUserForm()
        title = 'New Account'

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['first_name']
                email = form.cleaned_data['email']
                form.save()

                send_welcome_email(name,email)
                return redirect('login')

    context = {'r_form': form, 'title': title}
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                nxt = request.GET.get("next", None)
                url = '/auth/login/'
                if nxt is not None:
                    url += '?next=' + nxt

                return redirect(url)

            else:
                messages.info(request, 'Username or password is incorrect.')
    title = 'Login'
    context = {'title':title}
    return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')




