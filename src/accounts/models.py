from django.db import models, connection
from django.contrib.auth.models import AbstractUser
import uuid

# Function to check if table exists
def table_exists(table_name):
    return table_name in connection.introspection.table_names()

# Function to generate unique user ID
def generate_unique_user_id():
    new_id = uuid.uuid4()
    if table_exists("accounts_customuser"):
        from .models import CustomUser
        while CustomUser.objects.filter(id=new_id).exists():
            new_id = uuid.uuid4() 
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
 # Primary key
    id = models.UUIDField(primary_key=True, default=generate_unique_user_id, editable=False)
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES,default=SCHOOL, help_text="User type selection for allauth modularity")
