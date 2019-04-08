from django.conf.urls import url
from . import views

app_name = 'Home'
urlpatterns = [
    # /home/
    url(r'^$', views.index.as_view(), name="index"),

    # /home/album-store
    url(r'^album-store/$', views.albumstore.as_view(), name="albums-store"),

    url('add_album/', views.AlbumAddView.as_view(), name='AddAlbum'),

    url(r'^(?P<pk>[0-9]+)/$', views.AlbumView.as_view(), name='AlbumView'),

    url(r'^(?P<pk>[0-9]+)/$', views.ArtistView.as_view(), name='ArtistView'),

    url(r'^(?P<pk>[0-9]+)/update/$', views.AlbumUpdateView.as_view(), name='UpdateAlbum'),

    url(r'^del/(?P<pk>[0-9]+)/$', views.AlbumDeleteView.as_view(), name='DeleteAlbum'),

    url(r'^(?P<pk>[0-9]+)/add song/$', views.SongAddView.as_view(), name='AddSong'),

    url('album/(?P<pk>[0-9]+)/delete', views.SongDeleteView.as_view(), name='DeleteSong'),

    url('album/(?P<pk>[0-9]+)/update/', views.SongUpdateView.as_view(), name='UpdateSong'),

    url(r'contact/$', views.contact, name='contact'),

    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
