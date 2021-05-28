from .forms import ExtendedUserCreationForm
from .models import ExtendedUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
	form_class = ExtendedUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

class MyProfileView(LoginRequiredMixin, generic.TemplateView):
	model = ExtendedUser
	template_name = 'account_management/myprofile.html'
	login_url = 'login'