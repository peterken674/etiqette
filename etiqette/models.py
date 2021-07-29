from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Movie:
    def __init__(self, movie_id, adult, backdrop_path, overview, poster_path, title, vote_average, vote_count, release_date, runtime, original_language, genre, trailer):
        self.movie_id = movie_id
        self.adult = adult
        self.backdrop_path = backdrop_path
        self.overview = overview
        self.poster_path = poster_path
        self.title = title
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.release_date = release_date
        self.runtime = runtime
        self.original_language = original_language
        self.genre = genre
        self.trailer = trailer

class Cinema(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    rating = models.PositiveIntegerField(null=True)
    image = CloudinaryField('images')

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_picture = CloudinaryField('images', default='image/upload/v1626430054/default_zogkvr.png')

    def __str__(self) -> str:
        return self.user.username

class Session(models.Model):
    name = models.CharField(max_length=50, blank=True)
    start_time = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return self.name

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=10)
    movie_id = models.PositiveIntegerField()
    user = models.ForeignKey(Profile, related_name='tickets', on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ticket_number

