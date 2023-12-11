from django import forms

from . import models
class Musician_form(forms.ModelForm):
    class Meta:
        model = models.Add_musician
        flelds = '__all__'