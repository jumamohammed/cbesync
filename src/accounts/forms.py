from allauth.account.forms import SignupForm
from django import forms
from django.db import transaction, IntegrityError
from accounts.models import CustomUser
from schools.models import School
import logging

logger = logging.getLogger(__name__)

#custom signup form for school registration
class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES1)

    # School fields
    school_code = forms.CharField(required=False)
    school_name = forms.CharField(required=False)
    school_type = forms.ChoiceField(choices=School.SCHOOL_TYPES_CHOICES, required=False)
    school_category = forms.ChoiceField(choices=School.CATEGORY_CHOICES, required=False)
    school_ownership = forms.ChoiceField(choices=School.OWNERSHIP_CHOICES, required=False)
    school_admins = forms.CharField(required=False)
    school_county = forms.CharField(required=False)
    school_subcounty = forms.CharField(required=False)
    school_ward = forms.CharField(required=False)
    school_location = forms.CharField(required=False)
    school_phone = forms.CharField(required=False)
    school_principal = forms.CharField(required=False)

    #custom form validation
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        # If registering as a school, validate required fields
        if user_type == CustomUser.SCHOOL:
            required_fields = [
                'school_code', 'school_name', 'school_type', 'school_category',
                'school_ownership', 'school_admins', 'school_county', 'school_subcounty',
                'school_location', 'school_phone', 'school_principal', 'school_ward'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f"{field.replace('_', ' ').capitalize()} is required for school registration.")

            school_code = cleaned_data.get('school_code')
            if school_code and School.objects.filter(school_code=school_code).exists():
                self.add_error('school_code', 'This school code is already taken.')

        return cleaned_data
    #form data save when no failure
    def save(self, request):
        try:
            with transaction.atomic():
                # Save the user
                user = super().save(request)
                user.user_type = self.cleaned_data['user_type']
                user.save()

                # Handle school creation
                if user.user_type == CustomUser.SCHOOL:
                    # Check if this user already has a school
                    if School.objects.filter(user=user).exists():
                        raise forms.ValidationError("This user already has an associated school.")

                    school_code = self.cleaned_data.get('school_code')
                    existing_school = School.objects.filter(school_code=school_code).first()

                    if not existing_school:
                        # Create new school
                        School.objects.create(
                            user=user,
                            school_code=school_code,
                            school_name=self.cleaned_data.get('school_name'),
                            school_type=self.cleaned_data.get('school_type'),
                            school_category=self.cleaned_data.get('school_category'),
                            school_ownership=self.cleaned_data.get('school_ownership'),
                            school_admins=self.cleaned_data.get('school_admins'),
                            school_county=self.cleaned_data.get('school_county'),
                            school_subcounty=self.cleaned_data.get('school_subcounty'),
                            school_ward=self.cleaned_data.get('school_ward'),
                            school_location=self.cleaned_data.get('school_location'),
                            school_phone=self.cleaned_data.get('school_phone'),
                            school_principal=self.cleaned_data.get('school_principal'),
                        )
                    else:
                        # Optionally update school details (associate with user)
                        existing_school.user = user
                        existing_school.school_name = self.cleaned_data.get('school_name', existing_school.school_name)
                        existing_school.school_type = self.cleaned_data.get('school_type', existing_school.school_type)
                        existing_school.school_category = self.cleaned_data.get('school_category', existing_school.school_category)
                        existing_school.school_ownership = self.cleaned_data.get('school_ownership', existing_school.school_ownership)
                        existing_school.school_admins = self.cleaned_data.get('school_admins', existing_school.school_admins)
                        existing_school.school_county = self.cleaned_data.get('school_county', existing_school.school_county)
                        existing_school.school_subcounty = self.cleaned_data.get('school_subcounty', existing_school.school_subcounty)
                        existing_school.school_ward = self.cleaned_data.get('school_ward', existing_school.school_ward)
                        existing_school.school_location = self.cleaned_data.get('school_location', existing_school.school_location)
                        existing_school.school_phone = self.cleaned_data.get('school_phone', existing_school.school_phone)
                        existing_school.school_principal = self.cleaned_data.get('school_principal', existing_school.school_principal)
                        existing_school.save()

                return user

        except IntegrityError as e:
            logger.exception("Database integrity error during signup: %s", e)
            raise
        except Exception as e:
            logger.exception("Error creating profile for user %s: %s", self.cleaned_data.get('email'), e)
            raise
