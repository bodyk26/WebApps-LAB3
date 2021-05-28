from django.db import models
from django.core.validators import RegexValidator
from account_management.models import ExtendedUser
from django.urls import reverse


class Phonebook(models.Model):
	owner = models.ForeignKey(ExtendedUser,
							   on_delete=models.CASCADE)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	person_name = models.CharField(max_length=70)
	person_email = models.EmailField(max_length=70, blank=True, null=True)

	def __str__(self):
 		return self.person_name

	def get_absolute_url(self):
		return reverse('phonenumber_detail', args=[str(self.id)])
