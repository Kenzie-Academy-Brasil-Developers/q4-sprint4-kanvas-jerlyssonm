from rest_framework import serializers


class StudentUserSerialiser(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    is_admin =serializers.BooleanField()
