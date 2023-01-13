from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Subscription
from datetime import datetime
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm, SubForm
from django.contrib.auth.mixins import PermissionRequiredMixin
#from django.core.mail import EmailMultiAlternatives
#from django.template.loader import render_to_string
from django.http import HttpResponse
from table.tasks import hello, w_send_mail


class IndexView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('Hello!')


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

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


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('table.add_product',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def post(self, request, *args, **kwargs):
        article = Post(
            author=request.POST['author'],
            title=request.POST['title'],
            category=request.POST['category'],
            text=request.POST['text'],
        )
        article.save()
        w_send_mail.delay()
        return redirect('post_list')


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('table.change_product',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('table.delete_product',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class Suber(CreateView):
    model = Subscription
    form_class = SubForm
    template_name = 'make_subscription.html'
    success_url = reverse_lazy('post_list')