from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import date

# Create your models here.
class Student(models.Model):
    #inherited user style from accounts
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True, help_text="User defined")
    # #1. Primary key for student
    # student_id = models.AutoField(primary_key=True, help_text="A unique identifier for every student in the table")
    #2. Student school
    student_school = models.ForeignKey('schools.School', on_delete=models.CASCADE, null=True, blank=True, related_name='students', help_text="the school the student belongs to")
    #3. The class of the student
    student_class = models.ForeignKey('classes.SchoolClass', on_delete=models.SET_NULL, null=True, blank=True, related_name='students', help_text="the class the student is currently enrolled in")
    #4. Student admission no and assessmet no
    student_admission_number = models.CharField(max_length=30, unique=True, default="XXXXX", help_text="Unique number given to student after registration")
    student_assessment_number = models.CharField(max_length=20, unique=True, default="XXXXX", help_text="Unique number given to the student by the state")
    # #5. Name fields though overridden by the user-inherited model
    # student_first_name = models.CharField(max_length=100, help_text="Student's first name")
    # student_last_name = models.CharField(max_length=100, help_text="Student's last name")
    #6.  Gender
    GENDER_CHOICES = [ ('Male', 'Male'), ('Female', 'Female'), ]
    student_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male', help_text="Students gender i.e male or female no ninary stuff")
    #7.  Student's date of birth
    student_dob = models.DateField(default=date(2000, 1, 1),help_text="Student's date of birth")
    #8. Students contact info phone optional
    # student_email = models.EmailField(max_length=100, null=False, blank=False, help_text="Students email for login")
    student_phone = models.CharField(max_length=20, null=True, blank=True, help_text="Student phone no .i.e optional but recommended")
    # #9. Student login password though overriden by user-inherit
    # student_password = models.CharField(max_length=255, help_text="Encrypted student password")
    #10. Status ENUM
    STATUS_CHOICES = [ ('Active', 'Active'), ('Transferred', 'Transferred'), ('Graduated', 'Graduated'), ('Suspended', 'Suspended'),]
    student_status = models.CharField(max_length=15,choices=STATUS_CHOICES, default='Active', help_text="Student status in school")
    #11. Enrollment date
    student_enrollment_date = models.DateField(default=date.today, help_text="The date the student was enrolled")
    #12. Student parent links
    student_guardian1 = models.ForeignKey('parents.Parent', on_delete=models.SET_NULL, null=True, blank=True, related_name='primay_students', help_text="Primary guardian(1)")
    student_guardian2 = models.ForeignKey('parents.Parent', on_delete=models.SET_NULL, null=True, blank=True, related_name='secondary_students',help_text="Secondary guradian(2)")
    #13. Timestamps i.e created, updated
    student_creation_date = models.DateTimeField( default=timezone.now, help_text="Student record creation timestamp")
    student_update = models.DateTimeField(auto_now=True, help_text="Last record update timestamp")
    # #14. Save method to hash password if not hashed by default
    # def save(self, *args, **kwargs):
    #     if self.student_password and not self.student_password.startswith('pbkdf2_'):
    #         self.student_password = make_password(self.student_password)
    #     super().save(*args, **kwargs)

    #15. string representaion of the class
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.student_admission_number}"
    
