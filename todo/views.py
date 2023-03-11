import requests

from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from .models import Todo
from .forms import TodoForm


class Home(LoginRequiredMixin, FormView):
    template_name = 'todo/home.html'
    form_class = TodoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Get the current user
        user = self.request.user

        # Prepare the data to be sent to the API
        data = {
            'title': form.cleaned_data['title'],
            'description': form.cleaned_data['description'],
            'user': user.id  # Include the current user ID
        }

        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4NTE2MDI0LCJpYXQiOjE2Nzg1MTQyMjQsImp0aSI6ImI2MzdmNzJkYWVkMDRhNzlhYTIzZDIyOGI1YWRhNTUyIiwidXNlcl9pZCI6MX0.HI092yidIFeSDaQF12wB2Lj-bDfiIt0Cd04LgP5pfxc'
        }
        
        # Send a POST request to the API to create a new to-do item
        response = requests.post('http://localhost:8000/api/', data=data, headers=headers)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4NTE2MDI0LCJpYXQiOjE2Nzg1MTQyMjQsImp0aSI6ImI2MzdmNzJkYWVkMDRhNzlhYTIzZDIyOGI1YWRhNTUyIiwidXNlcl9pZCI6MX0.HI092yidIFeSDaQF12wB2Lj-bDfiIt0Cd04LgP5pfxc'
        }
        # Fetch the list of to-do items from the API
        response = requests.get('http://localhost:8000/api/', headers=headers)
        context['todos'] = response.json()
        return context
