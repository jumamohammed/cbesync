from allauth.account.forms import SignupForm
from django import forms
from accounts.models import CustomUser
from schools.models import School

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES1)

    # School fields (conditionally required)
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

    # Custom form validations
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        # If the registered user is a school, validate the fields
        if user_type == CustomUser.SCHOOL:
            required_fields = [
                'school_code', 'school_name', 'school_type', 'school_category',
                'school_ownership', 'school_admins', 'school_county', 'school_subcounty',
                'school_location', 'school_phone', 'school_principal', 'school_ward'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f"{field.replace('_', ' ').capitalize()} is required for school registration.")

        return cleaned_data

    def save(self, request):
        # Save the user
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        # If the user is a school, handle the school-related data
        if user.user_type == CustomUser.SCHOOL:
            school_code = self.cleaned_data.get('school_code')
            if School.objects.filter(school_code=school_code).exists():
                self.add_error('school_code', 'This school code is already taken.')

            # Check if a school with this school_code already exists
            school = School.objects.filter(school_code=school_code).first()

            if not school:
                # If no existing school found, create a new one
                school = School.objects.create(
                    user=user,
                    school_code=school_code,
                    school_name=self.cleaned_data.get('school_name'),
                    school_type=self.cleaned_data.get('school_type'),
                    school_category=self.cleaned_data.get('school_category'),
                    school_ownership=self.cleaned_data.get('school_ownership'),
                    school_admins=self.cleaned_data.get('school_admins'),
                    school_county=self.cleaned_data.get('school_county'),
                    school_subcounty=self.cleaned_data.get('school_subcounty'),
                    school_ward=self.cleaned_data.get('school_ward', ''),
                    school_location=self.cleaned_data.get('school_location'),
                    school_phone=self.cleaned_data.get('school_phone'),
                    school_principal=self.cleaned_data.get('school_principal'),
                )
            else:
                # Update the existing school details (only the provided fields)
                school.school_name = self.cleaned_data.get('school_name', school.school_name)
                school.school_type = self.cleaned_data.get('school_type', school.school_type)
                school.school_category = self.cleaned_data.get('school_category', school.school_category)
                school.school_ownership = self.cleaned_data.get('school_ownership', school.school_ownership)
                school.school_admins = self.cleaned_data.get('school_admins', school.school_admins)
                school.school_county = self.cleaned_data.get('school_county', school.school_county)
                school.school_subcounty = self.cleaned_data.get('school_subcounty', school.school_subcounty)
                school.school_ward = self.cleaned_data.get('school_ward', school.school_ward)
                school.school_location = self.cleaned_data.get('school_location', school.school_location)
                school.school_phone = self.cleaned_data.get('school_phone', school.school_phone)
                school.school_principal = self.cleaned_data.get('school_principal', school.school_principal)
                school.save()

        return user
