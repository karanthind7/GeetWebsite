from django.conf.urls import url
from . import views

app_name = 'Home'
urlpatterns = [
    # /home/
    url(r'^$', views.index.as_view(), name="index"),
    # /home/album_punjabi
    url(r'^album_punjabi/$', views.punjabi.as_view(), name="album_punjabi"),

    url(r'^albums-store/$', views.albumstore.as_view(), name="albums-store"),

    url(r'album_punjabi/add/$', views.AddCreate.as_view(), name='add-album'),

    url('album_hindi/', views.album_hindi),

    url('album_english/', views.album_english),

    # url('about/', views.login),

    # /music/album/add/

    #     # /home/<a.id>
    #     url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    #     # /home/<a.id>/favorite
    #     url(r'^(?P<movie_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    # music/45/
    #     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
