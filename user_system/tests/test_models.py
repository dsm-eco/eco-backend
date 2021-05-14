from django.test import TestCase

from user_system.models import User


class UserModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="testuser", password="12345", nickname="testnickname")

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 45)

    def test_nickname_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('nickname').verbose_name
        self.assertEquals(field_label, 'nickname')

    def test_nickname_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('nickname').max_length
        self.assertEquals(max_length, 45)

    def test_object_name_is_username(self):
        user = User.objects.get(id=1)
        expected_object_name = user.username
        self.assertEquals(expected_object_name, str(user))
