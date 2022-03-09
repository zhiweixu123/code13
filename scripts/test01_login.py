# 导包
import unittest
import requests
from api.login import LoginAPI

#创建测试类
class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginAPI()

    # 定义测试用例
    #case登录成功

    def test01_case001(self):
        response1 =self.login_api.login({"mobile": "13488888888", "password": "123456"})



