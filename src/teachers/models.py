from django.db import models
from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) #linking to the account_main_use for allauth authentification and such
    #1. Teacher primary key. an autofield by default in django
    teacher_id = models.AutoField(primary_key=True, help_text="A unique identifier for the teacher in the sys")
    #2. Foreign Key to school
    teacher_school = models.ForeignKey('schools.School',on_delete=models.CASCADE, related_name='teachers', help_text="The school from which teh teacher belongs")
    #3. Official TSC Number
    teacher_tsc_number = models.CharField(max_length=30, unique=True, help_text="Teacher's tsc assigned number")
    # #4. First and Last name
    # teacher_first_name = models.CharField(max_length=100, help_text="Teacher's first name")
    # teacher_last_name = models.CharField(max_length=100, help_text="Teacher's last name")
    # #5. Email for login and notification
    # teacher_email = models.EmailField(max_length=100, unique=True, help_text="Teacher's email for authentication and login")
    #6. Phone Contact
    teacher_phone = models.CharField(max_length=20, help_text="Teacher's phone number")
    #7. Teachers Role "enum"
    ROLE_CHOICES = [ ('Principal', 'Principal'), ('Deputy', 'Deputy'), ('Class Teacher', 'Class Teacher'), ('Subject Teacher', 'Subject Teacher'), ('Patron', 'Patron'), ]
    teacher_role = models.CharField(max_length=30, choices=ROLE_CHOICES , help_text="The title of the teacher in the school")
    # #8. Teachers password for system login
    # teacher_password = models.CharField(max_length=128, help_text="Encrypted teachers password for system login")
    # 9. Teacher's Status - Enum
    STATUS_CHOICES = [ ('Active', 'Active'), ('Suspended', 'Suspended'), ('Retired', 'Retired'), ]
    teacher_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Active', help_text="Teachers employment status")
    #10. Teacher D.O.B optional for HR compliance reporting
    teacher_dob = models.DateField(null=True, blank=True, help_text="Optional D.O.B for compliance reporting ")
    #11. Gender Field 
    GENDER_CHOICES = [ ('Male', 'Male'), ('Female', 'Female'), ]
    teacher_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, help_text="Male or female only ! no binary stuff")
    #12. Date of hire
    teacher_hire_date = models.DateField(help_text="The date that the teacher was hired in the school")
    #13. Timestamps
    teacher_creation_date = models.DateTimeField(auto_now_add=True, help_text="Simply the day the teacher was added into the system")
    teacher_updated_date = models.DateTimeField(auto_now=True, help_text="Last time the record was updated")
    # #14. Override to hash the password if not already hashed
    # def save(self, *args, **kwargs):
    #     if not self.teacher_password.startswith('pbkdf2_'):
    #         self.teacher_password = make_password(self.teacher_password)
    #     super().save(*args, **kwargs)

    #15. return string representation
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.teacher_tsc_number}"