from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
    friends = models.ManyToManyField('self', blank=True)

    
class Chat(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True)
    members = models.ManyToManyField(CustomUser)
    personal = models.BooleanField(default=True)


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, null=True, on_delete=models.CASCADE)
    text = models.TextField()

