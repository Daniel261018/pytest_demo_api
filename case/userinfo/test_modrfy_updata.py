# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-23 0:36

import pytest
import os
import allure
from setting import uesrinfo_data
from case.common_api.common_function import Loginclass


@allure.feature("个人信息模块")
class TestModefyUserinfo():

    @allure.story("修改个人信息成功")
    @allure.title("修改个人信息成功-sex")
    # @pytest.mark.info
    @pytest.mark.parametrize("test_input, expected", uesrinfo_data["test_param_sex"])
    def test_modefy_userinfo_sex(self, login_fixture, test_input, expected):
        '''登录-修改'''
        s = login_fixture
        info = Loginclass(s)
        r = info.modefy_userinfo(sex=test_input)
        # print(r.text)
        assert r.json()['code'] == expected["code"]
        assert r.json()['message'] == expected["message"]

    @allure.story("修改个人信息成功")
    @allure.title("修改个人信息成功-all")
    # @pytest.mark.info
    @pytest.mark.parametrize("test_input, expected", uesrinfo_data["test_param_updata"])
    def test_modefy_userinfo_all(self, login_fixture, test_input, expected):
        '''登录-修改'''
        s = login_fixture
        info = Loginclass(s)
        r = info.modefy_userinfo(sex=test_input["sex"], age=test_input["age"], mail=test_input["mail"])
        # print(r.text)
        assert r.json()['code'] == expected["code"]
        assert r.json()['message'] == expected["message"]
