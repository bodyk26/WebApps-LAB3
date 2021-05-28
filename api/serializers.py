from rest_framework import serializers
from my_phonebook.models import Phonebook

class PhonebookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Phonebook
		fields = ('person_name', 'phone_number', 'person_email')
