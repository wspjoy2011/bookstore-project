from django.contrib import admin

from .models import Book, Author, Review


class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ('id', 'title', 'price', 'get_authors')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
