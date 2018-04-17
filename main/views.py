# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Books, Borrows
from .forms import BookForm, LoginForm, RegisterForm, AddBookForm
from .rent import confirm_rent_database
book_list = []
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'main/index.html'
	context_object_name = 'all_book_list' #the list name of book list in html

	def get_queryset(self):
		"""Return all books in datebase"""
		return Books.objects.all()

# def check_admin:
#    return user.is_superuser

@login_required(login_url='/login/')
def rent(request):
	global book_list
	message = ''
	error = False
	if request.method == 'POST':
		print(book_list)
		form = BookForm(request.POST)
		if form.is_valid():
			isbn = form.cleaned_data['book_isbn']
			form = BookForm()
			try:
				book = Books.objects.get(book_isbn=isbn)
				print(book.book_borrowid)
				if book in book_list:
					message = '請勿重複掃描書籍'
					messages.warning(request, message, extra_tags='alert')
					return render(request, 'main/rent.html', {'form':form, 'book_list':book_list})
				if book.book_borrowid != request.user.profile.school_id and not book.book_borrowid == '':
					message = '這本書已被{} {}借出, 請選擇其他書籍'.format(book.book_borrowid, book.book_borrowname)
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
	if len(book_list) == 0:
		messages.error(request, '請先借閱書籍', extra_tags='alert')
		return render(request, 'main/rent_confirm.html')
	borrow_list = list(book_list)
	book_list = []
	print(request.user.username)
	confirm_rent_database(borrow_list, request.user)
	messages.success(request, '借閱&歸還成功', extra_tags='alert')
	return render(request, 'main/rent_confirm.html', {'borrow_list':borrow_list})

@login_required(login_url='/login/')
def history(request):
	borrow_list = Borrows.objects.filter(borrower=request.user.profile.real_name)
	return render(request, 'main/history.html', {'borrow_list':borrow_list})

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
			message = '找不到帳號或帳號密碼錯誤'
			messages.error(request, message, extra_tags='alert')
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
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.real_name = form.cleaned_data.get('real_name')
			user.profile.school_id = form.cleaned_data.get('school_id')
			user.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/book/')
	else:
		form = RegisterForm()
	return render(request, 'main/register.html', {'form':form})

# addBookList = []
# @user_passes_test(check_admin)
def addBookView(request):
	# global addBookList
	book_need_confirm = {}
	barcode = ''
	if request.method == 'POST':
		form = AddBookForm(request.POST)
		isbn = request.POST['isbn']
		barcode = request.POST['barcode']
		title = request.POST['title']
		author = request.POST['author']
		pubtime = request.POST['pubtime']
		print(request.POST)
		if 'search' in request.POST:
			try:
				book_need_confirm = Books.objects.get(book_isbn=isbn)				
			except:
				message = '資料庫中無此書籍'
				messages.warning(request, message, extra_tags='alert')
		elif form.is_valid() and 'save' in request.POST:
			try:
				book = Books.objects.get(book_isbn=isbn)
				book.book_title = title
				book.book_author = author
				book.book_pubtime = pubtime
				book.book_isbn = isbn
				book.book_barcode = barcode
				book.save()
				barcode = ''
				message = '已儲存'
				messages.success(request, message, extra_tags='alert')
			except:
				book = Books.objects.create()
			form = AddBookForm()
	else:
		form = AddBookForm()

	return render(request, 'main/addbook.html', {'form':form, 'book_need_confirm':book_need_confirm, 'barcode':barcode})
