from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from accounts.models import StudentUser
from courses.models import Course
from rest_framework.authentication import TokenAuthentication
from courses.serializers import CourseSerializer, CoursePatchSerializers, InstructorSerializer, StudentSerializer
from django.contrib.auth.models import AnonymousUser


class CoursesView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request: Request):
        isAdmin = request.user
        if isinstance(isAdmin, AnonymousUser):
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        if not isAdmin.is_admin:
            return Response( {'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_course = Course.objects.filter(name= serializer.validated_data['name'])

        if found_course:
            return Response({'message': 'Course already exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
        course = Course.objects.create(**serializer.validated_data)
        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, _:Request, course_id=''):
        try:
            if course_id:
                course = Course.objects.filter(uuid=course_id)

                if not course:
                    return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)
                
                serializer = CourseSerializer(course, many=True)
                return Response(serializer.data[0], status=status.HTTP_200_OK)

            courses = Course.objects.all()
            serializers = CourseSerializer(courses, many=True)

            return Response(serializers.data, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({"Detail": "Format ID incorrect"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request:Request, course_id=''):
        isAdmin = request.user
        try:
            if isinstance(isAdmin, AnonymousUser):
                return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
            if not isAdmin.is_admin:
                return Response( {'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
            course = Course.objects.filter(uuid=course_id)

            if not course:
                return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

            serializer = CoursePatchSerializers(request.data)
            course.update(**serializer.data)
            serializer = CourseSerializer(course[0])

            return Response(serializer.data, status=status.HTTP_200_OK)

        except IntegrityError:
            return Response({"message": "This course name already exists"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except ValidationError:
            return Response({"Detail": "Format ID incorrect"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, course_id=''):
        try:
            isAdmin = request.user
            if isinstance(isAdmin, AnonymousUser):
                return Response({"detail": 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

            if isAdmin.is_admin:
                course = Course.objects.filter(uuid=course_id)

                if not course:
                    return Response({"message": "Course does not exist"},  status=status.HTTP_404_NOT_FOUND)
                
                course.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        
        except ValidationError:
            return Response({"Detail": "Format ID incorrect"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, course_id=''):
        isAdmin = request.user

        if isinstance(isAdmin, AnonymousUser):
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        if not isAdmin.is_admin:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

        course = Course.objects.filter(uuid=course_id).first()
        if not course:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InstructorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instructor = StudentUser.objects.filter(uuid=serializer.validated_data["instructor_id"]).first()
        if not instructor:
            return Response({"message": "Invalid instructor_id"}, status=status.HTTP_404_NOT_FOUND)
        if not instructor.is_admin:
            return Response({"message": "Instructor id does not belong to an admin"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        courses = Course.objects.filter(instructor_id=instructor.uuid).first()
        if courses:
            courses.instructor = None
            courses.save()
        course.instructor = instructor
        course.save()

        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PutStudentView(APIView):
    authentication_classes = [TokenAuthentication]

    def put(self, request: Request, course_id=''):

        isAdmin = request.user

        if isinstance(isAdmin, AnonymousUser):
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        if not isAdmin.is_admin:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        course= Course.objects.filter(uuid=course_id).first()
        if not course:
            return Response({"message": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        for uuid in serializer.validated_data['students_id']:
            student= StudentUser.objects.filter(uuid=uuid).first()
            if not student:
                return Response({"message": "Invalid students_id list"}, status=status.HTTP_404_NOT_FOUND)
            if student.is_admin:
                return Response({"message": "Some student id belongs to an Instructor"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            else:
                course.students.add(student)
                course.save()
            serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)