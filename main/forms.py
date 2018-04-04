from django import forms

class NameForm(forms.Form):
 	book_isbn = forms.CharField(label='書籍ISBN', max_length=100)
