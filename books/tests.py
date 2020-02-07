from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Book, Review


class BooksAppTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testmail@testmailservice.com',
            password = 'testpass'
        )
        self.special_permission = Permission.objects.get(codename='special_status')
        self.book = Book.objects.create(
            title = 'title',
            author = 'author',
            price = '40.00',
            published_date = '2018-05-05',
        )
        self.review = Review.objects.create(
            book = self.book,
            author = self.user,
            review = 'test review'
        )


    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'title')
        self.assertEqual(f'{self.book.author}', 'author')
        self.assertEqual(f'{self.book.price}', '40.00')
        self.assertEqual(f'{self.book.published_date}', '2018-05-05')

    def test_book_list_view_for_logged_in_users(self):
        self.client.login(username = 'testuser', password = 'testpass')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
    
    def test_book_list_view_for_logged_out_users(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/books/' % reverse('account_login'))

    def test_book_detail_view_with_permissions(self):
        self.client.login(username = 'testuser', password = 'testpass')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'test review')