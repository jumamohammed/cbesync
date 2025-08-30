# accounts/signals.py
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from accounts.models import CustomUser
from schools.models import School
from teachers.models import Teacher 
from students.models import Student
from parents.models import Parent

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    data = request.POST  # Access form data

    if user.user_type == CustomUser.SCHOOL:
        # Check if a school with this school_code already exists
        school_code = data.get('school_code')
        school = School.objects.filter(school_code=school_code).first()

        if not school:
            # If no existing school found, create a new one
            School.objects.create(
                user=user,
                school_code=school_code,
                school_name=data.get('school_name'),
                school_type=data.get('school_type'),
                school_category=data.get('school_category'),
                school_ownership=data.get('school_ownership'),
                school_admins=data.get('school_admins'),
                school_county=data.get('school_county'),
                school_subcounty=data.get('school_subcounty'),
                school_ward=data.get('school_ward', ''),
                school_location=data.get('school_location'),
                school_phone=data.get('school_phone'),
                school_principal=data.get('school_principal'),
            )
        else:
            # Optionally, update the school if needed (e.g., if any school data is updated)
            school.school_name = data.get('school_name', school.school_name)
            school.school_type = data.get('school_type', school.school_type)
            school.school_category = data.get('school_category', school.school_category)
            school.save()  # Save updated fields if necessary

    elif user.user_type == CustomUser.TEACHER:
        Teacher.objects.create(user=user)

    elif user.user_type == CustomUser.STUDENT:
        Student.objects.create(user=user)

    elif user.user_type == CustomUser.PARENT:
        Parent.objects.create(user=user)
