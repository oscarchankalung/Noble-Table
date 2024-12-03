from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin

from .models import Account

class AccountCreationForm(forms.ModelForm):
    """
    A form for creating new account,
    includes all the required fields,
    plus a repeated passwords.
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ["email"]
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_date.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data["password1"])

        if commit:
            account.save()
        return account

class AccountChangeForm(forms.ModelForm):
    """
    A admin form for updating accounts.
    Includes all the fields on the account,
    but replaces the password field with password hash display field
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ["email", "password", "is_active", "is_admin", "is_personal", "is_organization"]

class AccountAdmin(UserAdmin):
    # The forms to add and change account instances
    form = AccountChangeForm
    add_form = AccountCreationForm

    # The fields to be used in displaying the Account model.
    # These override the definiations on the UserAdmin
    # that reference specific fields on auth.User
    list_display = ["email", "is_admin", "is_personal", "is_organization"]
    list_filter = ["is_admin", "is_personal", "is_organization"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_admin", "is_personal", "is_organization"]}),
    ]

    # add_fieldsets is not a standard ModelAdmin attribute.
    # AccountAdmin overrides get_fieldsets to use this attribute when creating an account.
    add_fieldsets = [(None, {"classes": ["wide"], "fields": ["email", "password1", "password2"]})]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []