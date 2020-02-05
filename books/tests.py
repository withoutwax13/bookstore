from django.test import TestCase, Client
from django.urls import reverse

from .models import Book


class BooksAppTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title = 'title',
            author = 'author',
            price = '40.00',
            published_date = '2018-05-05',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'title')
        self.assertEqual(f'{self.book.author}', 'author')
        self.assertEqual(f'{self.book.price}', '40.00')
        self.assertEqual(f'{self.book.published_date}', '2018-05-05')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')