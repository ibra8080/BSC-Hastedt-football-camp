from django.test import TestCase
from ..forms import CustomUserCreationForm, PlayerForm
from django.contrib.auth.models import User

class CustomUserCreationFormTests(TestCase):

    def test_custom_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'telephone': '1234567890',
            'address': '123 Test St, Test City, TC'
        })
        self.assertTrue(form.is_valid())
    
    def test_custom_user_creation_form_invalid_telephone(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'telephone': 'invalidphone',
            'address': '123 Test St, Test City, TC'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('telephone', form.errors)

class PlayerFormTests(TestCase):

    def test_player_form_empty_submission(self):
        form = PlayerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('age', form.errors)
        self.assertIn('gender', form.errors)
        self.assertIn('height', form.errors)
        self.assertIn('pic', form.errors)
    
    def test_player_form_valid_data(self):
        form = PlayerForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 10,
            'gender': 'Male',
            'height': 140,
            'pic': 'path/to/pic.jpg'
        })
        self.assertTrue(form.is_valid())
    
    def test_player_form_invalid_age(self):
        form = PlayerForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 7,  # Invalid age
            'gender': 'Male',
            'height': 140,
            'pic': 'path/to/pic.jpg'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)
        self.assertEqual(form.errors['age'], ['Age must be between 8 and 15.'])

        form = PlayerForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 16,  # Invalid age
            'gender': 'Male',
            'height': 140,
            'pic': 'path/to/pic.jpg'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)
        self.assertEqual(form.errors['age'], ['Age must be between 8 and 15.'])