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

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        if user_type == CustomUser.SCHOOL:
            required_fields = [
                'school_code', 'school_name', 'school_type', 'school_category',
                'school_ownership', 'school_admins', 'school_county', 'school_subcounty',
                'school_ward', 'school_location', 'school_phone', 'school_principal'
            ]
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, "This field is required for school user registration.")

        return cleaned_data



    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        
        if user.user_type == CustomUser.SCHOOL:
            # Create the associated School record
            School.objects.create(
                user=user,
                school_code=self.cleaned_data['school_code'],
                school_name=self.cleaned_data['school_name'],
                school_type=self.cleaned_data['school_type'],
                school_category=self.cleaned_data['school_category'],
                school_ownership=self.cleaned_data['school_ownership'],
                school_admins=self.cleaned_data['school_admins'],
                school_county=self.cleaned_data['school_county'],
                school_subcounty=self.cleaned_data['school_subcounty'],
                school_ward=self.cleaned_data.get('school_ward', ''),
                school_location=self.cleaned_data['school_location'],
                school_phone=self.cleaned_data['school_phone'],
                school_principal=self.cleaned_data['school_principal'],
                # school_status defaults to "Pending"
            )

        return user