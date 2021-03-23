from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_can_create_a_user(self):
        username = 'testid'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
