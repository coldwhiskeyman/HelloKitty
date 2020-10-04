from django import forms

from . import models


class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ['name', 'age', 'weight', 'height', 'details']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя животного'}),
            'age': forms.widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Возраст'}),
            'weight': forms.widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вес'}),
            'height': forms.widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рост'}),
            'details': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Особые приметы'}),
        }
