#accounts/signals.py
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from accounts.models import CustomUser
from schools.models import School
from teachers.models import Teacher 
from students.models import Student
from parents.models import Parent

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    if user.user_type == 'school':
        School.objects.create(user=user)
    elif user.user_type == 'teacher':
        Teacher.objects.create(user=user)
    elif user.user_type == 'student':
        Student.objects.create(user=user)
    elif user.user_type == 'parent':
        Parent.objects.create(user=user)