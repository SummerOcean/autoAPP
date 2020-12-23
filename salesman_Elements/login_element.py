# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: login_element.py
# @create_time: 2020/11/13 11:09
# @project: ZYSY_同商通汇APP
# @此模块提供：登录界面的元素
"""
from selenium.webdriver.common.by import By


class LoginElement:
    LOGIN_NAME = [By.ID, "com.hjkj.hjmall:id/et_login_user_name"]
    LOGIN_PASSWORD = [By.ID, "com.hjkj.hjmall:id/et_login_user_psw"]
    LOGIN_BUTTON = [By.ID, "com.hjkj.hjmall:id/tv_login_button"]
    COMPANY_NAME = [By.ID, "tv_ws_company_name"]
