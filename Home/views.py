from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from .models import Album


class punjabi(generic.ListView):
    template_name = 'Home/punjabi.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class albumstore(generic.ListView):
    template_name = 'Home/albums-store.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class index(generic.ListView):
    template_name = 'Home/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class AddCreate(CreateView):
    model = Album

    fields = ['artist', 'album_title', 'genre', 'logo']

    success_url = reverse_lazy('Home:index')


class AlbumUpdate(UpdateView):
    model = Album

    fields = ['artist', 'album_title', 'genre', 'logo']


class AlbumDelete(DeleteView):
    model = Album

    success_url = reverse_lazy('Home:index')


# def index(request):
#     return render(request, 'Home/index.html')
#
# def login(request):
#     return render(request, 'Home/login.html')

def album_punjabi(request):
    return render(request, 'Home/punjabi.html')


def album_hindi(request):
    return render(request, 'Home/album_hindi.html')


def album_english(request):
    return render(request, 'Home/album_english.html')
