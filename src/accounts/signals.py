from allauth.account.signals import user_signed_up, user_logged_in
from django.urls import reverse
from django.dispatch import receiver
from accounts.models import CustomUser
from schools.models import School
from teachers.models import Teacher
from students.models import Student
from parents.models import Parent
import logging
#secifics for auth redirections
from django.shortcuts import redirect

# Set up logging
logger = logging.getLogger(__name__)

@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    try:
        # Check the user type and create the corresponding profile
        if user.user_type == CustomUser.SCHOOL:
            # For schools, you might want to ensure that required school fields are set before creating
            school = School.objects.create(user=user)
            logger.info(f"Created a new School profile for {user.email}")
        
        elif user.user_type == CustomUser.TEACHER:
            # You might want to validate teacher-specific fields here
            teacher = Teacher.objects.create(user=user)
            logger.info(f"Created a new Teacher profile for {user.email}")
        
        elif user.user_type == CustomUser.STUDENT:
            # Ensure student-specific fields are set if necessary
            student = Student.objects.create(user=user)
            logger.info(f"Created a new Student profile for {user.email}")
        
        elif user.user_type == CustomUser.PARENT:
            # Validate parent's data if required
            parent = Parent.objects.create(user=user)
            logger.info(f"Created a new Parent profile for {user.email}")
        
        else:
            # If an unknown user type is found, log it as a warning
            logger.warning(f"Unknown user type {user.user_type} for user {user.email}")
        
    except Exception as e:
        # Log any error that happens during profile creation
        logger.error(f"Error creating profile for user {user.email}: {str(e)}")
        # Optionally, handle the error (e.g., send an email to admins, show error to user, etc.)




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
