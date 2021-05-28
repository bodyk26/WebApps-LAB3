from django.urls import path
from . import views


urlpatterns = [
	path('', views.MyPhonebookView.as_view(), name='myphonebook'),
	path('search/<str:word>/', views.PhonebookSearchView.as_view(), name='phonebooksearch'),
	path('<int:pk>/', views.PhonenumberDetailView.as_view(), name='phonenumber_detail'),
	path('create/', views.PhonenumberCreateView.as_view(), name='phonenumber_create'),
	path('update/<int:pk>/', views.PhonenumberUpdateView.as_view(), name='phonenumber_update'),
	path('delete/<int:pk>/', views.PhonenumberDeleteView.as_view(), name='phonenumber_delete'),
]

