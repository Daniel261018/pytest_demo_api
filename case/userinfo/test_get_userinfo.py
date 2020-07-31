# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-31 17:07

import pytest
import os
from setting import uesrinfo_data
from case.common_api.common_function import Loginclass


class TestGetUserinfo():

    def test_get_userinfo(self, login_fixture):
        s = login_fixture
        info = Loginclass(s)
        r = info.get_userinfo()
        assert r.json()["msg"] == "sucess!"
        assert r.json()["code"] == 0

