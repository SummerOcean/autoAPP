# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: create_customer_page.py
# @create_time: 2020/11/17 15:20
# @此模块提供：创建店铺页面
"""
import time
from appium.webdriver.common.touch_action import TouchAction
from salesman_PageObject.base_page import BasePage
from salesman_Elements.create_customer_element import CreateCustomerElement
from salesman_Middleware.Middleware_Handler import HandlerData

handler = HandlerData()
createcustomer = CreateCustomerElement()


class CreateCustomerPage(BasePage):
    """页面：创建店铺"""
    def __init__(self, driver):
        self.driver = driver
        handler.logger.info('正在初始化页面:创建店铺...')

    def switch_specify_page(self):
        """跳转到指定页面:主页"""
        self.driver.start_activity(createcustomer.PACKAGE_NAME, createcustomer.ACTIVITY_NAME)
        handler.logger.info('跳转到指定页面:主页')
        return self

    def click_new_customer_button(self):
        """新增客户按钮"""
        self.driver.find_element(*createcustomer.NEW_CUSTOMER).click()
        handler.logger.info('点击店铺新增客户按钮')
        return self

    def input_customer_number(self, shop_number):
        """输入店铺账号"""
        self.driver.find_element(*createcustomer.USER_NAME).send_keys(shop_number)
        handler.logger.info('输入店铺账号')
        return self

    def input_user_pwd(self, password):
        """输入账号密码、输入确认账号密码"""
        self.driver.find_element(*createcustomer.USER_PASSWORD).send_keys(password)
        handler.logger.info('输入账号密码')
        self.driver.find_element(*createcustomer.SURE_PASSWORD).send_keys(password)
        handler.logger.info('输入确认账号密码')
        return self

    def input_customer_name(self, shop_name):
        """输入店铺名称"""
        self.driver.find_element(*createcustomer.SHOP_NAME).send_keys(shop_name)
        handler.logger.info('输入店铺名称')
        return self

    def input_boss_name(self, boss_name):
        """输入老板名称"""
        self.driver.find_element(*createcustomer.SHOP_BOSS).send_keys(boss_name)
        handler.logger.info('输入老板名称')
        return self

    def select_shop_type(self):
        """选择店铺类型"""
        self.driver.find_element(*createcustomer.TYPE_LIST).click()
        handler.logger.info('选择店铺类型')
        time.sleep(0.3)
        self.random_tap_coordinate(450, 450, 750, 1450, Y=True)
        _TYPE_TEXT = self.driver.find_element(*createcustomer.TYPE_LIST).text
        handler.logger.info('当前选择的店铺类型为:{}'.format(_TYPE_TEXT))
        return self

    def input_shop_customize_address(self, customize_address):
        """输入店铺自定义地址(选填)"""
        self.driver.find_element(*createcustomer.SHOP_DEFINED_ADDRESS).send_keys(customize_address)
        handler.logger.info('输入店铺自定义地址')
        return self

    def upload_shop_picture(self):
        """上传店铺照片"""
        handler.logger.info('滑动屏幕至上传店铺照片位置')
        touch = TouchAction(self.driver)
        touch.press(x=450, y=1380) \
            .wait(ms=0) \
            .move_to(x=450, y=200) \
            .release().perform()
        handler.logger.info('点击上传按钮')
        self.driver.tap([(240, 1115), (240, 1115)], 100)
        handler.logger.info('选择一张照片')
        self.driver.tap([(640, 164), (640, 164)], 100)
        handler.logger.info('点击确定')
        self.driver.tap([(760, 90), (760, 90)], 100)
        handler.logger.info('店铺照片上传完成')
        return self

    def click_submit_audit(self):
        """点击提交审核按钮"""
        self.driver.find_element(*createcustomer.SUBMIT_AUDIT).click()
        handler.logger.info('点击提交审核按钮')
        return self

    def assert_create_success(self):
        """判断店铺创建成功"""
        self.assert_toast_message("创建成功")

