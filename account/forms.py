from random import choices
from django import forms
from django.core.exceptions import ValidationError
from .models import *
import datetime
class SearchForm(forms.ModelForm):
    class Meta:
        model=Lecturers
        fields=['department']
        widgets={
            'department': forms.Select(attrs={'class':'form-select'}),
        }