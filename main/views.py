from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Books
from .forms import NameForm
book_list = []
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'main/index.html'
	context_object_name = 'all_book_list' #the list name of book list in html

	def get_queryset(self):
		"""Return all books in datebase"""
		return Books.objects.all()

def rent(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			book = Books.objects.get(book_isbn=request.POST['book_isbn'])
			book_list.append(book)
			print(book_list)

	else:
		form = NameForm()
	return render(request, 'main/rent.html', {'form':form, 'book_list':book_list})

def detail(request, books_id):
	book = get_object_or_404(Books, pk=books_id) # use book_id as a url
	return render(request, 'main/detail.html', {'book': book}) #return a dict contain book's date


# def create(request):
# 	if request.method == 'POST':
# 		form = ArticleForm(request.POST)
# 		if form.is_valid():
# 			new_article = form.save()
# 			return HttpResponceRedirect('/main/' + str(new_article.pk))
# 		form = ArticleForm()
# 		return render(request, 'create_article.html')
