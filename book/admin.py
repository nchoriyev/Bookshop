from django.contrib import admin
from .models import Author, Book
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'created_at')
    list_display_links = ('id', 'first_name', 'last_name', 'birth_date', 'created_at')
    search_fields = ('first_name', 'last_name')
    ordering = ('created_at',)




@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    ordering = ('created_at',)
    prepopulated_fields = {"slug": ("title",)}