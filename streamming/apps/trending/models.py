from django.db import models
from apps.movies.models import Movies


class Trending(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    star = models.BooleanField()