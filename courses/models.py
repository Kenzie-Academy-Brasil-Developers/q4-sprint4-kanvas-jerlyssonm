import uuid
from django.db import models


class Course(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    demo_time = models.TimeField()
    created_at = models.DateTimeField(null=True)
    link_repo = models.CharField(max_length=499)
    instructor = models.OneToOneField('accounts.StudentUser', null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField('accounts.StudentUser', related_name='courses')
