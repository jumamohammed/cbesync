from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #1. Teacher primary key. an autofield by default in django
    teacher_id = models.AutoField(primary_key=True, help_text="A unique identifier for the teacher in the sys")
    #2. Foreign Key to school
    teacher_school = models.ForeignKey('schools.School',on_delete=models.CASCADE, related_name='teachers', help_text="The school from which teh teacher belongs")
    #3. Official TSC Number
    tsc_number = models.CharField(max_length=30, unique=True, help_text="Teacher's tsc assigned number")
    #4. 