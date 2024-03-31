from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class TestUserPassword(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser')

    def test_short_password(self):
        with self.assertRaises(ValidationError):
            validate_password('short', self.user)
            self.user.full_clean()
        pass

    def test_password_similarity(self):
        with self.assertRaises(ValidationError):
            validate_password('testuser123', self.user)
            self.user.full_clean()
        pass

    def test_numeric_password(self):
        with self.assertRaises(ValidationError):
            validate_password('123456789', self.user)
            self.user.full_clean()
        pass

    def test_commonly_used_password(self):
        with self.assertRaises(ValidationError):
            validate_password('password', self.user)
            self.user.full_clean()
        pass