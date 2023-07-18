from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import unittest

class LoginAPITest(unittest.TestCase):
    # first API
    # Test login
    def setUp(self):
        self.base_url = 'http://localhost:8000' 
        self.login_url = self.base_url + '/login'  # 要測試Django的後台
        self.username = 'testuser'
        self.password = 'testpassword'

    def test_login(self):
        data = {
            'username': self.username,
            'password': self.password
        }

        response = requests.post(self.login_url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('sessionid' in response.cookies)


    def test_failed_login(self):
        wrong_username = 'wrongusername'
        wrong_password = 'wrongpassword'

        data = {
            'username': wrong_username,
            'password': wrong_password
        }

        response = requests.post(self.login_url, json=data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse('sessionid' in response.cookies)

if __name__ == '__main__':
    unittest.main(warnings='ignore')