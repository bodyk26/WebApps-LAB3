from django.contrib.auth.models import AbstractUser
from django.db import models

class ExtendedUser(AbstractUser):
	date_of_birth = models.DateField(null=True)
	group_id = models.IntegerField(default=0)
	SEX_CHOICES = (
		('male', 'Male'),
		('female', 'Female'),
	)
	sex = models.CharField(
		max_length=6,
		choices=SEX_CHOICES,
	)