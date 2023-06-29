from rest_framework import serializers

from social_network.models import User, FriendRequest


class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        fields = ['password', 'email','first_name','last_name']


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class SendFriendRequestInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    class Meta:
        fields = ["user_id"]


class FriendRequestModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequest
        fields = ['id',  'status']


class AcceptFriendRequestSerializer(serializers.Serializer):
    request_id = serializers.IntegerField()
    is_accepted = serializers.BooleanField()

    class Meta:
        fields = ["request_id","is_accepted"]
