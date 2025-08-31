from allauth.account.signals import user_signed_up, user_logged_in
from django.urls import reverse
from django.dispatch import receiver
from accounts.models import CustomUser
from schools.models import School
from teachers.models import Teacher
from students.models import Student
from parents.models import Parent
from django.db import IntegrityError
import logging
#secifics for auth redirections
from django.shortcuts import redirect

# Set up logging
logger = logging.getLogger(__name__)

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    try:
        if user.user_type == CustomUser.SCHOOL:
            _, created = School.objects.get_or_create(user=user)
            if created:
                logger.info(f"Created a new School profile for {user.email}")
            else:
                logger.info(f"School profile already exists for {user.email}")

        elif user.user_type == CustomUser.TEACHER:
            _, created = Teacher.objects.get_or_create(user=user)
            if created:
                logger.info(f"Created a new Teacher profile for {user.email}")
            else:
                logger.info(f"Teacher profile already exists for {user.email}")

        elif user.user_type == CustomUser.STUDENT:
            _, created = Student.objects.get_or_create(user=user)
            if created:
                logger.info(f"Created a new Student profile for {user.email}")
            else:
                logger.info(f"Student profile already exists for {user.email}")

        elif user.user_type == CustomUser.PARENT:
            _, created = Parent.objects.get_or_create(user=user)
            if created:
                logger.info(f"Created a new Parent profile for {user.email}")
            else:
                logger.info(f"Parent profile already exists for {user.email}")

        else:
            logger.warning(f"Unknown user type {user.user_type} for user {user.email}")

    except IntegrityError as e:
        logger.error(f"IntegrityError during profile creation for {user.email}: {str(e)}")
    except Exception as e:
        logger.error(f"Error creating profile for user {user.email}: {str(e)}")




#signal to redirect the logged in user to a certain page
@receiver(user_logged_in)
def redirect_based_on_user_type(sender, request, user, **kwargs):
    """
    Store the redirection URL in the session after successful login based on user_type.
    """
    if user.is_authenticated:
        user_type = user.user_type  # Fetch from the user object      
        # Store the redirection URL based on the user type
        if user_type == CustomUser.SCHOOL:
            redirect_url = reverse('schools:dashboard')
            print(f'Redirecting to: {redirect_url}')
            request.session['redirect_url'] = redirect_url  # Store URL in session
        elif user_type == CustomUser.STUDENT:
            redirect_url = reverse('students:dashboard')
            request.session['redirect_url'] = redirect_url
        elif user_type == CustomUser.TEACHER:
            redirect_url = reverse('teachers:dashboard')
            request.session['redirect_url'] = redirect_url
        elif user_type == CustomUser.PARENT:
            redirect_url = reverse('parents:dashboard')
            request.session['redirect_url'] = redirect_url
        else:
            request.session['redirect_url'] = reverse('home')
