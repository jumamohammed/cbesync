from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
import uuid

#function to generate unique user is
def generate_unique_user_id():
    from .models import CustomUser
    while True:
        new_id = f"USR-{uuid.uuid4().hex[:10].upper()}"
        if not CustomUser.objects.filter(user_id=new_id).exists():
            return new_id

# Create your models here

#this is a custom user class or rather table for scalability to advanced types
class CustomUser(AbstractUser):
    SCHOOL = 'school'
    TEACHER = 'teacher'
    STUDENT = 'student'
    PARENT = 'parent'
    SYSADMIN = 'sysadmin'
    
    USER_TYPE_CHOICES = (
            (TEACHER, 'Teacher'),
            (STUDENT, 'Student'),
            (SCHOOL, 'School'),
            (PARENT, 'Parent'),
            (SYSADMIN, 'Sysadmin'),
        )
    USER_TYPE_CHOICES1 = (
            (SCHOOL, 'School'),
        )
    #primary key custom and teh field in every model
    user_id = models.CharField(primary_key=True, max_length=20, default=generate_unique_user_id, editable=False, help_text="Unique User id")
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, help_text="Usertype selection for allauth modularity")

