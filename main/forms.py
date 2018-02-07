
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class contactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField(required=True)
    comment = forms.CharField(widget = forms.Textarea())
