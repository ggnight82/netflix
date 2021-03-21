from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Genres, Actors, Contents, Videos
from .serializers import ContentsSerializer

class contents_list(generics.ListCreateAPIView):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer
