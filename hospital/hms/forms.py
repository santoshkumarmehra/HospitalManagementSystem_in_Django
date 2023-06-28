from django import forms
from .models import UserProfile


class DoctorSignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['category' , 'first_name', 'email', 'specialization','institute', 'password']
        
class PatientSignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['category' , 'first_name', 'email', 'gender', 'address', 'password']
        

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
