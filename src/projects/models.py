from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

#funtion to generate random but different project ids
def generate_unique_project_id():
    from .models import Project#from projects.models import Project #commented out since are in same file
    while True:
        new_id = f"PRJ-{uuid.uuid4().hex[:8].upper()}"
        if not Project.objects.filter(project_id=new_id).exists():
            return new_id

# Create your models here.
class Project(models.Model):
    #1. Unique project id for each poject
    project_id = models.CharField(max_length=20, primary_key=True, default=generate_unique_project_id, help_text="Unique identifier for the project.")
    #2. foreign keys, i.e student , subject and teacher
    project_student = models.ForeignKey('students.Student', to_field='student_id', on_delete=models.CASCADE, related_name='projects', help_text="Student assigned the project.")
    project_subject = models.ForeignKey('subjects.Subject', to_field='subject_id', on_delete=models.CASCADE, related_name='projects', help_text="Subject linked to the project.")
    project_class = models.ForeignKey('classes.SchoolClass', to_field='class_id', on_delete=models.CASCADE, related_name='projects', help_text="Class assigned with the project")
    project_teacher = models.ForeignKey('teachers.Teacher', to_field='teacher_id', on_delete=models.SET_NULL, null=True, blank=True, related_name='supervised_projects', help_text="Teacher supervising the projects")
    #3. Project info
    project_title = models.CharField(max_length=200, help_text="Project title.")
    project_description = models.TextField(blank=True, help_text="Details of the project.")
    #4. Project grading info
    project_score = models.DecimalField( max_digits=4, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Score awarded (0.00 to 100.00).")
    project_max_score = models.PositiveIntegerField( default=0, help_text="Possible maximum score")
    project_percentage_score = models.PositiveIntegerField( default=0, help_text="Project percentage score")
    #9. Academic context
    PROJECT_TERM_CHOICES = [ ('Pre-lim', 'Pre-lim'),('Mid-Term', 'Mid-Term'),('End-Term', 'End-Term'),]
    project_term = models.CharField(max_length=20, db_index=True, choices=PROJECT_TERM_CHOICES, help_text="Academic term E.G Mid-Term. ")
    project_year = models.IntegerField(default=datetime.now().year, db_index=True, help_text="Year done e.g. 2025")
    #10 project timestamps
    project_creation_date = models.DateTimeField(default=timezone.now, help_text="Submission date.")
    project_update_date = models.DateTimeField(auto_now=True, help_text="When the project was marked.")

    #11. Return string for the project
    def __str__(self):
        return f"{self.project_title} | {self.project_student} | {self.project_year} | {self.project_term}"