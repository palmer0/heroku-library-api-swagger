from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route

from api_books.models import Author, Book
from api_books.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, editing, retrieving and deleting authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_object(self, pk):
        """
        Override the get_object() method to return a detail error message.
        """
        try:
            author = Author.objects.get(id=pk)
            return author
        except Author.DoesNotExist:
            return Response({'author': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        """
        This method retrieves an author.
        """
        author = self.get_object(pk)

        # We check if author is an author object or a message error
        if isinstance(author, Author):
            author_serializer = AuthorSerializer(author)
            return Response(author_serializer.data, status=status.HTTP_200_OK)
        else:
            # Return the error message
            return author

    def update(self, request, pk=None):
        """
        This method updates an author.
        """
        try:
            author = self.get_object(pk)

            # We check if author is an author object or a message error
            if isinstance(author, Author):
                author_serializer = AuthorSerializer(data=request.data)
                # Checks if author request data is valid
                if author_serializer.is_valid():
                    # We can update the author
                    author.first_name = request.data['first_name']
                    author.last_name = request.data['last_name']
                    author.save()

                    author_serializer = AuthorSerializer(author)
                    return Response(author_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Return the error message
                return author
        except Exception:
            return Response({'body': 'Incorrect format'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        This method deletes an author
        """
        author = self.get_object(pk)

        # We check if author is an author object or a message error
        if isinstance(author, Author):
            author.delete()
            return Response({'author': 'Succesfully deleted!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            # Return the error message
            return author


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, editing, retrieving and deleting books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self, pk):
        """
        Override the get_object() method to return a detail error message.
        """
        try:
            book = Book.objects.get(id=pk)
            return book
        except Book.DoesNotExist:
            return Response({'book': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """
        This method creates a book.

        If author has been created previously, we only need to pass id
        parameter in author object.
        """
        try:
            # If there is no author ID in request data or there's no author
            # with supplied ID, exceptions are thrown.
            author_id = int(request.data['author'])
            author = Author.objects.get(id=author_id)
        except KeyError:
            return Response({'author': 'Field required'}, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response({'author': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'body': 'Incorrect format'}, status=status.HTTP_400_BAD_REQUEST)

        book_serializer = BookSerializer(data=request.data)
        # Checks if book request data is valid.
        if book_serializer.is_valid():
            # We can create the book and assign it the author instance
            book = Book.objects.create(
                title = request.data['title'],
                author = author,
                isbn = request.data['isbn'],
                published = request.data['published']
            )
            book_serializer = BookSerializer(book)
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        This method retrieves a book.
        """
        book = self.get_object(pk)

        # We check if book is a book object or a message error
        if isinstance(book, Book):
            book_serializer = BookSerializer(book)
            return Response(book_serializer.data, status=status.HTTP_200_OK)
        else:
            # Return the error message
            return book

    def update(self, request, pk=None):
        """
        This method updates a book.
        """
        try:
            # If there is no author ID in request data or there's no author
            # with supplied ID, exceptions are thrown.
            author_id = int(request.data['author'])
            author = Author.objects.get(id=author_id)
            book = self.get_object(pk)

            # We check if book is a book object or a message error
            if isinstance(book, Book):
                book_serializer = BookSerializer(data=request.data)
                # Checks if book request data is valid.
                if book_serializer.is_valid():
                    # We can update the book and assign it the author instance if it is
                    # changed
                    book.title = request.data['title']
                    book.author = author
                    book.isbn = request.data['isbn']
                    book.published = request.data['published']
                    book.save()

                    book_serializer = BookSerializer(book)
                    return Response(book_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Return the error message
                return book
        except KeyError:
            return Response({'author': 'Field required'}, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response({'author': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({'body': 'Incorrect format'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        This method deletes a book
        """
        book = self.get_object(pk)

        # We check if author is an author object or a message error
        if isinstance(book, Book):
            book.delete()
            return Response({'book': 'Succesfully deleted!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            # Return the error message
            return book


    @list_route(methods=['post'], url_path='createBookAndAuthor')
    def create_book_and_author(self, request):
        """
        If author hasn't been created, it creates an author passing the first
        name and last name parameters in author object.
        """
        try:
            author_serializer = AuthorSerializer(data=request.data['author'])
            # Checks if author request data is valid
            if author_serializer.is_valid():
                # We can create the author
                author = Author.objects.create(
                    first_name=request.data['author']['first_name'],
                    last_name=request.data['author']['last_name']
                )

                book_serializer = BookSerializer(data=request.data)
                # Checks if book request data is valid
                if book_serializer.is_valid():
                    # We can create the book and assign it the author instance
                    book = Book.objects.create(
                        title=request.data['title'],
                        author=author,
                        isbn=request.data['isbn'],
                        published=request.data['published']
                    )
                    # Now serialize the book object and return it
                    book_serializer = BookSerializer(book)
                    return Response(book_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'body': 'Incorrect format'}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    """
    Returns the Library API html.
    """
    return render(request, "api_books/index.html")
