from django import forms

class NameForm(forms.Form):
 	book_isbn = forms.CharField(label='書籍ISBN', max_length=100)

class LoginForm(forms.Form):
	username = forms.CharField(label='帳號', max_length=50)
	password = forms.CharField(label='密碼', max_length=50, widget=forms.PasswordInput)
