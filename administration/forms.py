from django import forms


class AdminForm(forms.Form):
    user_name = forms.CharField(label="User Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
