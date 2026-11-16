from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User
Type_choices=(("Admin","Admin"),("Manager","Manager"),("Staff","Staff"))
class SignUpForm(UserCreationForm):
    email=forms.CharField(max_length=100,help_text='Please include an "@" in the email address. Something is missing an "@"')
    userType=forms.ChoiceField(choices=Type_choices)
    userImage=forms.FileField()
    class Meta:
        model=User
        fields=UserCreationForm.Meta.fields+('email','status','userType','userImage')
