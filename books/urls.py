from django.urls import path

from .views import BooksListView, BookDetailView, SearchResultView

urlpatterns = [
    path('', BooksListView.as_view(), name = 'book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name = 'book_detail'),
    path('search/', SearchResultView.as_view(), name = 'search_results'),
]