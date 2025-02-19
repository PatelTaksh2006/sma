from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
# from django.contrib.auth import commit
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    CHOICE_ROLE=[
        ('investor','investor'),
        ('guider','guider')
    ]

    role=forms.ChoiceField(label="Login as",choices=CHOICE_ROLE,widget=forms.Select,error_messages={'required': ''})
    
    

    password = forms.CharField(widget=forms.PasswordInput(),label="Password")
    # # RememberMe=forms.BooleanField(label="Remeber me",error_messages={'required': '\n'})


class SignUpForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    
    ROLE_CHOICES = [
        ('investor', 'Investor'),
        ('guider', 'Guider'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Register as")

    class Meta:
        model = CustomUser
        fields = ("role", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        # user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']

        # Modify username only in backend for Guiders
        if commit:
            user.save()
        return user
    

class searchForm(forms.Form):
    name=forms.CharField(label="search stock",widget=forms.TextInput(attrs={'placeholder':'Search for stocks...'}))


class InvestmentForm(forms.Form):
    investment = forms.IntegerField(
        label="Monthly Investment Amount (₹)",
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 5000'})
    )
    
    duration = forms.IntegerField(
        label="Investment Duration (Years)",
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 5'})
    )
    
    expected_return = forms.FloatField(
        label="Expected Rate of Return (% per annum)",
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 12'})
    )
