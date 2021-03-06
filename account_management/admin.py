from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ExtendedUserCreationForm, ExtendedUserChangeForm
from .models import ExtendedUser

class ExtendedUserAdmin(UserAdmin):
	add_form = ExtendedUserCreationForm
	form = ExtendedUserChangeForm
	model = ExtendedUser
	list_display = ['email', 'username', 'date_of_birth', 'sex', 'is_staff', ]
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('date_of_birth', 'sex')}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('date_of_birth', 'sex')}),
	)

admin.site.register(ExtendedUser, ExtendedUserAdmin)
