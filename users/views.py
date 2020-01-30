from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomCreationForm

class SignupView(CreateView):
    form_class = CustomCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
