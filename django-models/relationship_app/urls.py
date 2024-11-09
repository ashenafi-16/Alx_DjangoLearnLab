from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('',list_books,name='bookList'),
    path('', LibraryDetailView.as_view(), name='library_detail'),

]