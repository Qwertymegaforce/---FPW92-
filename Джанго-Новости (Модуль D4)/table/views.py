from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from datetime import datetime
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm

class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current'] = datetime.utcnow()
        context['main_event'] = None
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'event.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')