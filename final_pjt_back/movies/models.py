from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

class Movie(models.Model):
    adult = models.BooleanField()
    genre_ids = models.ManyToManyField(Genre)
    original_language = models.CharField(max_length=2)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    title = models.CharField(max_length=255)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    movie_id = models.IntegerField(unique=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_movies')

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    
    
    