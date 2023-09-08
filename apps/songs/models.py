from django.db import models
from apps.albums.models import Albums


class Song(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название Песни', blank=True,null=False)
    albums = models.ManyToManyField(Albums, through='SongsAlbum',verbose_name='Альбом')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class SongsAlbum(models.Model):
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField(verbose_name='Порядковый номер в альбоме',null=False,)

    def __str__(self):
        return f"{self.album} {self.track_number} {self.song}"

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
