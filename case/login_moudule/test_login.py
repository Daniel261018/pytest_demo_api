# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-22 0:19
from case.common_api.common_function import Loginclass
import requests


class TestLogin():

    def test_login_success(self):
        '''输入正确账号，正确密码'''
        s = requests.session()
        info = Loginclass(s)
        infos = info.login()
        assert infos.json()["token"]

    def test_login_fail(self):
        '''输入正确账号，错误密码'''
        s = requests.session()
        info = Loginclass(s)
        infos = info.login(psw="1245")
        assert not infos.json()["token"]
