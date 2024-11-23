from django.urls import path,include
from .import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'books_all', views.BookViewSet)

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]