from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *


class UserRegister(CreateView):
    ''' This class creates new User'''
    form_class = RegisterUserForm
    template_name = 'regus/user_register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class AuthUSer(LoginView):
    ''' This class helps user to authenticate '''
    form_class = AuthenticationForm
    template_name = 'regus/user_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    ''' The purpose of existiment of this small function is to 'logout' User '''
    logout(request)
    return redirect('home')
