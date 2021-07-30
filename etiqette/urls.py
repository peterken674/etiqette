from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('movie/<session_id>/', views.single_movie, name='movie'),
    path('cinema/', views.single_cinema, name='cinema'),
    path('book/<session_id>/', views.book_ticket, name='book'),
]