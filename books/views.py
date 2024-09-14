from django.shortcuts import render
from rest_framework import viewsets

from books.models import Book
from .serialiazers import BookSerializer  
# Create your views here.


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



def books(request):
    books = Book.objects.all()
    return render(request,'books.html',{'books':books})