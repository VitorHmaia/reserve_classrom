from django import forms
from .models import ClassEntity

class ClassForm(forms.Form):
    nome = forms.CharField(max_length=100)
    responsavel = forms.CharField(max_length=100)
    
