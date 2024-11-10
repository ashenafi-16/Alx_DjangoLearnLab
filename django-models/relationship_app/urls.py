from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register
from .views import login_view
from .views import logout_view

urlpatterns = [
    path('',list_books,name='bookList'),
    path('', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name="register"),
    path('login/', login_view, name='login'),
    path('logout',logout_view, name='logout'),
]