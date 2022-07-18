from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'


class BookDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView):

    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/search_results.html'
    # queryset = Book.objects.filter(title__icontains='beginners')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
