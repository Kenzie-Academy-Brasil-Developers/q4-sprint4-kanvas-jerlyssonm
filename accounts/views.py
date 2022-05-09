from urllib import request
from django.contrib.auth import authenticate
from .serializers import LoginUserSerializer, RegisterUserSerialiser

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

from accounts.models import StudentUser


class AccountsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = []

    def get(self, request: Request):
        self.permission_classes.append(IsAuthenticated)
        userOn = request.user
        if userOn.is_admin:
            students = StudentUser.objects.all()
            onlyStudents = students.filter(is_admin = False)
            serializer = RegisterUserSerialiser(onlyStudents, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"message": "Your not authorizated"}, status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request: Request):
        
        serializer = RegisterUserSerialiser(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        found_user = StudentUser.objects.filter(
            email=serializer.validated_data['email']
            ).exists()

        if found_user:
            return Response({"message": "User already exists"}, status=status.HTTP_409_CONFLICT)

        user = StudentUser.objects.create_user(**serializer.validated_data)
        user.set_password(serializer.validated_data['password'])
        user.save()
        serializer = RegisterUserSerialiser(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def login_user_view(request: Request):
    serializer = LoginUserSerializer(data=request.data)
    
    serializer.is_valid(raise_exception=True)

    user = authenticate(
        email = serializer.validated_data['email'],
        password = serializer.validated_data['password'],
    )

    if not user:
        return Response({"message": "Invalide Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({"token": token.key})
