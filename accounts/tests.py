from django.http import response
from django.test import TestCase
from accounts.models import User
from django.urls import reverse


class BaseTest(TestCase):

    def setUp(self) -> None:
        self.home_url = reverse('home')
        self.profile_url = reverse('profile')
        self.register_url = reverse('account_signup')
        self.login_url = reverse('account_login')
        self.logout_url = reverse('account_logout')
        self.user = {
            'email': 'testuser@gmail.com',
            'username': 'myusername',
            'password1': 'mypassword',
            'password2': 'mypassword',
        }
        return super().setUp()


class TestRegister(BaseTest):

    def test_user_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
    
    def test_can_register(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
    
    def test_can_login(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_can_logout(self):
        self.client.post(self.register_url, self.user, format='text/html')
        self.client.post(self.login_url, self.user, format='text/html')
        response = self.client.post(self.logout_url, self.user)
        self.assertEqual(response.status_code, 302) #TODO: Rewrite test 

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302)