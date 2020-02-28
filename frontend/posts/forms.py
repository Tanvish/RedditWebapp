from django import forms


class NameForm(forms.Form):
    sub = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control align-self-center w-100',
        'id': 'input-form'
    }))
