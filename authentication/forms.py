from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignupForm(UserCreationForm):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.fields["username"].widget.attrs.update({
    #               "class":"floating-input form-control",
    #               "type":"text",
    #               "placeholder":""
    #         })
    #         self.fields["email"].widget.attrs.update({
    #               "class":"floating-input form-control",
    #               "type":"email",
    #               "placeholder":""
    #         })
    #         self.fields["password1"].widget.attrs.update({
    #               "class":"floating-input form-control",
    #               "type":"password",
    #               "placeholder":""
    #         })
    #         self.fields["password2"].widget.attrs.update({
    #               "class":"floating-input form-control",
    #               "type":"password",
    #               "placeholder":""
    #         })

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "full_name",
            "phone_no",
            "password1",
            "password2",
        ]
