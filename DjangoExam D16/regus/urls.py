from django.urls import path

from .views import *


urlpatterns = [
    path('registration/', UserRegister.as_view(), name='register'),
    path('login/', AuthUSer.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]