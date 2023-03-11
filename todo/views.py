import requests

from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView

from .models import Todo
from .forms import TodoForm

HEADERS = {
    'Authorization': f'Bearer {settings.ACCESS_TOKEN}'
}


class Home(LoginRequiredMixin, FormView):
    template_name = 'todo/home.html'
    form_class = TodoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Get the current user
        profile = self.request.user.profile

        # Prepare the data to be sent to the API
        data = {
            'title': form.cleaned_data['title'],
            'description': form.cleaned_data['description'],
            'profile': profile.id  # Include the current user ID
        }
        
        # Send a POST request to the API to create a new to-do item
        response = requests.post(
            'http://localhost:8000/api/', data=data, headers=HEADERS)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the list of to-do items from the API
        response = requests.get('http://localhost:8000/api/', headers=HEADERS)
        context['todos'] = response.json()
        return context


@login_required
def todo_complete(request, pk):
    response = requests.get(
        f'http://localhost:8000/api/{pk}/', headers=HEADERS)
    completed = response.json()['completed']
    title = response.json()['title']
    description = response.json()['description']
    if completed:
        data = {
            'title': title,
            'description': description,
            'completed': False}
    else:
        data = {
            'title': title,
            'description': description,
            'completed': True}
    requests.put(
        f'http://localhost:8000/api/{pk}/', headers=HEADERS, data=data)
    return redirect('home')
