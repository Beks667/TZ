from rest_framework import serializers
from .models import Albums
from apps.songs.serializers import SongSerializer,SongsAlbumSerializer


class AlbumsSerializer(serializers.ModelSerializer):
    songs = SongsAlbumSerializer(many=True,source='songsalbum_set')

    class Meta:
        model = Albums
        fields = ('id','album_name','release_year','singer','songs')