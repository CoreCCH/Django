from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from Accounts.models import Stuff


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
        self.assertEqual(response.json()['log_in_resp'], 'pass')
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

class StuffModelTest(TestCase):

    def test_saving_and_retrieving_stuffs(self):
        first_stuff = Stuff()
        first_stuff.name = "Eugene Krabs"
        first_stuff.account = "Eugene_Krabs"
        first_stuff.title = "Boss"
        first_stuff.unit = "Krusty Krab"
        first_stuff.email = "Eugene_Krabs@gmail.com"
        first_stuff.permission = "A"
        first_stuff.activation = True
        first_stuff.save()

        second_stuff = Stuff()
        second_stuff.name = "Sponge Bob"
        second_stuff.account = "Sponge_Bob"
        second_stuff.title = "Chef"
        second_stuff.unit = "Krusty Krab"
        second_stuff.email = "Sponge_Bob@gmail.com"
        second_stuff.permission = "R"
        second_stuff.activation = True
        second_stuff.save()

        saved_stuffs = Stuff.objects.all()
        self.assertEqual(saved_stuffs.count(),2)

        