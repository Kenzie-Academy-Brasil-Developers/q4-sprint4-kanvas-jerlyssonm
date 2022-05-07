from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentUser


admin.site.register(StudentUser, UserAdmin)
