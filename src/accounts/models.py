from django.db import models, connection
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
import uuid

#function to check tables' existence
def table_exists(table_name):
    return table_name in connection.introspection.table_names()
#function to generate unique user id
def generate_unique_user_id():
    new_id = f"USR-{uuid.uuid4().hex[:10].upper()}"
    if table_exists("accounts_customuser"):
        from .models import CustomUser
        while CustomUser.objects.filter(user_id=new_id).exists():
            new_id = f"USR-{uuid.uuid4().hex[:10].upper()}"
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

