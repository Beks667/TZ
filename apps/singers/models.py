from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=155,blank=True,null=False,verbose_name="Имя Исполнителя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
