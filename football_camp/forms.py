from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'telephone', 'address', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.telephone = self.cleaned_data['telephone']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user