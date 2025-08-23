from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid

#funtion to generate random but different cat ids
def generate_unique_cat_id():
    from .models import Cat#from cats.models import cat #commented out since are in same file
    while True:
        new_id = f"CAT-{uuid.uuid4().hex[:8].upper()}"
        if not Cat.objects.filter(cat_id=new_id).exists():
            return new_id

# Create your models here.
class Cat(models.Model):
    #1. the primary key for the table
    cat_id = models.CharField(max_length=20, primary_key=True, default=generate_unique_cat_id, help_text="A unique id for each cat")
    #2. cat foreign keys, course, class, subject and teacher
    cat_student = models.ForeignKey('students.Student', to_field='student_id', null=True, on_delete=models.CASCADE, related_name='cats', help_text="Student assigned the cat.")
    cat_course = models.ForeignKey('courses.Course', to_field='course_id', on_delete=models.CASCADE, related_name='cats', help_text="Course associated with the cat")
    cat_class = models.ForeignKey('classes.SchoolClass', to_field='class_id', on_delete=models.CASCADE, related_name='cats', help_text="Class associated with the cat")
    cat_subject = models.ForeignKey('subjects.Subject', to_field='subject_id', on_delete=models.CASCADE, related_name='cats', help_text="Subject associated with the cat")
    cat_teacher = models.ForeignKey('teachers.Teacher', to_field='teacher_id', null= True, on_delete=models.SET_NULL, related_name='supervised_cats', help_text="Teacher associated with the cat")
    #3.cat name
    cat_name = models.CharField(max_length=100, help_text="CAT name (e.g., CAT1, CAT2, Weekly Test).")
    #4. cat term and academic year
    CAT_TERM_CHOICES = [ ('Pre-lim', 'Pre-lim'),('Mid-Term', 'Mid-Term'),('End-Term', 'End-Term'),]
    cat_term = models.CharField(max_length=20, db_index=True, choices=CAT_TERM_CHOICES, help_text="Academic term E.G Mid-Term. ")
    cat_year = models.IntegerField(default=datetime.now().year, db_index=True, help_text="Year done e.g. 2025")
    #8. cat grading info
    cat_score = models.DecimalField( max_digits=4, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Score awarded (0.00 to 100.00).")
    cat_max_score = models.PositiveIntegerField( default=0, help_text="Possible maximum score")
    cat_percentage_score = models.PositiveIntegerField( default=0, help_text="Cat percentage score")
    #6 cat creation and last time of update
    cat_creation_date = models.DateTimeField(default=timezone.now, help_text="Date cat was taken")
    cat_updated_date = models.DateTimeField(auto_now=True, help_text="Last time cat record was updated")
    #7. return string 
    def __str__(self):
        return f"{self.cat_name} | {self.cat_subject.subject_name} | {self.cat_year} | {self.cat_term}"