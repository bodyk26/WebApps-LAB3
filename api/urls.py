from django.urls import path
from .views import PhonebookAPIView, DetailAPIView

urlpatterns = [
	path('phonenumber/<int:pk>/', DetailAPIView.as_view()),
	path('', PhonebookAPIView.as_view()),
]
