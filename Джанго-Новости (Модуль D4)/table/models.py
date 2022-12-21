from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    text = models.TextField(default='Здесь ничего не написано')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}, {self.title}, {self. category}, {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



