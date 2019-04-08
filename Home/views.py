from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from .models import Album , Song


class albumstore(generic.ListView):
    template_name = 'Home/albums-store.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class AlbumView(generic.DetailView):
    template_name = 'Home/DetailView.html'
    model = Album

class index(generic.ListView):
    template_name = 'Home/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class AlbumAddView(CreateView):
    model = Album
    template_name = 'Home/UploadAlbum.html'
    fields = ['name', 'artist', 'genre', 'released', 'image']
    context_object_name = 'form'
    success_url = reverse_lazy('Home:AddAlbum')


class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'Home/UploadAlbum.html'
    context_object_name = 'form'
    fields = ['name', 'artist', 'genre', 'released', 'image']
    success_message = 'Album Updated'


class AlbumDeleteView(generic.DeleteView):
    template_name = 'Home/UploadAlbum.html'
    context_object_name = 'form'
    model = Album
    success_message = 'Album deleted'
    success_url = reverse_lazy('music:HomeView')


class SongAddView(generic.CreateView):

    template_name = 'Home/UploadAlbum.html'
    context_object_name = 'form'
    model = Song
    fields = ['song_name', 'song_artist', 'duration', 'rating', 'song', 'like']
    success_message = 'Song added'

    def dispatch(self, request, *args, **kwargs):
        self.album_id = self.kwargs.get('pk')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        a = Album.objects.get(pk=self.album_id)
        form.instance.album = a
        return super(SongAddView, self).form_valid(form)


class SongDeleteView( generic.DeleteView):

    template_name = 'Home/UploadAlbum.html'
    context_object_name = 'form'
    model = Song
    success_message = 'Song deleted'
    success_url = reverse_lazy('music:HomeView')


class SongUpdateView(generic.UpdateView):

    template_name = 'Home/UploadAlbum.html'
    context_object_name = 'form'
    model = Song
    fields = ['song_name', 'song_artist', 'duration', 'rating', 'song', 'like']
    success_message = 'Song Updated'


def contact(request):
    return render(request, 'Home/contact.html')
