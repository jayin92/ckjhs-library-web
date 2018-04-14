from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.Form):
 	book_isbn = forms.CharField(label='書籍ISBN', max_length=100)

class LoginForm(forms.Form):
	username = forms.CharField(label='帳號', max_length=50)
	password = forms.CharField(label='密碼', max_length=50, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
	real_name = forms.CharField(help_text='請輸入真實姓名', max_length=5)
	school_id = forms.CharField(help_text='例如：41402',max_length=5)

	class Meta:
		model = User
		fields = ('username', 'real_name', 'school_id', 'password1', 'password2')

class AddBookForm(forms.Form):
	isbn = forms.CharField(label='書籍ISBN', max_length=100)
	barcode = forms.CharField(label='書籍條碼', max_length=5)
	title = forms.CharField(label='標題')
	author = forms.CharField(label='作者')
	pubtime = forms.CharField(label='出版日期')
