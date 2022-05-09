from rest_framework import serializers
from accounts.serializers import RegisterUserSerialiser

class AddressSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    street = serializers.CharField()
    house_number = serializers.IntegerField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    country = serializers.CharField()
    users = RegisterUserSerialiser(read_only=True, many=True)
