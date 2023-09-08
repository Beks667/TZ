from django.db import models

from apps.singers.models import Executor


class Albums(models.Model):
    album_name = models.CharField(max_length=255, blank=True, null=False, verbose_name="Название Альбома")
    release_year = models.IntegerField(verbose_name="Дата Выпуска")
    singer = models.ForeignKey(Executor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.album_name} - {self.singer}"

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


