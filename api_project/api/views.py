from django.shortcuts import render
from rest_framework import generics,viewsets,permissions
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-author')
    serializer_class = BookSerializer
