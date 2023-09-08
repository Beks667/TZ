from django.contrib import admin
from .models import Albums


@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    pass

# Register your models here.
