from django.shortcuts import render
from rest_framework import viewsets
from .models import Executor
from .serializers import SingerSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = SingerSerializer

