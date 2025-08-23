from django.db import models
from django.utils import timezone
import uuid

#funtion to generate random but different student ids
def generate_unique_club_id():
    from .models import Club#from clubs.models import Club #commented out since from the same file
    while True:
        new_id = f"CLB-{uuid.uuid4().hex[:8].upper()}"
        if not Club.objects.filter(club_id=new_id).exists():
            return new_id


# Create your models here.
class Club(models.Model):
    #1. club ID that is unique to every cub in the school
    club_id = models.CharField(primary_key=True, max_length=20, default=generate_unique_club_id ,editable=False, help_text="A unique identifier for every club in the school")
    #2. school to which the club belongs
    club_school = models.ForeignKey('schools.School', to_field='school_id', on_delete=models.CASCADE, related_name='clubs', help_text="the school ownign the club")
    #3. Club name
    club_name = models.CharField(max_length=100, unique=True, help_text="Name of the club e.g Drama, Science")
    #4. Club description
    club_description = models.TextField(max_length=300 ,null=True, blank=True, help_text="Short description of the club")
    #5. Club patron i.e a teacher responsible for the club
    club_patron = models.ForeignKey('teachers.Teacher', to_field='teacher_id', on_delete=models.SET_NULL, null=True, blank=True, related_name="patron_clubs", help_text="The patron of the club")
    #6. Status choices
    STATUS_CHOICES = [ ('Active', 'Active'), ('Inactive', 'Inactive'),]
    club_status = models.CharField(max_length=20, choices=STATUS_CHOICES, db_index=True, default='Active', help_text="whether the club is active/inactive")
    #7. Timestmps for creation and update
    club_creation_date = models.DateField(default=timezone.now, help_text="clubs creation timestamp")
    club_update_date = models.DateTimeField(auto_now=True, help_text="Last time the club was updated")
    #8. string representation of the club
    def __str__(self):
        return f"{self.club_name} - ({self.club_school.school_name})"
