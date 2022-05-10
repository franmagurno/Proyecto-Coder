from attr import fields
from django import forms
from .models import Entrada
from django.db import models

class EntradaForm(forms.ModelForm):
    
    class Meta:
        model = Entrada
        fields=['nombre', 'contenido', 'imagen', 'autor']



