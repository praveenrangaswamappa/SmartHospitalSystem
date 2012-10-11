from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Your Username",max_length = 20)
    password = forms.CharField(widget=forms.PasswordInput,max_length =10)