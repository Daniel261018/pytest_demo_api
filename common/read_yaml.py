# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-23 0:03

import os
import yaml


def get_yaml_data(yaml_path):
    """获取yaml文件数据"""
    f = open(yaml_path, "r", encoding="utf-8")
    yamldata = f.read()
    # print(yamlpath)

    # 把yaml文件数据转字典
    d = yaml.load(yamldata)
    f.close()
    # print(d['test_info_params'])
    return d


if __name__ == '__main__':
    cur_path = os.path.dirname(os.path.realpath(__file__))
    print(cur_path)  # F:\PythonProject\pytest_demo_api\common
    print(os.path.dirname(cur_path))  # F:\PythonProject\pytest_demo_api
    yaml_path = os.path.join(os.path.dirname(cur_path), "test_data",
                             "uesrinfo_data.yml")  # F:\PythonProject\pytest_demo_api\test_data\uesrinfo_data.yml
    print(yaml_path)
    a = get_yaml_data(yaml_path)
    print(a)
