from rest_framework import serializers
from .models import Song,SongsAlbum


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id','title','albums',)


class SongsAlbumSerializer(serializers.ModelSerializer):
    song = SongSerializer()

    class Meta:
        model = SongsAlbum
        fields = ('id','song', 'track_number','album',)