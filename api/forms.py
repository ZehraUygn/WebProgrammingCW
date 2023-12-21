from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'autocomplete': 'username'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'autocomplete': 'email'})
    )
    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'autocomplete': 'username'})
    )
    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'})
    )
