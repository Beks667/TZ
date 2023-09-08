from django.contrib import admin
from .models import Song,SongsAlbum


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
# Register your models here.


@admin.register(SongsAlbum)
class SongsAlbumAdmin(admin.ModelAdmin):
    pass
