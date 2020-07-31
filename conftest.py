# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 14:10

import os
import pytest


# 控制整个项目的  钩子函数

# 添加pytest命令行参数
def pytest_addoption(parser):
    parser.addoption("--host",
                     action="store",
                     default="http://49.235.92.12:6009",
                     help="host option:host1 or host2")


# autouse=True 自动使用
@pytest.fixture(scope="session", autouse=True)
def host_fixture(request):
    # # 获取命令行参数给到环境变量
    os.environ["host"] = request.config.getoption("--host")
    # os.environ["host"] = "http://49.235.92.12:6009"
