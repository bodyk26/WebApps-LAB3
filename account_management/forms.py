from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ExtendedUser

class ExtendedUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = ExtendedUser
		fields = UserCreationForm.Meta.fields + ('email', 'date_of_birth', 'sex',)


class ExtendedUserChangeForm(UserChangeForm):
	class Meta:
		model = ExtendedUser
		fields = UserChangeForm.Meta.fields
