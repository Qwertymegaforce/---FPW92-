import time
import datetime
from celery import shared_task
from table.models import Subscription, Post
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail


@shared_task
def do_it_weekly():
    data = list(Subscription.objects.all())
    for i in data:
        send_mail(
            subject='Новые новости на нашем сайте',
            message='http://127.0.0.1:8000/news/',
            from_email='solomonovyegor@yandex.ru',
            recipient_list=[f'{i.mail}']
        )


@shared_task
def w_send_mail():
    data = list(Subscription.objects.all())
    post = list(Post.objects.all())
    send = post[-1]

    for i in data:

        if i.name == send.category:
            link = 'http://127.0.0.1:8000/news/' + f'{send.id}'
            html = render_to_string(
                'single_mail.html',
                {
                    'post': send,
                    'link': link,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Внимание, на горизонте замачил очередной кринж категории {send.category}',
                body=send.text,
                from_email='solomonovyegor@yandex.ru',
                to=[f'{i.mail}']
                #to=['solomonovyegor@yandex.ru']
            )
            msg.attach_alternative(html, "text/html")
            msg.send()


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")




