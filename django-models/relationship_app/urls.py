from django.urls import path
from .views import LibraryDetailView,book_list

urlpatterns = [
    path('',book_list,name='bookList'),
    path('', LibraryDetailView.as_view(), name='library_detail'),

]