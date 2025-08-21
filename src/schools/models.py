from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

# Create your models here.
#this is a school class(table in short)
class School(models.Model):
    #unique school code max 20 char
    school_code = models.CharField(max_length=20, unique=True, help_text="Official MOE school code.")
    #official school name
    school_name = models.CharField(max_length=150, help_text="Official school name.")
    #school type enum
    SCHOOL_TYPES_CHOICES = [ ('Pre-Pri', 'Pre-Pri'), ('Primary', 'Primary'), ('Junior-SS', 'Junior-SS'), ('Senior-SS', 'Senior-SS'), ('Internatioanal', 'Internatioanal'),]
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPES_CHOICES, help_text="Type of school i.e P-PR,JSS,SSC,")
    #school category enum
    CATEGORY_CHOICES = [ ('Day', 'Day'), ('Boarding', 'Boarding'), ('Day & Boarding', 'Day & Boarding'),]
    school_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, help_text="School Category i.e public, private")
    # 5. Ownership (enum)
    OWNERSHIP_CHOICES = [('Public', 'Public'), ('Private', 'Private'), ('Community', 'Community'), ('Mission', 'Mission'), ('Others', 'Others'), ]
    school_ownership = models.CharField(max_length=20, choices=OWNERSHIP_CHOICES, help_text="School ownership i.e Public, Private")
    # 6. Admins: this should be a relationship, not just a field
    school_admins = models.TextField(help_text="Comma separated list of admins username/emails-simplified for now")
    #7.Location fields
    school_county = models.CharField(max_length=50, help_text="County where the school is located.")
    school_subcouty = models.CharField(max_length=50, help_text="Sub-county for finer location granularity.")
    school_ward = models.CharField(max_length=50, blank=True, null=True, help_text="Optional ward fill for zonal exams management")
    school_location = models.CharField(max_length=255, help_text="Location of school residence.")
    #8. Contact fields
    school_email = models.EmailField(max_length=100, help_text="Official school email")
    school_phone = models.CharField(max_length=20, help_text="Official  School tell NO.")
    #9. School status in the site
    STATUS_CHOICES = [ ('Pending', 'Pending Validation'), ('Active', 'Active'), ('Suspended', 'Suspended')]
    school_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', help_text="School_status on the platform e.g Verified")
    #10. School name(topadmin)
    school_principal = models.CharField(max_length=100, help_text="Name of the toplevel Admin")
    #11. School password i.e hashed school password
    school_password = models.CharField(max_length=128, help_text="Hashed school login password")
    #12. Timestamps
    school_creation_date = models.DateTimeField(auto_now_add=True, help_text="Creation date/time stamp")
    school_updated_date = models.DateTimeField(auto_now=True, help_text="Last Modification timestamp")

    #automatically save and hash the password if not hashed
    def save(self, *args, **kwargs):
        #hash the unhashed password
        if not self.school_password.startswith('pbkdf2_'):
            self.school_password = make_password(self.school_password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.school_name} {self.school_code}"