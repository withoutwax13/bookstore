from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book

class BooksListView(LoginRequiredMixin, ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'