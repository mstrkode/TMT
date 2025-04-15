from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileTests(TestCase):
    def test_create_user(self):
        """Test creating a new user"""
        email = "test@example.com"
        first_name = "Test"
        last_name = "User"
        password = "testpass123"

        user = User.objects.create_user(
            email=email, first_name=first_name, last_name=last_name, password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_admin)
        self.assertEqual(user.get_full_name(), f"{first_name} {last_name}")
        self.assertEqual(user.get_username(), email)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        email = "admin@example.com"
        first_name = "Admin"
        last_name = "User"
        password = "adminpass123"

        user = User.objects.create_superuser(
            email=email, first_name=first_name, last_name=last_name, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_admin)
