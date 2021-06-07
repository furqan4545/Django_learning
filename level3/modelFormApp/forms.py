from django import forms
from modelFormApp.models import User

class NewUserForm(forms.ModelForm):
    # Inline class or meta class
    class Meta:
        model = User
        fields = '__all__' # mtlb sari fields ko utha lao.

