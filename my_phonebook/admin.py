from django.contrib import admin
from .models import Phonebook

# Register your models here.

@admin.register(Phonebook)
class PhonebookAdmin(admin.ModelAdmin):
	list_display = ('owner', 'person_name', 'phone_number', 'person_email')
