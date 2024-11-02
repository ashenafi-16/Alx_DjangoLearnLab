from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = [
        ("title", admin.EmptyFieldListFilter),
        ("author", admin.EmptyFieldListFilter),
        ("publication_year", admin.EmptyFieldListFilter)
    ]