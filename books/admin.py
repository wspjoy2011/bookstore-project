from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
