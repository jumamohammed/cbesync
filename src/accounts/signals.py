from allauth.account.signals import user_signed_up, user_logged_in
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
    Redirects user after successful login based on their user_type.
    """
    if user.user_type == CustomUser.SCHOOL:
        return redirect('schools:dashboard')  # Redirect to school dashboard
    
    elif user.user_type == CustomUser.STUDENT:
        return redirect('students:dashboard')  # Redirect to student dashboard
    
    elif user.user_type == CustomUser.TEACHER:
        return redirect('teachers:dashboard')  # Redirect to teacher dashboard
    
    # Default case for other user types or unexpected ones
    return redirect('home')  # Redirect to the home page
