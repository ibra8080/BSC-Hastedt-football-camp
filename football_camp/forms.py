from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Player, Profile

# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.get_or_create(
                user=user,
                defaults={
                    'telephone': self.cleaned_data['telephone'],
                    'address': self.cleaned_data['address']
                }
            )
        return user

# Player form
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'age', 'gender', 'height', 'pic']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 8 or age > 15:
            raise forms.ValidationError("Age must be between 8 and 15.")
        return age