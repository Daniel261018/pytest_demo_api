# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 14:56


# 项目根目录

import os
from common.read_yaml import get_yaml_data

base_dir = os.path.dirname(os.path.realpath(__file__))
# print(base_dir)  # F:\PythonProject\pytest_demo_api

yaml_path1 = os.path.join(base_dir, "test_data", "login_data.yml")
login_data = get_yaml_data(yaml_path1)

yaml_path2 = os.path.join(base_dir, "test_data", "register_data.yml")
register_data = get_yaml_data(yaml_path2)

yaml_path3 = os.path.join(base_dir, "test_data", "uesrinfo_data.yml")
uesrinfo_data = get_yaml_data(yaml_path3)
