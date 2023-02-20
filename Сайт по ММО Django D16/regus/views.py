from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .utils import random_create_token

from django.db.models.signals import post_save
from django.dispatch import receiver

from .forms import *
from .models import *


@receiver(post_save, sender=ModelTempUser)
def confirm_email(sender, instance, created, **kwargs):
    '''When temp user created this func sends him mail with link confirmation'''
    html = render_to_string(
        'regus/confirm.html',
        {
            'link': f'http://127.0.0.1:8000/user_action/confirm/{instance.super_token}'
        }
    )

    msg = EmailMultiAlternatives(
        subject='Подтверждение регистрации',
        body='',
        from_email='solomonovyegor@yandex.ru',
        #to=[f'{instance.temp_user_email}'], #Все еще Яндекс, все еще Яндекс
        to=['solomonovyegor@yandex.ru'],
    )

    msg.attach_alternative(html, "text/html")
    msg.send()


def finish(request, token):
    '''Finishes registration by converting temp user into default django one. Also deletes
    unnecessary data from database'''
    test_item = ModelTempUser.objects.filter(super_token=token)
    if test_item.exists():
        temp_user = ModelTempUser.objects.get(super_token=token)
        new_user = User.objects.create_user(
            username=temp_user.temp_user_username,
            password=temp_user.temp_user_password1,
            email=temp_user.temp_user_email
        )
        context = {
            'new': new_user
        }
        temp_user.delete()
        return render(request, 'regus/register_confirmed.html', context)
    return HttpResponse('Все уже подтверждено!')


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


class TempUser(CreateView):
    '''Creates a table in database with temporary user'''
    form_class = RegisterUserForm
    model = ModelTempUser
    template_name = 'regus/user_register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        while True:
            formed_token = random_create_token()
            test_item = ModelTempUser.objects.filter(super_token=formed_token)
            if not test_item.exists():
                self.object.super_token = formed_token
                self.object = form.save()
                return super().form_valid(form)


def logout_user(request):
    ''' The purpose of existiment of this small function is to 'logout' User '''
    logout(request)
    return redirect('home')
