from typing import Dict, Any

from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm[User]):
    """Simple user registration form with password confirmation."""

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirm password"
    )

    class Meta:
        model = User
        fields = ("username", "email")

    def clean(self) -> Dict[str, Any]:
        data = super().clean()
        if data is None:
            raise forms.ValidationError("No data to clean.")
        if data.get("password") != data.get("password_confirm"):
            raise forms.ValidationError("Passwords do not match.")
        return data

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
