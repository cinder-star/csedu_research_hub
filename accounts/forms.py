from django.contrib.auth import authenticate, get_user_model
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from crispy_forms.bootstrap import PrependedText, FormActions

from .models import User

class UsersLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "email",
            "password",
            FormActions(Submit("submit", "Login", css_class="btn btn-block btn-lg")),
        )

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = None
            try:
                user = User.objects.get(email=email)
            except:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UsersLoginForm, self).clean(*args, **keyargs)


class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "full_name",
            "email",
            "registration_number",
            "password",
            "confirm_password",
        ]

    full_name = forms.CharField(label="Full Name")
    email = forms.EmailField(label="Email")
    registration_number = forms.CharField(label="Registration Number")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    agreement = forms.BooleanField(
        label="I agree to the <a href='#'>terms and conditions</a>"
    )

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {
                "class": "form-control",
                "name": "full_name",
                "placeholder": "Mr. Abdur Rahim",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "name": "email",
                "placeholder": "20XX-XXX-XXX@cse.du.ac.bd",
            }
        )
        self.fields["registration_number"].widget.attrs.update(
            {
                "class": "form-control",
                "name": "reg_number",
                "placeholder": "20XXXXXXXX",
            }
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "name": "password"}
        )
        self.fields["confirm_password"].widget.attrs.update(
            {"class": "form-control", "name": "confirm_password"}
        )
        self.fields["agreement"].widget.attrs.update(
            {"class": "form-control", "name": "agreement"}
        )
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "full_name",
            "email",
            "registration_number",
            Row(
                Column("password", css_class="form-group col-md-6 mb-0"),
                Column("confirm_password", css_class="form-group col-md-6 mb-0"),
            ),
            "agreement",
            FormActions(Submit("submit", "Register", css_class="btn btn-block btn-lg")),
        )

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        full_name = self.cleaned_data.get("full_name")
        registration_number = self.cleaned_data.get("registration_number")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        agreement = self.cleaned_data.get("agreement")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists!"
            )

        if password != confirm_password:
            raise forms.ValidationError("Passwords must match")

        if password and len(password) < 8:
            raise forms.ValidationError("Password must be greater than 8 characters")

        if not agreement:
            raise forms.ValidationError("You must agree to the terms and conditions!")

        return super(UsersRegisterForm, self).clean(*args, **keyargs)