from django import forms


class JoinGroupForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
