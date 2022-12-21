from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   class Meta:
        model = Post
        fields = ['author', 'title', 'category', 'text']

   def clean(self):
      cleaned_data = super().clean()
      title = cleaned_data.get('title')
      category = cleaned_data.get('category')

      if title == category:
          raise ValidationError('Название статьи не должно быть равно категории')

      if title[0].islower():
          raise ValidationError("Название должно начинаться с заглавной буквы")

      return cleaned_data
