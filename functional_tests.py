import requests
import unittest

class LoginAPITest(unittest.TestCase):
    # first API
    # Test login
    def setUp(self):
        self.base_url = 'http://localhost:8000'
        self.login_url = self.base_url + '/login'  # 要测试Django的登录API
        self.username = 'admin'
        self.password = 'admin'

    def test_login(self):
        data = {
            'account': self.username,
            'password': self.password
        }

        response = requests.post(self.login_url, data)

        self.assertEqual(response.status_code, 200)

        self.assertTrue('log_in_resp' in response.json())  # 驗證返回是否包含log_in_resp: pass
        log_in_resp = response.json()['log_in_resp']
        self.assertEqual("pass",log_in_resp)

        self.assertTrue('token' in response.json())  # 驗證返回是否包含token
        token = response.json()['token']
        self.assertIsNotNone(token)  # 驗證Token是否為None

        # headers = {'Authorization': f'Token {token}'}


    def test_failed_login(self):
        wrong_username = 'wrongusername'
        wrong_password = 'wrongpassword'

        # 測試帳號不存在
        data = {
            'account': wrong_username,
            'password': wrong_password
        }

        response = requests.post(self.login_url, data)
        self.assertEqual(response.status_code, 401)

        self.assertTrue('log_in_resp' in response.json())  # 驗證返回是否包含log_in_resp: account fail
        log_in_resp = response.json()['log_in_resp']
        self.assertEqual("account fail",log_in_resp)

        # 測試密碼錯誤
        data = {
            'account': self.username,
            'password': wrong_password
        }

        response = requests.post(self.login_url, data)
        self.assertEqual(response.status_code, 401)

        self.assertTrue('log_in_resp' in response.json())  # 驗證返回是否包含log_in_resp: password fail
        log_in_resp = response.json()['log_in_resp']
        self.assertEqual("password fail",log_in_resp)

if __name__ == '__main__':
    unittest.main(warnings='ignore')