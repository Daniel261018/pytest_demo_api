# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 12:45

import pytest
import requests
import allure
from case.common_api.common_function import Loginclass

@allure.step("注册模块")
class TestRegister():

    @allure.title("注册成功")
    def test_register_success(self, unlogin_fixture, delete_user):
        '''注册成功'''
        info = Loginclass(unlogin_fixture)
        r = info.register()
        assert r.json()["msg"] == "注册成功!"
        assert r.json()["code"] == 0

    @allure.title("注册账号已经被注册过")
    def test_register_fail(self, unlogin_fixture, delete_user):
        '''已经被注册'''
        info = Loginclass(unlogin_fixture)
        r = info.register()
        assert r.json()["msg"] == "注册成功!"
        assert r.json()["code"] == 0

        # 第二次注册，已经被注册
        r2 = info.register()
        assert r2.json()["msg"] == "test1992用户已被注册"
        assert r2.json()["code"] == 2000
