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
# ======================================
# 1. Communication Model
# ======================================
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

#communication group model
# ======================================
# 1. CommunicationGroups Model
# ======================================
#funtion to generate random but different communication ids
def generate_unique_group_id():
    from .models import CommunicationGroup#from comms.models import CommunicationGroup #commented out since from the same file
    while True:
        new_id = f"CGP-{uuid.uuid4().hex[:8].upper()}"
        if not CommunicationGroup.objects.filter(communication_group_id=new_id).exists():
            return new_id
      
class CommunicationGroup(models.Model):
    #1. Inherited communication id for the group
    communication_group_id = models.CharField(max_length=20,primary_key=True, default=generate_unique_group_id, help_text="Uique group ID")
    #2. group details
    communication_group_name = models.CharField(max_length=100, unique=True, help_text="Group name e.g. 'Grade 7 Parents'")
    communication_group_description = models.TextField(null=True, blank=True, help_text="Details about the group")
    #3. group owner details
    communication_group_creator = models.ForeignKey('teachers.Teacher', to_field='teacher_id', on_delete=models.CASCADE, help_text="Creator (Teacher or School_Admin)")
    # communication_group_creator_role = models.CharField(max_length=20, choices=[('Teacher', 'Teacher'), ('School_Admin', 'School_Admin')], help_text="Role of creator")
    #4. group creation timestamp
    communication_group_creation_date = models.DateTimeField(default=timezone.now, help_text="Date the group was created")

    #5. return string for the group
    def __str__(self):
        return f"{self.communication_group_name} (Created by {self.communication_group_creator.teacher_role} {self.communication_group_creator.user.first_name})"

    class Meta:
        verbose_name = "Communication Group"
        verbose_name_plural = "Communication Groups"
        ordering = ['-communication_group_creation_date']

#communication group members models to allow many to many
# ======================================
# 1. CommunicationGroupMembers Model
# ======================================
class CommunicationGroupMember(models.Model):
    #1. group where the member belongs to 
    communicator_group = models.ForeignKey('comms.CommunicationGroup', to_field='communication_group_id', on_delete=models.CASCADE, related_name='members', help_text='The group of belonging')
    #2. group member detail and roles
    communicator_member_id = models.CharField(max_length=20, help_text="Member ID")
    communicator_role = models.CharField(max_length=20, choices=[('Teacher', 'Teacher'),('Parent', 'Parent'),('Student', 'Student'), ('School_Admin', 'School_Admin'),])
    communicator_status = models.CharField(max_length=20, choices=[('Admin', 'Admin'), ('Member', 'Member'), ], default='Member')
    #3. Member.join.date
    communicator_join_date = models.DateTimeField(default=timezone.now)

    #4. return string for the  member model
    def __str__(self):
        return f"{self.communicator_role} {self.communicator_member_id} in {self.communicator_group.communication_group_name}"


    #4. to avoid duplications
    class Meta:
        unique_together = ('communicator_group', 'communicator_member_id')