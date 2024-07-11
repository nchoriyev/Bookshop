from django.contrib import admin
from .models import Savat
from import_export.admin import ImportExportModelAdmin

@admin.register(Savat)
class SavatAdmin(ImportExportModelAdmin):
    list_display = ('user', 'book', 'slug', 'title','shipping_date', 'count_orders', 'created_at')
    list_display_links = ('user', 'book', 'slug', 'title', 'shipping_date', 'count_orders', 'created_at')
    search_fields = ('book', 'title')
    ordering = ('-created_at',)
    prepopulated_fields = {"slug": ("title",)}