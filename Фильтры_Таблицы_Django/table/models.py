from django.db import models


class Author(models.Model):
    pass


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    text = models.TextField(default='Здесь ничего не написано')

    def __str__(self):
        return f'{self.title}, {self. category}, {self.text}'



