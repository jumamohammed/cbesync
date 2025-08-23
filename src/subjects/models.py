from django.db import models
from django.utils import timezone
import uuid

#funtion to generate random but different subject id
def generate_unique_subject_id():
    from subjects.models import Subject
    while True:
        new_id = f"SBJ-{uuid.uuid4().hex[:8].upper()}"
        if not Subject.objects.filter(subject_id=new_id).exists():
            return new_id

# Create your models here.
class Subject(models.Model):
    #1. subject id for every subjec
    subject_id = models.CharField(max_length=20, default=generate_unique_subject_id, primary_key=True, help_text="Subject ID")
    #2. the course containing the subject
    subject_course = models.ForeignKey('courses.Course', to_field='course_id', on_delete=models.CASCADE, related_name='subjects', help_text="Course of the subject")
    #3. the name of the course
    subject_name = models.CharField(max_length=100, help_text='This is the name of the subject')
    #4. Subject code i.e short name e.g CIT-001
    subject_code = models.CharField(max_length=20, unique=True, null=True, blank=True, help_text="Program short code e.g CIT-001")
    #5. A Subject description
    subject_description = models.TextField(max_length=300, null=True, blank=True, help_text="Description of the subject")
    #6. Status
    STATUS_CHOICES = [('Available', 'Available'), ('Unavailable', 'Unavailable'),]
    subject_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available', help_text="Aailable for registration or !")
    #7. Timestamps
    subject_creation_date = models.DateTimeField(default=timezone.now, help_text="Subject creation Timestamp")
    subject_update_date = models.DateTimeField(auto_now=True, help_text="Subject last updated Timestamp")
    #8. Subject Representation
    def __str__(self):
        return f"{self.subject_name} - {self.subject_code} - {self.subject_course}"