from django import forms
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'formField'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'formField'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'formField'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'formField'}))
    class Meta():
        model=User
        fields=('username', 'email', 'password')

    def clean(self):
        all_clean_data=super().clean()
        password=all_clean_data['password']
        confirm_password=all_clean_data['confirm_password']

        if password!=confirm_password:
            raise forms.ValidationError("Password Not Matching: Re-enter same password!")
