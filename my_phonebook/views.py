from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Phonebook
from django.urls import reverse_lazy


class MyPhonebookView(LoginRequiredMixin, ListView):
	model = Phonebook
	context_object_name = 'phonenumbers_list'
	template_name = 'my_phonebook/myphonebook.html'
	login_url = 'login'

	def get_queryset(self):
		return Phonebook.objects.filter(owner=self.request.user.id)



class PhonebookSearchView(LoginRequiredMixin, ListView):
	model = Phonebook
	context_object_name = 'phonenumbers_list'
	template_name = 'my_phonebook/myphonebook.html'
	login_url = 'login'

	def get_queryset(self):
		word = self.kwargs['word']
		return Phonebook.objects.filter(owner=self.request.user.id).filter(person_name__startswith=str(word))


class PhonenumberDetailView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Phonebook
	template_name = "my_phonebook/phonenumber_detail.html"

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user


class PhonenumberCreateView(LoginRequiredMixin, CreateView):
	model = Phonebook
	template_name = "my_phonebook/phonenumber_create.html"
	fields = ['person_name', 'phone_number', 'person_email']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)


class PhonenumberUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
	model = Phonebook
	template_name = "my_phonebook/phonenumber_update.html"
	fields = ['person_name', 'phone_number', 'person_email']

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user


class PhonenumberDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Phonebook
	template_name = "my_phonebook/phonenumber_delete.html"
	success_url = reverse_lazy('myphonebook')

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user
