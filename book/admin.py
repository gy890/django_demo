from django.contrib import admin
from book.views import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    search_fields = ['name', 'author']  # 搜索功能
    list_filter = ['author']  # 过滤器


admin.site.register(Book, BookAdmin)
