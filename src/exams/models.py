from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid


#funtion to generate random but different exam ids
def generate_unique_exam_id():
    from .models import Exam#from exams.models import exam #commented out since are in same file
    while True:
        new_id = f"EXM-{uuid.uuid4().hex[:8].upper()}"
        if not Exam.objects.filter(exam_id=new_id).exists():
            return new_id

# Create your models here.
class Exam(models.Model):
    #1. unique exam identifier
    exam_id = models.CharField(max_length=20, primary_key=True, default=generate_unique_exam_id, help_text="Unique id for each exam")
    #2. exam foreign keys i.e class,course,student,teacher
    exam_student = models.ForeignKey('students.Student', to_field='student_id', null=True, on_delete=models.CASCADE, related_name='exams', help_text="Student assigned the exam.")
    exam_course = models.ForeignKey('courses.Course', to_field='course_id', on_delete=models.CASCADE, related_name='exams', help_text="The course the exam is linked to")
    exam_class = models.ForeignKey('classes.SchoolClass', to_field='class_id', on_delete=models.CASCADE, related_name='exams', help_text="Class of exams")
    exam_subject = models.ForeignKey('subjects.Subject', to_field='subject_id', on_delete=models.CASCADE,null=True, related_name='exams', help_text="The subject whose exam is")
    exam_teacher = models.ForeignKey('teachers.Teacher', to_field='teacher_id', on_delete=models.SET_NULL, null=True, blank=True, related_name='supervised_exams', help_text="Teacher supervising the exam")

    #3. The name of the exam
    exam_name = models.CharField(max_length=100, help_text="Exam name (e.g., End-Term 1, Zonal CAT 2025).")
    #4. Exam term and academic year
    EXAM_TERM_CHOICES = [ ('Pre-lim', 'Pre-lim'),('Mid-Term', 'Mid-Term'),('End-Term', 'End-Term'),]
    exam_term = models.CharField(max_length=20, db_index=True, choices=EXAM_TERM_CHOICES, help_text="Academic term E.G Mid-Term. ")
    exam_year = models.IntegerField(default=datetime.now().year, db_index=True, help_text="Year done e.g. 2025")
    #5. Exam Type and max_score
    EXAM_TYPE_CHOICES = [('CAT', 'CAT'), ('Internal','Internal'),('Zonal', 'Zonal'), ('National', 'National'), ('Project', 'Project'), ]
    exam_type = models.CharField(max_length=20, db_index=True, choices=EXAM_TYPE_CHOICES, default='Internal', help_text="Exam type e.g zonal")
    #5.1. exam grading info
    exam_score = models.DecimalField( max_digits=4, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Score awarded (0.00 to 100.00).")
    exam_max_score = models.PositiveIntegerField( default=0, help_text="Possible  maximum score")
    exam_percentage_score = models.PositiveIntegerField( default=0, help_text="Exam percentage score")
    #6. Status
    EXAM_STATUS_CHOICES = [ ('Scheduled', 'Scheduled'), ('Ongoing', 'Ongoing'),    ('Completed', 'Completed'), ]
    exam_status = models.CharField(max_length=20, choices=EXAM_STATUS_CHOICES, default='Scheduled', help_text="Current status of the exam.")
    #7. Timestamps
    exam_creation_date = models.DateTimeField(default=timezone.now, db_index=True, help_text="Exam creation timestamp.")
    exam_updated_date = models.DateTimeField(auto_now=True, help_text="Last time updated")

    #8String representation of the model
    def __str__(self):
        return f"{self.exam_name} | {self.exam_class.class_name} | {self.exam_year} ({self.exam_type})"
    #9. Meta classes for uniquesness
    class Meta:
        unique_together = ('exam_course', 'exam_class', 'exam_name', 'exam_year')
