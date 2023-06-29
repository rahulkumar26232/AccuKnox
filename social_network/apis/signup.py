from django.contrib.auth.hashers import make_password

from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView

from social_network.models import User
from social_network.serializers import UserRegistrationSerializer


class UserSignupApi(APIView):
    authentication_classes = []
    permission_classes = []

    @transaction.atomic
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']

        try:
            user = User.objects.get(email__iexact=email)
            if user:
                return Response({'status': 'failure', 'message': 'User already exists with this email', "payload": {}})

        except User.DoesNotExist:
            user = User(email=email, first_name=first_name, last_name=last_name)
            user.password = make_password(password)
            user.save()

        return Response({
            'status': 'success', 'message': 'User successfully signed up'
            , "payload": {}
        })
