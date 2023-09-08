from django.contrib import admin
from .models import Executor


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    pass
# Register your models here.
