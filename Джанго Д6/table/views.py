from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Subscription
from datetime import datetime
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm, SubForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


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

        data = list(Subscription.objects.all())
        post = list(Post.objects.all())
        send = post[-1]

        for i in data:

            if i.name == send.category:
                link = 'http://127.0.0.1:8000/news/' + f'{article.id}'
                html = render_to_string(
                    'single_mail.html',
                    {
                        'post': article,
                        'link': link,
                    }
                )
                msg = EmailMultiAlternatives(
                    subject=f'Внимание, на горизонте замачил очередной кринж категории {article.category}',
                    body=article.text,
                    from_email='solomonovyegor@yandex.ru',
                    to=[f'{i.mail}']
                )
                msg.attach_alternative(html, "text/html")
                msg.send()

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