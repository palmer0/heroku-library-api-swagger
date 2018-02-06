from __future__ import unicode_literals

from rest_framework import serializers

from api_books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'created', 'updated')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'published', 'created', 'updated')
        depth = 1
