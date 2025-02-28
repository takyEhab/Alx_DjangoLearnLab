from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def book_list(request):
    books = Book.objects.all()  
    return render(request, 'books/book_list.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  
        return context