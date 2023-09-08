from rest_framework import serializers
from .models import Executor
from apps.albums.serializers import AlbumsSerializer


class SingerSerializer(serializers.ModelSerializer):
    albums = AlbumsSerializer(many=True,read_only=True)

    class Meta:
        model = Executor
        fields = ('id','name','albums')