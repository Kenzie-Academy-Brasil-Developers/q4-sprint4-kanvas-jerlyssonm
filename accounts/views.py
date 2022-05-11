from django.contrib.auth import authenticate
from .serializers import LoginUserSerializer, RegisterUserSerialiser

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AnonymousUser

from accounts.models import StudentUser


class AccountsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []

    def get(self, request: Request):
        userOn = request.user
        if isinstance(userOn, AnonymousUser):
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        if userOn.is_admin:
            students = StudentUser.objects.all()
            serializer = RegisterUserSerialiser(students, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request: Request):
        
        serializer = RegisterUserSerialiser(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        found_user = StudentUser.objects.filter(
            email=serializer.validated_data['email']
            ).exists()

        if found_user:
            return Response({"message": "User already exists"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        user = StudentUser.objects.create_user(**serializer.validated_data)
        user.set_password(serializer.validated_data['password'])
        user.save()
        serializer = RegisterUserSerialiser(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request: Request):
        serializer = LoginUserSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'],
        )

        if not user:
            return Response({"message": "Invalide Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)
