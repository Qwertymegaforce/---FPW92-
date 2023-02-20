from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormMixin

from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import *
from .forms import *


@receiver(post_save, sender=Response)
def first_accept(sender, instance, created, **kwargs):
    '''When the Response created -> send notification'''
    send_mail(
        subject=f'Пользователь {instance.left_by.username} откликнулся на ваше объявление!',
        message=f"""Примите отклик в личном кабинете! 
        
        {instance.message}""",
        from_email='solomonovyegor@yandex.ru',
        # recipient_list=[f'{instance.left_by.email}'], #Потому что спам фильтр, я не виноват
        recipient_list=[f'solomonovyegor@yandex.ru'],
    )


def accept(request, key):
    '''Function to accept the response and send mail'''
    response = Response.objects.get(id=key)
    send_mail(
        subject=f'Пользователь {response.to_post.author.username} принял ваше предложение!',
        message=f'Электронная почта для продолжения общения {response.to_post.author.email}',
        from_email='solomonovyegor@yandex.ru',
        #recipient_list=[f'{response.left_by.email}'], все еще чертов спам фильтр
        recipient_list=[f'solomonovyegor@yandex.ru'],
    )
    response.delete()
    return redirect('home')


class AdsList(ListView):
    '''Shows Default Homepage with list of all posts'''
    model = Ads
    paginate_by = 6
    template_name = 'ads/home.html'
    context_object_name = 'ads'


class DetailAd(FormMixin, DetailView):
    '''Shows single ad'''
    model = Ads
    template_name = 'ads/ad.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'ad_id'
    form_class = CreateResponseForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        '''Automatically fill the form`s fields (left_by and to_post in Response model)
        with some necessary data that cannot be input by user itself'''
        self.object = form.save(commit=False)
        self.object.left_by = self.request.user
        self.object.to_post = self.get_object()
        self.object = form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CreateAd(LoginRequiredMixin, CreateView):
    '''Create ad'''
    form_class = CreateAdForm
    model = Ads
    template_name = 'ads/create_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Добавить объявление'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class UpdateAd(LoginRequiredMixin, UpdateView):
    '''Updates Ad. Method is prohibited for everyone except admin and author'''
    fields = ['title', 'text']
    template_name = 'ads/update_add.html'
    model = Ads
    pk_url_kwarg = 'ad_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Обновить объявление'
        return context

    def get_form_kwargs(self):
        '''If user is admin or user is owner of the ad he can change it then'''
        kwargs = super().get_form_kwargs()
        if self.request.user.is_superuser:
            return kwargs
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class DeleteAd(LoginRequiredMixin, DeleteView):
    '''Deletes Ad. Method is prohibited for everyone except admin and author'''
    model = Ads
    template_name = 'ads/delete_add.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'ad_id'
    context_object_name = 'ad'

    def post(self, request, *args, **kwargs):
        '''Method guarantees the post will be deleted only by owner ow admin  '''
        self.object = self.get_object()
        success_url = self.get_success_url()
        if request.user != self.object.author:
            return self.handle_no_permission()
        elif request.user.is_superuser:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        self.object.delete()
        return HttpResponseRedirect(success_url)


class ResponseList(ListView):
    '''Shows the list of owner`s post responses'''
    model = Response
    paginate_by = 6
    template_name = 'ads/response.html'
    context_object_name = 'resp'

    def get_queryset(self):
        return Response.objects.filter(to_post__author=self.request.user)


class DenyResponse(LoginRequiredMixin, DeleteView):
    ''' Deny response and then delete it from database '''
    model = Response
    template_name = 'ads/delete_resp.html'
    success_url = reverse_lazy('response_list')
    pk_url_kwarg = 'resp_id'
    context_object_name = 'resp'

    def post(self, request, *args, **kwargs):
        '''Method guarantees the response will be deleted only by owner or admin '''
        self.object = self.get_object()
        success_url = self.get_success_url()
        if self.request.user != self.object.to_post.author:
            return self.handle_no_permission()
        elif request.user.is_superuser:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        self.object.delete()
        return HttpResponseRedirect(success_url)
