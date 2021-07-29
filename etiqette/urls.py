from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('movie/', views.single_movie, name='movie'),
    path('cinema/', views.single_cinema, name='cinema'),
]