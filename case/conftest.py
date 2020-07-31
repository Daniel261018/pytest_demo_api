# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 14:19

import requests
import pytest
from case.common_api.common_function import Loginclass


@pytest.fixture(scope="session")
def login_fixture():
    s = requests.session()
    info = Loginclass(s)
    info.login()
    # print("用例的前置操作")
    yield s
    # print("用例执行之后只执行一次")
    s.close()  # 关闭会话


@pytest.fixture(scope="function")
def unlogin_fixture():
    s = requests.session()
    yield s
    # print("用例执行之后只执行一次")
