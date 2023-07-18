from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token


class LoginAPITest(TestCase):
    def setUp(self):
        self.url = reverse('login')
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        data = {
            'account': self.username,
            'password': self.password
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['sign_in_resp'], 'pass')
        self.assertTrue('token' in response.json())

    def test_login_failure(self):
        data = {
            'account': 'wrongaccount',
            'password': 'wrongpassword'
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse('token' in response.json())

    def test_inactive_user(self):
        self.user.is_active = False
        self.user.save()

        data = {
            'account': self.username,
            'password': self.password
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse('token' in response.json())
