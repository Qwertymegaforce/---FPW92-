from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import CustomUser, Chat
from .serializers import UserSerializer, ChatSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import json


def homepage(request):
    if request.user.is_authenticated:
        context = {
        'friends': request.user.friends.all(),
        'chats': Chat.objects.filter(members__username = request.user.username, personal=False)
    }
        return render(request, 'users/homepage.html', context)
    
    return render(request, 'users/homepage.html')


def profile_page(request):
    return render(request, 'users/profile.html')


def login_page(request):
    return render(request, 'users/login.html')


def registration_page(request):
    return render(request, 'users/register.html')


def logout_user(request):
    logout(request)
    return redirect('homepage')


def find_users(request):
    return render(request, 'users/find_users.html')


def create_chat(request):
    return render (request, 'users/create_chat.html')


def set_chat(request, pk):
    user_chat = Chat.objects.filter(members__username = request.user.username, personal=True).get(members__id = pk)
    return redirect(f'chat', user_chat.id)


def personal_chat(request, pk):
    chat = Chat.objects.get(id=pk)
    context = {
        'room_id': pk,
        'chat' : chat,
        }
    if chat.personal:
        friend = chat.members.all().exclude(username=request.user.username).first()
        if friend.avatar:
            context['image'] = friend.avatar
            context['add'] = True
        else:
            context['add'] = False
        context['first_name'] = friend.first_name
        context['last_name'] = friend.last_name

    
    return render(request, 'users/chat.html', context)


@api_view(['GET', 'POST'])
def registration(request):
    serializer = UserSerializer(data=request.data, many=False)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def login_user(request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'accepted': 'authorized'}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error': 'Такого пользователя не существует!'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def change_profile(request):
    serializer = UserSerializer(data=request.data, instance=request.user, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_users(request, first_name, last_name):
    userlist = CustomUser.objects.filter(first_name=first_name, last_name=last_name).exclude(username__in=[i.username for i in request.user.friends.all()]).exclude(username=request.user.username)
    serializer = UserSerializer(userlist, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def to_friend_list(request, pk):
    friend = CustomUser.objects.get(id=pk)
    request.user.friends.add(friend)
    if not Chat.objects.filter(members__username = request.user.username, personal = True).filter(members__username=friend.username):
        personal_chat = Chat.objects.create()
        personal_chat.members.add(request.user, friend)
        personal_chat.save()
    return Response(status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_friends(request):
    friends = request.user.friends.all()
    friends_list = UserSerializer(friends, many=True)
    return Response(friends_list.data)


@api_view(['POST'])
def form_chat(request):
    list_arr = json.loads(dict(request.data)['members'][0])
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        new_chat = serializer.save(personal=False)
        for item in list_arr:
            new_chat.members.add(CustomUser.objects.get(id=item['id']))
        new_chat.members.add(CustomUser.objects.get(username=request.user.username))
        new_chat.personal = False
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
