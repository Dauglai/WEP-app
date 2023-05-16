from django import forms

class ChoiceForm(forms.Form):
    CHOICES = (
        ("1", "one"),
        ("2", "two"),
        ("3", "free"),
        ("4", "four"))
    response = forms.ChoiceField(widget=forms.RadioSelect,
                                 label="question.question", choices=CHOICES)

class JoinGroupForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)