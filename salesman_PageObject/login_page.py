# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: Login_page.py
# @create_time: 2020/8/7 11:32
# @project: 同商通汇APP
# @此模块提供：登录页面封装
"""
from salesman_Middleware.Middleware_Handler import HandlerData
from salesman_Elements.login_element import LoginElement

handler = HandlerData()
login_element = LoginElement()


class LoginPage:
    def __init__(self, driver):
        handler.logger.info("---登录方法已连接---")
        self.driver = driver

    def login(self, login_username, login_password):
        self.user_name_input(login_username)\
            .user_password_input(login_password)\
            .click_login_button()\
            .is_login_success()
        handler.logger.info("--登录成功--")

    def user_name_input(self, user_name):
        """输入用户名"""
        handler.logger.info('输入用户名')
        self.driver.find_element(*login_element.LOGIN_NAME).send_keys(user_name)
        return self

    def user_password_input(self, user_password):
        """输入用户密码"""
        handler.logger.info('输入用户密码')
        self.driver.find_element(*login_element.LOGIN_PASSWORD).send_keys(user_password)
        return self

    def click_login_button(self):
        """点击登录按钮"""
        handler.logger.info('点击登录按钮')
        self.driver.find_element(*login_element.LOGIN_BUTTON).click()
        return self

    def is_login_success(self):
        """获取登录成功弹窗信息"""
        handler.logger.info('判断是否登录成功...')
        if not self.driver.find_element(*login_element.COMPANY_NAME).text:
            raise Exception('登陆失败...')
