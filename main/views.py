from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Books
from .forms import BookForm, LoginForm
from .rent import confirm_rent_database
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
	message = ''
	error = False
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			isbn = form.cleaned_data['book_isbn']
			form = BookForm()
			try:
				book = Books.objects.get(book_isbn=isbn)
				if book.book_borrowid :
					message = '這本書已被{}借出, 請選擇其他書籍'.format(book.book_borrowid)
					messages.warning(request, message, extra_tags='alert')
				else:
					book_list.append(book)
			except:
				message = '請輸入有效的ISBN'
				messages.warning(request, message, extra_tags='alert')
	else:
		form = BookForm()
	return render(request, 'main/rent.html', {'form':form, 'book_list':book_list})
@login_required(login_url='/login/')
def rent_confirm(request):
	global book_list
	print(len(book_list))
	if len(book_list) <= 1:
		messages.error(request, '請先借閱書籍', extra_tags='alert')
		return render(request, 'main/rent_confirm.html')
	borrow_list = list(book_list)
	book_list = []
	confirm_rent_database(book_list, request.user.username)
	messages.success(request, '借閱成功', extra_tags='alert')
	return render(request, 'main/rent_confirm.html', {'book_list':borrow_list})

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
