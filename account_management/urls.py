from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('myprofile/', views.MyProfileView.as_view(), name='myprofile'),
]