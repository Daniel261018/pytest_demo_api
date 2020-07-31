# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-23 0:36

import pytest
import os
from setting import uesrinfo_data
from case.common_api.common_function import Loginclass


class TestModefyUserinfo():

    # @pytest.mark.info
    @pytest.mark.parametrize("test_input, expected", uesrinfo_data["test_param_updata"])
    def test_modefy_userinfo(self, login_fixture, test_input, expected):
        '''登录-修改'''
        s = login_fixture
        info = Loginclass(s)
        r = info.modefy_userinfo(sex=test_input["sex"], age=test_input["age"], mail=test_input["mail"])
        # print(r.text)
        assert r.json()['code'] == expected["code"]
        assert r.json()['message'] == expected["message"]
