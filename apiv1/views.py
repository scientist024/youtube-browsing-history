from django.db import models
from django.db.models import query
from rest_framework import viewsets

from .models import Movie, Streamer
from .serializers import MovieSerializer, StreamerSerializer

class StreamerViewSet(viewsets.ModelViewSet):
    serializer_class = StreamerSerializer
    queryset = Streamer.objects.order_by('name')

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.order_by('-watched_date')