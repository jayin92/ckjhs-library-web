from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Books
from .forms import NameForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
book_list = []
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'main/index.html'
	context_object_name = 'all_book_list' #the list name of book list in html

	def get_queryset(self):
		"""Return all books in datebase"""
		return Books.objects.all()

@login_required(login_url='/login/')
def rent(request):
	error = False
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			isbn = form.cleaned_data['book_isbn']
			error = False
			try:
				book = Books.objects.get(book_isbn=isbn)
				book_list.append(book)
			except:
				error = True
				pass
			form = NameForm()
	else:
		form = NameForm()
	return render(request, 'main/rent.html', {'form':form, 'book_list':book_list, 'error':error})

def detail(request, books_id):
	book = get_object_or_404(Books, pk=books_id) # use book_id as a url
	return render(request, 'main/detail.html', {'book': book}) #return a dict contain book's date


def loginview(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/book/')

	else:
		form = LoginForm()
	return render(request, 'main/login.html', {'form':form})
def logoutview(request):
	logout(request)
	return HttpResponseRedirect('/book/')
