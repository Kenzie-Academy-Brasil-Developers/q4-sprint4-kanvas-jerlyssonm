from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentUserSerialiser
from rest_framework import status

from accounts.models import StudentUser


class AccountView(APIView):
    def post(self, request):
        serializer = StudentUserSerialiser(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        find_user = StudentUser.objects.filter(email=serializer.validated_data['email']).exists()

        if find_user:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        user = StudentUser.objects.create_user(**serializer.validated_data)

        serializer = StudentUserSerialiser(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

