# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 14:56


# 项目根目录

import os
from common.read_yaml import get_yaml_data

base_dir = os.path.dirname(os.path.realpath(__file__))

print(base_dir)  # F:\PythonProject\pytest_demo_api
yaml_path = os.path.join(base_dir, "test_data", "test_data.yml")
# print(yaml_path)
# data = get_yaml_data(yaml_path)
# print(yaml_path)