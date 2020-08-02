# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-22 0:19


import requests
import allure
import pytest
from case.common_api.common_function import Loginclass
from setting import login_data


@allure.feature("登录模块")
class TestLogin():

    @allure.story("登录成功")
    @allure.title("输入正确账号，正确密码")
    def test_login_success(self):
        s = requests.session()
        info = Loginclass(s)
        infos = info.login()
        assert infos.json()["msg"] == 'login success!'
        assert infos.json()["code"] == 0

    @allure.story("登录失败")
    @allure.title("输入错误账号，正确密码")
    @pytest.mark.parametrize("test_input, expected", login_data["test_login_fail"])
    def test_login_user_fail(self, test_input, expected):
        s = requests.session()
        info = Loginclass(s)
        infos = info.login(user=test_input)
        assert infos.json()["msg"] == expected["msg"]
        assert infos.json()["code"] == expected["code"]

    @allure.story("登录失败")
    @allure.title("输入正确账号，错误密码")
    @pytest.mark.parametrize("test_input, expected", login_data["test_login_fail"])
    def test_login_psw_fail(self, test_input, expected):
        s = requests.session()
        info = Loginclass(s)
        infos = info.login(psw=test_input)
        assert infos.json()["msg"] == expected["msg"]
        assert infos.json()["code"] == expected["code"]
