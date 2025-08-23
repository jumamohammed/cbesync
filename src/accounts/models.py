from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

# Create your models here

#this is a custom user class or rather table for scalability to advanced types
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
            ('school', 'School'),
            ('teacher', 'Teacher'),
            ('student', 'Student'),
            ('parent', 'Parent'),
            ('SysAdmin', 'SysAdmin'),
        )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, help_text="Usertype selection for allauth modularity")

