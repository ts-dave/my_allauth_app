from django.test import TestCase
from accounts.models import User
from django.test import Client
from django.urls import reverse


class BaseTest(TestCase):

    def setUp(self) -> None:
        self.register_url = reverse()
        self.login_url = reverse()
        self.user = {
            'email': 'testuser@gmail.com',
            'username': 'myusername',
            'password1': 'mypassword',
            'password2': 'mypassword',
        }
        return super().setUp()