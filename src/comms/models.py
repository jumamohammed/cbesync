from django.db import models
from django.utils import timezone
import uuid

#funtion to generate random but different communication ids
def generate_unique_communication_id():
    from .models import Communication#from comms.models import Communication #commented out since from the same file
    while True:
        new_id = f"CMN-{uuid.uuid4().hex[:8].upper()}"
        if not Communication.objects.filter(communication_id=new_id).exists():
            return new_id
# Create your models here.
class Communication(models.Model):
    #1. Communication id for every communication in the table
    communication_id = models.CharField(max_length=20, primary_key=True, default=generate_unique_communication_id, help_text="Unique communication id for every comm in the table")
    #2. sender details
    COMM_ROLE_CHOICES = [ ('Teacher', 'Teacher'), ('Parent', 'Parent'), ('Student', 'Student'), ('School_Admin', 'School_Admin'),]
    communication_sender_id = models.CharField(max_length=20, help_text="This is the id of the sender")
    communication_sender_role = models.CharField(max_length=20, choices=COMM_ROLE_CHOICES, help_text="Role of the sender")
    #3. Recipient roles
    communication_recipient_id = models.CharField(max_length=20, help_text="ID of the recipient in the communiccaation")
    communication_recipient_role = models.CharField(max_length=20, choices=COMM_ROLE_CHOICES  +  [('Group', 'Group')], help_text="Role of the recipient")
    #4. Communication_key details
    communication_subject = models.CharField(max_length=200, help_text="Subject or title of the communication")
    communication_message = models.TextField(max_length=1000, help_text="Message to send")
    #5. communication type specifity
    COMM_TYPE_CHOICES = [ ('Message', 'Message'), ('Notification', 'Notification'), ('Reminder', 'Reminder'), ('Alert', 'Alert'), ]
    COMM_STATUS_CHOICES = [ ('Sent', 'Sent'), ('Delivered', 'Delivered'), ('Read', 'Read'), ]
    COMM_PRIORITY_CHOICES = [ ('Normal', 'Normal'), ('High', 'High'),  ('Urgent', 'Urgent'), ]
    communication_type = models.CharField(max_length=20, choices=COMM_TYPE_CHOICES, default='Message', help_text="Type of communication")
    communication_status = models.CharField(max_length=20, choices=COMM_STATUS_CHOICES, default='Sent', help_text="Delivery status of the communication")
    communication_priority = models.CharField(max_length=20, choices=COMM_PRIORITY_CHOICES, default='Normal', help_text="Priority of the communication")   
    #6. Communication timestamps
    communication_creation_time = models.DateTimeField(default=timezone.now,db_index=True, help_text="Timestamp when the message was created")
    communication_read_time = models.DateTimeField(null=True, blank=True, help_text="The time when the message was read")

    #7. return string of the comm models
    def __str__(self):
        return f"{self.communication_type}: {self.communication_subject} from {self.communication_sender_role}({self.communication_sender_id}) to {self.communication_recipient_role}({self.communication_recipient_id})"
    #8. ordering of the messager
    class Meta:
        ordering = ['-communication_creation_time']