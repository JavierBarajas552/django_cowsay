from django import forms


class CowForm(forms.Form):
    text = forms.CharField(max_length=100)
