from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import genre, actor, contents, video
from .serializers import ContentsSerializer

class contents_list(generics.ListCreateAPIView):
    queryset = contents.objects.all()
    serializer_class = ContentsSerializer
