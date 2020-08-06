# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 14:13
import os
import requests
import allure
from nb_log import LogManager
from nb_log_config import LOG_PATH

logger = LogManager(logger_name="api").get_logger_and_add_handlers(is_add_stream_handler=True,
                                                                   log_filename="api.log",
                                                                   log_path=LOG_PATH)


class Loginclass():

    def __init__(self, s):
        self.s = s

    @allure.step("登录")
    def login(self, user="test", psw="123456"):
        '''登录'''
        url = os.environ["host"] + "/api/v1/login"
        # Content-Type: application/json
        body = {
            "username": user,
            "password": psw
        }
        r = self.s.post(url, json=body)
        logger.debug("登录返回:%s" % r.text)
        # print(r.text)
        # 提取token
        token = r.json()["token"]  # 等价于json.loads(r.text) 转字典
        logger.debug("获取token:%s" % token)
        h = {
            "Authorization": "Token " + token
        }
        self.s.headers.update(h)  # s已经带了token
        # print(token)
        return r

    @allure.step("获取个人信息")
    def get_userinfo(self):
        '''获取个人信息'''
        url = os.environ["host"] + "/api/v1/userinfo"
        r = self.s.get(url)
        logger.debug("获取个人信息:%s" % r.text)
        # print(r2.json())
        # print(r2.text)
        return r

    @allure.step("修改个人信息")
    def modefy_userinfo(self, name="test", age=20, sex="M", mail="1993@qq.com"):
        '''修改个人信息'''
        url = os.environ["host"] + "/api/v1/userinfo"
        body = {
            "name": name,
            "age": age,
            "sex": sex,
            "mail": mail
        }
        r = self.s.post(url, json=body)
        logger.info("修改个人信息:%s" % r.text)
        # print(r2.json())
        # print(r2.text)
        return r

    @allure.step("注册")
    def register(self, uesrname="test1992", password="123456", mail="1992@qq.com"):
        """注册"""
        url = os.environ["host"] + "/api/v1/register"
        body = {
            "username": uesrname,
            "password": password,
            "mail": mail
        }
        r = self.s.post(url, json=body)
        logger.debug("注册接口返回:%s" % r.text)
        return r


if __name__ == '__main__':
    os.environ["host"] = "http://49.235.92.12:6009"
    s = requests.session()
    a = Loginclass(s)
    b = a.login()
    # c = a.get_userinfo()
    # d = a.modefy_userinfo()
    # f = a.register(mail="")
    print(b.json())
    # print(c.json())
    # print(d.json())
    # print(f.json())
