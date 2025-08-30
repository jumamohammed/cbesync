from allauth.account.forms import SignupForm
from django import forms
from accounts.models import CustomUser
from schools.models import School

#custom signup form to assign the user_type, and then create the matching profile based on the type — 
# even if the models live in different apps
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

    #Custom form validations
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        # If the registered user is a school, validate the fields
        if user_type == CustomUser.SCHOOL:
            required_fields = [
                'school_code', 'school_name', 'school_type', 'school_category',
                'school_ownership', 'school_admins', 'school_county', 'school_subcounty',
                'school_location', 'school_phone', 'school_principal'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f"{field.replace('_', ' ').capitalize()} is required for school registration.")

        return cleaned_data



    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()

        # profile creation or update handled in the signal
        return user