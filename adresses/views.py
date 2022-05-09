from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from adresses.models import Address
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

from adresses.serializers import AddressSerializer


class AddressView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def put(self, request: Request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        userOn = request.user

        address = Address.objects.create(**serializer.validated_data)
        address.save()

        userOn.address = address
        userOn.save()

        serializer = AddressSerializer(address)

        return Response(serializer.data, status=status.HTTP_200_OK)
