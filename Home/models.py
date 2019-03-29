from django.db import models
from django.urls import reverse


class Movie(models.Model):
    movie = models.CharField(max_length=50)
    actor = models.CharField(max_length=30)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.movie


class Album(models.Model):
    artist = models.CharField(max_length=500)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('Home:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
