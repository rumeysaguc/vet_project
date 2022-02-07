from django import forms
from django.contrib.auth.models import Group, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
        ]
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for arr in self.fields:
            self.fields[arr].widget.attrs.update({'class': 'form-control ', })