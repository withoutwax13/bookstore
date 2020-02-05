from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Book

class BooksListView(ListView):

    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'