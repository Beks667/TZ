from rest_framework import viewsets
from .models import Albums
from .serializers import AlbumsSerializer


class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

