from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email(self):
        """create user with email address"""
        email = "test1311@gmail.com"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_case_sence(self):
        """case sence for email address"""
        email = "test1311@gmail.com"
        user = get_user_model().objects.create_user(
            email=email
        )
        self.assertEqual(user.email, email.lower())
    
    def test_invalid_email_address(self):
        """raises from invalid email addresss"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test1234")

    def test_create_super_user(self):
        """create super user with email address"""
        user = get_user_model().objects.create_superuser(
            "test1311@gmail.com",
            "test1234"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)