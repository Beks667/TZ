from rest_framework import viewsets
from .models import Song,SongsAlbum
from.serializers import SongSerializer,SongsAlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongsAlbumViewSet(viewsets.ModelViewSet):
    queryset = SongsAlbum.objects.all()
    serializer_class = SongsAlbumSerializer
