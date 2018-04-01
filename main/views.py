from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Books
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'all_book_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Books.objects.all()

def detail(request, books_id):
    book = get_object_or_404(Books, pk=books_id)
    return render(request, 'main/detail.html', {'book': book})

def book(request, book_id):
	pass
