from __future__ import unicode_literals

from django.test import TestCase
from api_books.models import Book, Author


class LibraryAPIModelBaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(LibraryAPIModelBaseTestCase, cls).setUpClass()

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

class AuthorAPIModelTestCase(LibraryAPIModelBaseTestCase):

    def test_author_model(self):
        """
        Test that all author data is correct.
        """
        self.assertEqual(self.author.first_name, 'James')
        self.assertEqual(self.author.last_name, 'Cook')

    def test_str_object_author(self):
        """
        Test string function of author.
        """
        self.assertEqual(str(self.author), 'James Cook')


class BookAPIModelTestCase(LibraryAPIModelBaseTestCase):

    def test_book_model(self):
        """
        Test that all book data is correct.
        """
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author.first_name, 'James')
        self.assertEqual(self.book.author.last_name, 'Cook')
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.published, '2016-11-13')

    def test_str_object_book(self):
        """
        Test string function of book.
        """
        self.assertEqual(str(self.book), 'Test Book')
