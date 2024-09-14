from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):  # corrected class name
    class Meta:  # corrected Meta class name
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn_number']