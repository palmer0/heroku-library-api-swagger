from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status

from api_books.models import Author, Book
from api_books.views import index

import json


class LibraryAPIBaseTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

        super(LibraryAPIBaseTestCase, self).setUp()

    @classmethod
    def setUpClass(cls):
        super(LibraryAPIBaseTestCase, cls).setUpClass()

        cls.author = Author.objects.create(
            first_name='James',
            last_name='Cook'
        )

        cls.book = Book.objects.create(
            title='Test Book',
            author=cls.author,
            isbn='1234567890123',
            published='2016-11-13'
        )


class IndexViewTestCase(LibraryAPIBaseTestCase):

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses
        the correct template
        """
        request = self.factory.get("/api/v1/docs/")
        with self.assertTemplateUsed('api_books/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

class AuthorsAPITestCase(LibraryAPIBaseTestCase):

    def test_AuthorViewSet_returns_authors(self):
        """
        Test that API returns a list of all authors and a 200 response.
        """
        response = self.client.get('/api/v1/authors')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['first_name'], 'James')
        self.assertEqual(response.data[0]['last_name'], 'Cook')

    def test_AuthorViewSet_creates_an_author(self):
        """
        Test that API can create an author and returns a 201 response.
        """
        data = {
            'first_name': 'John',
            'last_name': 'Fisher'
        }
        response = self.client.post('/api/v1/authors', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_AuthorViewSet_does_not_create_an_author_with_blank_fields(self):
        """
        Test that API returns a 400 response and required fields.
        """
        data = {}
        response = self.client.post('/api/v1/authors', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            'first_name': ['This field is required.'],
            'last_name': ['This field is required.']
        })


    def test_AuthorViewSet_returns_an_author(self):
        """
        Test that API can return an author
        and returns a 200 response.
        """
        response = self.client.get('/api/v1/authors/1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_AuthorViewSet_does_not_return_a_not_existing_author(self):
        """
        Test that API returns a 404 response.
        """
        response = self.client.get('/api/v1/authors/2')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'author': 'Not Found'})

    def test_AuthorViewSet_updates_an_author(self):
        """
        Test that API can update an author
        and returns a 200 response.
        """
        data = {
            'first_name': 'Peter',
            'last_name': 'Cameron'
        }
        response = self.client.put('/api/v1/authors/1', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_AuthorViewSet_does_not_update_author_with_blank_fields(self):
        """
        Test that API returns a 400 response and required fields.
        """
        data = {}
        response = self.client.put('/api/v1/authors/1', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            'first_name': ['This field is required.'],
            'last_name': ['This field is required.']
        })

    def test_AuthorViewSet_does_not_update_author_with_incorrect_body_format(self):
        """
        Test that API returns a 400 response.
        """
        data = {
            'first_name': 'Lewis',
            'last_name': 'Brown'
        }
        response = self.client.put('/api/v1/authors/hi', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'body': 'Incorrect format'})

    def test_AuthorViewSet_does_not_update_if_author_not_exists(self):
        """
        Test that API returns 404 response.
        """
        data = {
            'first_name': 'Peter',
            'last_name': 'Cameron'
        }
        response = self.client.put('/api/v1/authors/2', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'author': 'Not Found'})

    def test_AuthorViewSet_deletes_an_author(self):
        """
        Test that API can delete an author and returns a 204 response.
        """
        response = self.client.delete('/api/v1/authors/1', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, {'author': 'Succesfully deleted!'})

    def test_AuthorViewSet_does_not_delete_an_author_if_not_exists(self):
        """
        Test that API returns a 404 response.
        """
        response = self.client.delete('/api/v1/authors/2', format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data,{'author':'Not Found'})


class BooksAPITestCase(LibraryAPIBaseTestCase):

    def test_BookViewSet_returns_books(self):
        """
        Test that API returns a list of all books and a 200 response.
        """
        response = self.client.get('/api/v1/books')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['title'], 'Test Book')
        self.assertEqual(response.data[0]['author']['first_name'], 'James')
        self.assertEqual(response.data[0]['author']['last_name'], 'Cook')
        self.assertEqual(response.data[0]['isbn'], '1234567890123')
        self.assertEqual(response.data[0]['published'], '2016-11-13')

    def test_BookViewSet_creates_a_book_with_existing_author(self):
        """
        Test that API can create a book and returns a 201 response.
        """
        data = {
            'title': 'Book Test',
            'author': 1,
            'isbn': '9876543210321',
            'published': '2016-11-21'
        }
        response = self.client.post('/api/v1/books', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_BookViewSet_does_not_create_a_book_without_author_field(self):
        """
        Test that API returns 400 response and required field.
        """
        data = {
            'title': 'Book Test',
            'isbn': '9876543210321',
            'published': '2016-11-21'
        }
        response = self.client.post('/api/v1/books', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'author':'Field required'})

    def test_BookViewSet_does_not_create_a_book_with_incorrect_body_format(self):
        """
        Test that API returns a 400 response.
        """
        data = {
            'title': 'Book Test',
            'author': 'Test',
            'isbn': '9876543210321',
            'published': '2016-11-21'
        }
        response = self.client.post('/api/v1/books', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'body': 'Incorrect format'})

    def test_BookViewSet_does_not_create_a_book_with_blank_or_incorrect_data(self):
        """
        Test that API returns 400 response and required or incorrect fields.
        """
        data = {
            'author': 1,
            'published': '2013/04/16'
        }
        response = self.client.post('/api/v1/books', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "title": ["This field is required."],
            "isbn": ["This field is required."],
            "published": [
                "Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]]."
            ]
        })

    def test_BookViewSet_does_not_create_a_book_without_existing_author(self):
        """
        Test that API returns 404 response.
        """
        data = {
            'title': 'Green Book',
            'author': 3,
            'isbn': '1234567890123',
            'published': '2016-11-22'
        }
        response = self.client.post('/api/v1/books', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'author':'Not Found'})

    def test_BookViewSet_creates_a_book_and_author(self):
        """
        Test that API can create a book and returns a 201 response.
        """
        author = Author.objects.create(
            first_name='Lisa',
            last_name='Cook'
        )

        data = {
            'title': 'Book Test',
            'author': {
                'first_name': author.first_name,
                'last_name': author.last_name
            },
            'isbn': '9876543210321',
            'published': '2016-11-21'
        }
        response = self.client.post('/api/v1/books/createBookAndAuthor', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_BookViewSet_does_not_create_a_book_and_author_if_author_not_exists(self):
        """
        Test that API returns a 400 response.
        """
        data = {
            'title': 'Book Test',
            'isbn': '9876543210321',
            'published': '2016-11-21'
        }
        response = self.client.post('/api/v1/books/createBookAndAuthor', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'body':'Incorrect format'})

    def test_BookViewSet_does_not_create_a_book_and_author_if_author_data_is_not_correct(self):
        """
        Test that API returns a 400 response.
        """
        data = {
            'title': 'Book Test',
            'author': {
                'first_name': 'John'
            },
            'isbn': '9876543210321',
            'published': '2016-11-21'
        }
        response = self.client.post('/api/v1/books/createBookAndAuthor', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"last_name": ["This field is required."]})

    def test_BookViewSet_does_not_create_a_book_and_author_if_book_data_is_not_correct(self):
        """
        Test that API returns a 400 response.
        """
        data = {
            'title': 'Book Test',
            'author': {
                'first_name': 'John',
                'last_name': 'Murray'
            },
            'published': '2016-11-21'
        }
        response = self.client.post(
            '/api/v1/books/createBookAndAuthor',
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"isbn": ["This field is required."]})

    def test_BookViewSet_returns_a_book(self):
        """
        Test that API can return a book and returns a 200 response.
        """
        response = self.client.get('/api/v1/books/1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_BookViewSet_does_not_return_a_book_if_not_exists(self):
        """
        Test that API returns a 404 response.
        """
        response = self.client.get('/api/v1/books/2')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'book': 'Not Found'})

    def test_BookViewSet_updates_a_book(self):
        """
        Test that API can update a book and returns a 200 response.
        """
        data = {
            'title': 'First Book',
            'author': 1,
            'isbn': '5463210792463',
            'published': '2000-11-24'
        }
        response = self.client.put('/api/v1/books/1', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_BookViewSet_does_not_update_a_book_without_author_field(self):
            """
            Test that API returns 400 response and required field.
            """
            data = {
                'title': 'First Book',
                'isbn': '5463210792463',
                'published': '2000-11-24'
            }
            response = self.client.put('/api/v1/books/1', data, format='json')

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(response.data, {'author': 'Field required'})

    def test_BookViewSet_does_not_update_a_book_with_blank_or_incorrect_data(self):
        """
        Test that API returns 400 response and required or incorrect fields.
        """
        data = {
            'author': 1,
            'published': '2013/04/16'
        }
        response = self.client.put('/api/v1/books/1', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "title": ["This field is required."],
            "isbn": ["This field is required."],
            "published": [
                "Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]]."
            ]
        })

    def test_BookViewSet_does_not_update_a_book_with_incorrect_body_format(self):
        """
        Test that API returns 400 response.
        """
        data = {
            'title': 'First Book',
            'author': 'hi',
            'isbn': '5463210792463',
            'published': '2000-11-24'
        }
        response = self.client.put('/api/v1/books/1', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'body': 'Incorrect format'})

    def test_BookViewSet_does_not_update_a_book_if_not_exists(self):
        """
        Test that API returns 404 response.
        """
        data = {
            'title': 'First Book',
            'author': 1,
            'isbn': '5463210792463',
            'published': '2000-11-24'
        }
        response = self.client.put('/api/v1/books/20', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'book': 'Not Found'})

    def test_BookViewSet_does_not_update_a_book_without_existing_author(self):
        """
        Test that API returns 404 response.
        """
        data = {
            'title': 'First Book',
            'author': 4,
            'isbn': '5463210792463',
            'published': '2000-11-24'
        }
        response = self.client.put('/api/v1/books/1', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'author':'Not Found'})

    def test_BookViewSet_deletes_a_book(self):
        """
        Test that API can delete a book and returns a 204 response.
        """
        response = self.client.delete('/api/v1/books/1', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_BookViewSet_does_not_delete_a_book_if_not_exists(self):
        """
        Test that API returns a 404 response.
        """
        response = self.client.delete('/api/v1/books/2', format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'book': 'Not Found'})
