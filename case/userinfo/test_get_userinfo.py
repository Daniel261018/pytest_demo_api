# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-31 17:07

import pytest
import os
import allure
from setting import uesrinfo_data
from case.common_api.common_function import Loginclass

@allure.feature("个人信息模块")
class TestGetUserinfo():

    @allure.story("获取个人信息成功")
    @allure.title("获取个人信息：所有参数正确")
    def test_get_userinfo(self, login_fixture):
        s = login_fixture
        info = Loginclass(s)
        r = info.get_userinfo()
        assert r.json()["msg"] == "sucess!"
        assert r.json()["code"] == 0

