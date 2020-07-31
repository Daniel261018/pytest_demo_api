# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-23 0:36

from case.common_api.common_function import Loginclass
import pytest
import os
from common.read_yaml import get_yaml_data
from setting import yaml_path

data = get_yaml_data(yaml_path)


class TestModefyInfo():

    @pytest.mark.info
    @pytest.mark.parametrize("test_input, expected", data["test_param_updata"])
    def test_modefy_info_2(self, login_fixture, test_input, expected):
        '''登录-修改'''
        s = login_fixture
        info = Loginclass(s)
        r = info.modefy_info(sex=test_input["sex"], age=test_input["age"], mail=test_input["mail"])
        # print(r.text)
        assert r.json()['code'] == expected["code"]
        assert r.json()['message'] == expected["message"]
