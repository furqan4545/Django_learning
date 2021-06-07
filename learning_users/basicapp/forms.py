from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput()) # input will be password type.

    class Meta():
        model = User # here we r using builtin User model
        fields = ('username', 'email', 'password') # these r the fields tat we want to use for our form from the bulitin User class. 

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
