from django.shortcuts import render
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import SignupForm

class SignupView(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('myapp.index')

class MypageView(DetailView):
    model = CustomUser
    template_name = 'accounts/mypage.html'