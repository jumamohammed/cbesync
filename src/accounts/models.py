from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

# Create your models here

#this is a custom user class or rather table for scalability to advanced types
class CustomUser(AbstractUser):
    SCHOOL = 'school'
    TEACHER = 'teacher'
    STUDENT = 'student'
    PARENT = 'parent'
    SysAdmin = 'sysadmin'
    USER_TYPE_CHOICES = (
            (TEACHER, 'Teacher'),
            (STUDENT, 'Student'),
            (PARENT, 'Parent'),
            ('SysAdmin', 'SysAdmin'),
        )
    USER_TYPE_CHOICES1 = (
            (SCHOOL, 'School'),
        )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, help_text="Usertype selection for allauth modularity")

