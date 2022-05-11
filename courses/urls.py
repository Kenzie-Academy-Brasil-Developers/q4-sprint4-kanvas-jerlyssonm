from django.urls import path

from courses.views import CoursesView, PutStudentView


urlpatterns = [
    path('courses/', CoursesView.as_view()),
    path('courses/<course_id>/', CoursesView.as_view()),
    path('courses/<course_id>/registrations/instructor/', CoursesView.as_view()),
    path('courses/<course_id>/registrations/students/', PutStudentView.as_view()),
]
