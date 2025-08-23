from django.db import models
from django.utils import timezone
import uuid

#funtion to generate random but different course
def generate_unique_course_id():
    from courses.models import Course
    while True:
        new_id = f"SCH-{uuid.uuid4().hex[:8].upper()}"
        if not Course.objects.filter(course_id=new_id).exists():
            return new_id
# Create your models here.
class Course(models.Model):
    #1. unique course id for the courses in the schools
    course_id = models.CharField(max_length=20, primary_key=True, default=generate_unique_course_id, editable=False, help_text="Unique course id for each in the school")
    #2. school of the course
    course_school = models.ForeignKey('schools.School', to_field='school_id', on_delete=models.CASCADE, related_name='courses', help_text="Courses offered in the schools")
    #3. the name of the course
    COURSES_OPTIONS = [('PRE-PRIMARY-EDUCATION', 'PRE-PRIMARY-EDUCATION'),('JUNIOR-SECONDARY-EDUCATION','JUNIOR-SECONDARY-EDUCATION'),('SENIOR-SECONDARY-EDUCATION','SENIOR-SECONDARY-EDUCATION'),('OTHER', 'OTHER')]
    course_name = models.CharField(max_length=50, unique=True,choices=COURSES_OPTIONS, help_text="Name of the course")
    #4. course description
    course_description = models.TextField(null=True, blank=True, help_text="Course description")
    #5. course level to be taken ..jss, ppr, sss,,
    course_level = models.ForeignKey('classes.SchoolClass', on_delete=models.SET_NULL,null=True, to_field='class_level', help_text="The level of the course")
    #6.  Status
    STATUS_CHOICES = [ ('Available', 'Available'), ('Unavailable', 'Unavailable'), ]
    course_status = models.CharField(max_length=15, choices=STATUS_CHOICES, help_text="Availability or unavailability of the course")
    #7. Timestamps for when the course was created
    course_creation_date = models.DateTimeField(default=timezone.now, help_text="The time when the course was created")
    course_update_date = models.DateTimeField(auto_now=True, help_text="The last record update")
    #8. Return string for the course
    def __str__(self):
        return f"{self.course_name} - ({self.course_level}) - {self.course_school.school_name}"