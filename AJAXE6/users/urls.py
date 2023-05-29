from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', registration_page, name='registration_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('find_users/', find_users, name='find_users'),
    path('create_chat/', create_chat, name='create_chat'),
    path('set_chat/<int:pk>', set_chat, name='set_chat'),
    path('chat/<int:pk>', personal_chat, name='chat' ),
    path('api/get_friends', get_friends),
    path('api/create_user', registration),
    path('api/login_user', login_user),
    path('api/update_profile', change_profile),
    path('api/get_users/<str:first_name>/<str:last_name>', get_users),
    path('api/to_friend_list/<int:pk>', to_friend_list),
    path('api/form_chat', form_chat)
]
