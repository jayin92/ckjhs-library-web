from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:books_id>/', views.detail, name='detail'),
	path('rent/', views.get_name, name='get_name')
	# path('rent/', views.rent(), name='rent')
]
