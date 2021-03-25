from django.test import TestCase

from user_system.models import User


class UserModelTests(TestCase):

    def setUpTestData(cls):
        User.objects.create_user(username="testuser", password="12345", nickname="가나다라마")
