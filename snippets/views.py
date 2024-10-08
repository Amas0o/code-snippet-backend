from django.shortcuts import render

# Create your views here.
# snippets/views.py
from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
