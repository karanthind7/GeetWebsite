from django.contrib import admin
from .models import Album, Song

from .models import Movie

admin.site.register(Movie)
admin.site.register(Album)
admin.site.register(Song)
