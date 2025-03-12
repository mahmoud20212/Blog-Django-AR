from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label=_('username'), max_length=30, help_text=_('username should not contain spaces.'))
    email = forms.EmailField(label=_('email'))
    first_name = forms.CharField(label=_('first name'))
    last_name = forms.CharField(label=_('last name'))
    password1 = forms.CharField(label=_('password'), widget=forms.PasswordInput(), min_length=8, help_text=_('password should not be less than 8 items.'))
    password2 = forms.CharField(label=_('confirm password'), widget=forms.PasswordInput(), min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                'last_name', 'password1', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_('password not matching.'))
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError(_('this username already exists.'))
        return cd['username']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label=_('username'))
    password = forms.CharField(label=_('password'), widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label=_('first name'))
    last_name = forms.CharField(label=_('last name'))
    email = forms.EmailField(label=_('email'))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']