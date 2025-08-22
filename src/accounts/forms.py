from allauth.account.forms import SignupForm
from django import forms
from accounts.models import CustomUser

#custom signup form to assign the user_type, and then create the matching profile based on the type — 
# even if the models live in different apps
class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)
    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user