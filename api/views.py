from rest_framework import generics
from my_phonebook.models import Phonebook
from .serializers import PhonebookSerializer
from .permissions import IsOwner


class PhonebookAPIView(generics.ListCreateAPIView):
	serializer_class = PhonebookSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def get_queryset(self):
		return Phonebook.objects.filter(owner=self.request.user.id)

class DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwner,)
	serializer_class = PhonebookSerializer

	def get_queryset(self):
		return Phonebook.objects.filter(owner=self.request.user.id)
