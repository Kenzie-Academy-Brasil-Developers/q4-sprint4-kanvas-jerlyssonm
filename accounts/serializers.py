from rest_framework import serializers


class RegisterUserSerialiser(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_admin =serializers.BooleanField()

class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()