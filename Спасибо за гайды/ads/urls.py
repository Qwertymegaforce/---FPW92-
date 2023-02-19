from django.urls import path

from .views import *


urlpatterns = [
    path('', AdsList.as_view(), name='home'),
    path('ad/<int:ad_id>', DetailAd.as_view(), name='detail_ad'),
    path('create_add/', CreateAd.as_view(), name='create_add'),
    path('update_add/<int:ad_id>', UpdateAd.as_view(), name='update_add'),
    path('delete/<int:ad_id>', DeleteAd.as_view(), name='delete_add')
]
