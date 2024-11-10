from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.list_books, name='bookList'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),

    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),

    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),

]
