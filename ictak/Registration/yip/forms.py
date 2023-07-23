from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Data
DISTRICT_CHOICES = [
    (1, 'Thiruvananthapuram'),
    (2, 'Kollam'),
    (3, 'Pathanamthitta'),
    (4, 'Alappuzha'),
    (5, 'Kottayam'),
    (6, 'Idukki'),
    (7, 'Ernakulam'),
    (8, 'Thrissur'),
    (9, 'Palakkad'),
    (10, 'Malappuram'),
    (11, 'Kozhikode'),
    (12, 'Wayanad'),
    (13, 'Kannur'),
    (14, 'Kasaragod'),
    # Add more choices as needed
]

class registration(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    mobile = forms.CharField(label='Mobile', max_length=15)
    district = forms.ChoiceField(label='District', choices=DISTRICT_CHOICES)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
class OtpForm(forms.Form):
    otp = forms.CharField(label='Name', max_length=100)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {
            'ideator_dob': forms.DateInput(attrs={'type': 'date'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'
    