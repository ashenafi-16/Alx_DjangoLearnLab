from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def list_books(request):
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