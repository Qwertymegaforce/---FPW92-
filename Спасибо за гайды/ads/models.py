from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    '''Allows to create categories in admin panel'''
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Ads(LoginRequiredMixin, models.Model):
    '''Post model'''
    author = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=128)
    time_creation = models.TimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField(default='В этом объявлении нет текста 😔')
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        verbose_name = 'Посты'
        verbose_name = 'Пост'
        ordering = ['-time_creation']

    def __str__(self):
        return f"""
        Автор - {self.author}
        Заголовок - {self.title}
        Категория - {self.category}
        Текст - {self.text}
        """

    def get_absolute_url(self):
        return reverse('detail_ad', kwargs={'ad_id': self.id})


class Response(LoginRequiredMixin, models.Model):
    '''Response model'''
    left_by = models.ForeignKey(User, on_delete=models.CASCADE)
    to_post = models.ForeignKey(Ads, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"""
        Оставлено пользователем {self.left_by}
        К посту {self.to_post}
        Со следующим содержанием {self.message}
        """
