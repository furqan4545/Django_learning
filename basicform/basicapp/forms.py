from django import forms
from django.core import validators

# making ur own custom validators 
# def check_for_z(value):  # it will check that either ur specific field starts with z or not. 
#     if value[0].lower() != "z":
#         raise forms.ValidationError("Name Needs to start with Z")


# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
#                                     validators=[validators.MaxLengthValidator(0)]) # validators paramter is used for cathcing bots or validating the form
#                                     # yani ap MaxLenthValdidator(0) ka mtlb hai k ap ki hidden field ki length 0 sy bari nhi honi chahye vrna yeh bot hai. 

    
# claening the entire form all at once. 
class FormName(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again: ")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        
        all_clean_data = super().clean()  # it's going to return all ur clean data for the entire form. 
        email = all_clean_data["email"]
        vmail = all_clean_data["verify_email"]

        if email != vmail:
            raise forms.ValidationError("Make sure Email matchs!")
        


