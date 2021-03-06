
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit, Layout, ButtonHolder, Fieldset
)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=200,
    )

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('login', 'Login'))

class UserEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.editer = kwargs.pop('editer', None)
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_email(self):
        email_submitted = self.cleaned_data['email']
        if self._meta.model.objects.filter(email=email_submitted).exclude(email=self.editer).exists():
            raise ValidationError(
                'A user with this email already exists',
                code='invalid'
            )
        return self.cleaned_data['email']

class UserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')

        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password2'))

        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label = _("Password"),
        help_text = _(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        )
    )
    
    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']
