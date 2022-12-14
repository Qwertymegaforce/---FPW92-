from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = datetime.utcnow()
        context['main_event'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'event.html'
    context_object_name = 'post'
