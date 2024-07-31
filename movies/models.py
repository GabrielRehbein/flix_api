from django.db import models
from actors.models import Actor
from genres.models import Genre
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.PositiveIntegerField(blank=True, null=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name