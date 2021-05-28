import datetime
import json
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from my_phonebook.models import Phonebook
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from chat.models import ConnectedUsers
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UsersOnlineView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	model = ConnectedUsers
	context_object_name = 'connected_users'
	template_name = 'chat/online.html'
	login_url = 'login'

	def test_func(self):
		return self.request.user.is_staff


class ChatView(LoginRequiredMixin, TemplateView):
	template_name = 'chat/chat.html'
	login_url = 'login'

	def get_context_data(self):
		context = super().get_context_data()
		context['room_name'] = 'room'
		return context


class SendNumberView(LoginRequiredMixin, TemplateView):
	template_name = 'chat/chat.html'
	login_url = 'login'

	def get(self, request, *args, **kwargs):
	    channel_layer = get_channel_layer()
	    if not channel_layer.groups:
	        return render(request, 'chat/send_number.html', {
	            'message': "Error!"
	        })

	    number = get_object_or_404(Phonebook, pk=kwargs['pk'])
	    message = "Person: %s\nPhone number: %s\n" % (number.person_name, number.phone_number) 

	    async_to_sync(channel_layer.group_send)(
	        list(channel_layer.groups.keys())[0],
	        {
	            'type': 'chat_message',
	            'message': message,
	            'user' : request.user.username,
	            'datetime': timezone.now().isoformat(), 
	        }
	    )
	    return render(request, 'chat/send_number.html', {
	        'message': "Success!"
	    })