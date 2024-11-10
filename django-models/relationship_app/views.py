from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import user_passes_test


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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'relationship_app/register.html',{'form':form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, 'You are now logged in.')
            return redirect('register')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request,'relationship_app/login.html', {'form':form})

def LogoutView(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user has the 'Librarian' role
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user has the 'Member' role
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')