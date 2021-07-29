from django.db import models

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
    location = models.CharField(max_length=200, blank=True)

