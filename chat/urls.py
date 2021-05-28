from django.urls import path

from . import views

urlpatterns = [
    path('sendnumber<int:pk>/', views.SendNumberView.as_view(), name='sendnumber'),
    path('online/', views.UsersOnlineView.as_view(), name='online'),
    path('', views.ChatView.as_view(), name='chat'),
]