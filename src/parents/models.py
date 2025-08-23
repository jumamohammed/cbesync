from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import uuid

#funtion to generate random but different parent ids
def generate_unique_parent_id():
    from parents.models import Parent
    while True:
        new_id = f"PAR-{uuid.uuid4().hex[:8].upper()}"
        if not Parent.objects.filter(parent_id=new_id).exists():
            return new_id

# Create your models here.
class Parent(models.Model):
    #Inherited user model for django allauth stuff
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True, help_text="inherited user account")
    #1. parent identifier id
    parent_id = models.CharField(primary_key=True,max_length=20, default=generate_unique_parent_id, editable=False, help_text="parent identifer in the system")
    # #3. parent names
    # parent_first_name = models.CharField(max_length=100, help_text="Parent first name")
    # parent_last_name = models.CharField(max_length=100, help_text="parent last name")
    #3. parent contact info
    # parent_email = models.EmailField(max_length=100, help_text="Parent email")
    parent_phone = models.CharField(max_length=15,default="07", help_text="primary phonenumber for communication")
    #4. parent password for login though overriden by user
    # parent_password = models.CharField(max_length=128, help_text="encrypted parentpassword")
    #5. Relationship to student
    RELATIONSHIP_CHOICES = [ ('Father', 'Father'), ('Mother', 'Mother'), ('Guardian', 'Guardian'), ('Sponsor', 'Sponsor'), ('Other', 'Other'), ]
    parent_relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES,default='Father', help_text="Parents relationship to children")
    #6. Parent status
    STATUS_CHOICES = [ ('Active', 'Active'), ('Suspended', 'Suspended'), ('Deleted', 'Deleted'), ]
    parent_status = models.CharField(max_length=15,default='Suspended', choices=STATUS_CHOICES, help_text="parent's status in the system")
    #7. Parent address
    parent_address = models.CharField(max_length=255, null=True, unique=True, help_text="Home address or location")
    #8. Timestamps i.e creation date and last update
    parent_creation_date = models.DateTimeField(default=timezone.now, help_text="Day on added to system" )
    parent_updated_date = models.DateTimeField(auto_now=True, help_text="Last time record was updated ")
    # #9. password hashing when managed locally
    # def save(self, *args, **kwargs):
    #     if self.parent_password and not self.parent_password.startswith('pbkdf2_'):
    #         self.parent_password = make_password(self.parent_password)
    #     super().save(*args, **kwargs)
    #10. return string when parent referenced
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.parent_relationship}"