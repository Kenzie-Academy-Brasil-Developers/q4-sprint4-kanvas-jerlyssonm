from datetime import datetime
from rest_framework import serializers
from accounts.serializers import RegisterUserSerialiser


class CourseSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField()
    demo_time = serializers.TimeField()
    created_at = serializers.DateTimeField(default=datetime.now())
    link_repo = serializers.CharField()
    instructor = RegisterUserSerialiser(read_only=True)
    students = RegisterUserSerialiser(read_only=True, many=True)
    
class CoursePatchSerializers(serializers.Serializer):
    name = serializers.CharField(required=False)
    demo_time = serializers.TimeField(required=False)
    link_repo = serializers.CharField(required=False)

class InstructorSerializer(serializers.Serializer):
    instructor_id = serializers.UUIDField()

class StudentSerializer(serializers.Serializer):
    students_id = serializers.ListField(child=serializers.UUIDField())
