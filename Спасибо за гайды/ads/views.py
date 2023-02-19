from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import *
from .forms import *


class AdsList(ListView):
    '''Shows Default Homepage with list of all posts'''
    model = Ads
    paginate_by = 6
    template_name = 'ads/home.html'
    context_object_name = 'ads'


class DetailAd(DetailView):
    '''Shows single ad'''
    model = Ads
    template_name = 'ads/ad.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'ad_id'


class CreateAd(LoginRequiredMixin, CreateView):
    '''Create ad'''
    form_class = CreateAdForm
    model = Ads
    template_name = 'ads/create_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Добавить объявление'
        return context


class UpdateAd(LoginRequiredMixin, UpdateView):
    form_class = CreateAdForm
    template_name = 'ads/create_add.html'
    model = Ads
    pk_url_kwarg = 'ad_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['value'] = 'Обновить объявление'
        return context


class DeleteAd(LoginRequiredMixin, DeleteView):
    model = Ads
    template_name = 'ads/delete_add.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'ad_id'
    context_object_name = 'ad'


class CreateResponse(CreateView):
    pass


class DenyResponse(DeleteView):
    pass
