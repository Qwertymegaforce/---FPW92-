from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    created_after = DateTimeFilter(
        field_name='time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Post
        fields = {
            'author': ['icontains'],
            'title': ['icontains'],
            'category': ['icontains'],
            'text': ['icontains'],
        }