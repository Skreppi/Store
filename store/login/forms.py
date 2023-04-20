import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.utils.timezone import now

from login.models import EmailVerification, User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите имя',
                'id': 'inputFirstName',
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите фамилию',
                'id': 'inputLastName',
            }
        )
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите имя пользователя',
                'id': 'inputUsername',
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите адрес эл. почты',
                'id': 'inputEmailAddress',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите пароль',
                'id': 'inputPassword',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Подтвердите пароль',
                'id': 'inputConfirmPassword',
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=24)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя',
                'id': 'inputEmailAddress',
            }
        )
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите пароль',
                'id': 'inputPassword',
            }
        )
    )


class ChangeForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'id': 'inputFirstName',
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'id': 'inputLastName',
            }
        )
    )
    image = forms.ImageField(
        max_length=100,
        widget=forms.FileInput(
            attrs={
                'class': 'custom-file-input',
                'id': 'userAvatar',
            }
        )
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'id': 'inputUsername',
                'readonly': True,
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control py-4',
                'id': 'inputEmailAddress',
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
