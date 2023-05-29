from rest_framework import serializers
from .models import CustomUser, Chat, Message


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'password')



class UserSerializer(serializers.ModelSerializer):
    
    friends = FriendSerializer(many=True, read_only=True)


    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar', 'friends', 'password')


    def create(self, validated_data):
        print(validated_data)
        if CustomUser.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError('Такой пользователь существует')
        user = CustomUser.objects.create_user(**validated_data)
        user.password = validated_data['password']
        return user


class ChatSerializer(serializers.ModelSerializer):

    members = FriendSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'name', 'image', 'members')


    def create(self, validated_data):

        return super().create(validated_data)


    
