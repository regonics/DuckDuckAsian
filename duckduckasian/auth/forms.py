from django import forms

from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import PasswordInput

BIRTH_YEAR_CHOICES = range(1913,2013)

RACE_CHOICES = (('Chinese', 'Chinese'),
                ('Filipino', 'Filipino'),
                ('Japan', 'Japan'),
                ('Korean', 'Korean'),
                ('Taiwanese', 'Taiwanese'),
                ('Thai', 'Thai'),
                ('Vietnamese', 'Vietnamese'),
                ('Other', 'Other'))

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=PasswordInput, max_length=255)
    confirm_password = forms.CharField(widget=PasswordInput, max_length=255)
    email = forms.CharField(max_length=255)
    race = forms.ChoiceField(choices=RACE_CHOICES)
    date_of_birth = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
