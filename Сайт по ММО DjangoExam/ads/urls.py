from django.urls import path

from .views import *


urlpatterns = [
    path('', AdsList.as_view(), name='home'),
    path('ad/<int:ad_id>', DetailAd.as_view(), name='detail_ad'),
    path('create_add/', CreateAd.as_view(), name='create_add'),
    path('update_add/<int:ad_id>', UpdateAd.as_view(), name='update_add'),
    path('delete/<int:ad_id>', DeleteAd.as_view(), name='delete_add'),
    path('response_list/', ResponseList.as_view(), name='response_list'),
    path('accept_call/<int:key>', accept, name='accept'),
    path('deny_response/<int:resp_id>', DenyResponse.as_view(), name='deny')
]
