from django.urls import path

from .views import *


urlpatterns = [
    path('registration/', TempUser.as_view(), name='register'),
    path('login/', AuthUSer.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('confirm/<int:token>', finish, name='finish'),
]
