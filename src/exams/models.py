from django.db import models
from datetime import datetime
from django.utils import timezone
import uuid


#funtion to generate random but different exam ids
def generate_unique_exam_id():
    #from exams.models import exam #commented out since are in same file
    while True:
        new_id = f"EXM-{uuid.uuid4().hex[:8].upper()}"
        if not Exam.objects.filter(exam_id=new_id).exists():
            return new_id

# Create your models here.
class Exam(models.Model):
    #1. unique exam identifier
    exam_id = models.CharField(max_length=20, primary_key=True, default=generate_unique_exam_id, help_text="Unique id for each exam")
    #2. exam foreign keys i.e class,course
    exam_course = models.ForeignKey('courses.Course', to_field='course_id', on_delete=models.CASCADE, related_name='exams', help_text="The course the exam is linked to")
    exam_class = models.ForeignKey('classes.SchoolClass', to_field='class_id', on_delete=models.CASCADE, related_name='exams', help_text="Class of exams")
    #3. The name of the exam
    exam_name = models.CharField(max_length=100, help_text="Exam name (e.g., End-Term 1, Zonal CAT 2025).")
    #4. Exam term and academic year
    EXAM_TERM_CHOICES = [ ('Pre-lim', 'Pre-lim'),('Mid-Term', 'Mid-Term'),('End-Term', 'End-Term'),]
    exam_term = models.CharField(max_length=20, choices=EXAM_TERM_CHOICES, help_text="Academic term E.G Term-1. ")
    exam_year = models.IntegerField(default=datetime.now().year, help_text="Year done e.g. 2025")
    #5. Exam Type
    EXAM_TYPE_CHOICES = [('CAT', 'CAT'), ('Internal','Internal'),('Zonal', 'Zonal'), ('National', 'National'), ('Project', 'Project'), ]
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, default='Internal', help_text="Exam type e.g zonal")
    #6. Status
    EXAM_STATUS_CHOICES = [ ('Scheduled', 'Scheduled'), ('Ongoing', 'Ongoing'),    ('Completed', 'Completed'), ]
    exam_status = models.CharField(max_length=20, choices=EXAM_STATUS_CHOICES, default='Scheduled', help_text="Current status of the exam.")
    #7. Timestamps
    exam_creation_date = models.DateTimeField(default=timezone.now, help_text="Exam creation timestamp.")
    exam_updated_date = models.DateTimeField(auto_now=True, help_text="Last time updated")

    #8String representation of the model
    def __str__(self):
        return f"{self.exam_name} | {self.exam_class.class_name} |{self.exam_year} {self.exam_type}"