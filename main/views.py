from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Books
from .forms import BookForm, LoginForm
from .rent import confirm_rent_database
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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
	global book_list
	error = False
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			isbn = form.cleaned_data['book_isbn']
			try:
				book = Books.objects.get(book_isbn=isbn)
				if book.borrowid:
					message = '這本書已被{}借出, 請選擇其他書籍'.format(book.borrowid)
				else:
					book_list.append(book)
					message = '請輸入有效的ISBN'
			except:
				message = ''
			form = BookForm()
	else:
		form = BookForm()
	return render(request, 'main/rent.html', {'form':form, 'book_list':book_list, 'message':message})

def confirm_rent(request):
	global book_list
	if request.method == 'POST':
		confirm_rent_database(book_list, request.user.username)

	return render(request, 'main/rent_confirm.html', {'book_list':book_list})

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
	global book_list
	book_list = []
	logout(request)
	return HttpResponseRedirect('/book/')
def registerview(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/book/')
	else:
		form = UserCreationForm()
	return render(request, 'main/register.html', {'form':form})
