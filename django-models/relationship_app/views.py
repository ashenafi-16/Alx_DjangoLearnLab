from django.shortcuts import render
from .models import Book,Library
from django.views.generic import DetailView

def book_list(request):
    books = Book.objects.all()
    context = {
        'book_list':books
    }
    return render (request,'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = Book.objects.filter(library=library)
        return context
    def get_template_names(self):
        return ['templates/library_detail.html'] 