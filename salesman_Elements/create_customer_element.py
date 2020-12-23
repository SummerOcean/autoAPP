# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: create_customer.py
# @create_time: 2020/11/13 11:12
# @project: ZYSY_同商通汇APP
# @此模块提供：
"""
from appium.webdriver.common.mobileby import MobileBy


class CreateCustomerElement:
    """
    新增客户页面元素
    """
    # 包名
    PACKAGE_NAME = 'com.hjkj.hjmall'
    # 活动名
    ACTIVITY_NAME = '.MainActivity'
    # 新增客户
    NEW_CUSTOMER = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("新增客户").instance(0)']
    # 用户账号
    USER_NAME = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customeR_account"]
    # 账号密码
    USER_PASSWORD = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customeR_password"]
    # 确认账号密码
    SURE_PASSWORD = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customer_password_confirm"]
    # 店铺名称
    SHOP_NAME = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customer_name"]
    # 老板名称
    SHOP_BOSS = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customer_boss"]
    # 类型选择框
    TYPE_LIST = [MobileBy.ID, "com.hjkj.hjmall:id/tv_new_customer_password_type"]
    # 电话号码
    PHONE_NUMBER = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customer_phone"]
    # 店铺自定义地址
    SHOP_DEFINED_ADDRESS = [MobileBy.ID, "com.hjkj.hjmall:id/et_new_customer_address"]
    # 提交审核
    SUBMIT_AUDIT = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提交审核").instance(0);']

