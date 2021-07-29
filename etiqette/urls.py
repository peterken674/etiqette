from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('movie/<movie_id>/', views.single_movie, name='movie'),
    path('cinema/', views.single_cinema, name='cinema'),
    path('book/', views.book_ticket, name='book'),
]