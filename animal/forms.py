from django import forms
from animal.models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            'owner',
            "type",
            "genus",
            "age",
        ]
