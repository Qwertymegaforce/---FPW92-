from django.db import models


class ModelTempUser(models.Model):
    temp_user_username = models.CharField(max_length=64, unique=True)
    temp_user_email = models.CharField(max_length=128, unique=True)
    temp_user_password1 = models.CharField(max_length=32)
    temp_user_password2 = models.CharField(max_length=32)
    super_token = models.CharField(max_length=12)

    def __str__(self):
        return self.temp_user_username
