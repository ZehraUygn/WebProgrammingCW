from django import forms


class SignupForm(forms.Form):
    """
    Signup user - form
    The user is asked to input a username, an email and a password
    The username should be unique between users
    """

    # username input for the user
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
            }
        )
    )

    # email input for the user
    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(
            attrs={
                'autocomplete': 'email'
            }
        )
    )

    # user is asked to type a password
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'password'})
    )


class LoginForm(forms.Form):
    """
    Form for user login
    User is asked to input its username and a password
    """

    # user's username
    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username'})
    )

    # username's password
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'password'})
    )