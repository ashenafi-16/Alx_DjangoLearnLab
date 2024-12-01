from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', ListView.as_view(), name='list-view'),  
    path('books/<int:pk>/', DetailView.as_view(), name='detail-view'),  
    path('books/create/', CreateView.as_view(), name='create-view'),  
    path('books/<int:pk>/books/update/', UpdateView.as_view(), name='update-view'), 
    
    path('books/<int:pk>/books/delete', DeleteView.as_view(), name='delete-view'), 
]