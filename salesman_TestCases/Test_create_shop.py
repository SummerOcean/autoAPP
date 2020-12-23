# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail: xueqinyao@dingtalk.com
# @software: pycharm
# @file: test_salesman_create_shop.py
# @time: 2020/2/14 17:24
# @project: salesman_APP
# @此模块提供：创建店铺的方法
"""
import unittest, random, allure
from salesman_PageObject import login_page, base_page, create_customer_page
from salesman_Middleware.Middleware_Handler import HandlerData

handler = HandlerData()


@allure.feature('创建店铺')
class CreateShop(unittest.TestCase):
    def setUp(self):
        self.driver = base_page.BasePage().starting()

    def tearDown(self):
        self.driver.quit()

    @allure.story('成功创建店铺')
    @allure.description('描述：此用例用于测试店铺创建成功的真正向业务流程')
    @allure.step('创建店铺')
    def test_create_shop(self):
        with allure.step('第一步：登录业务员账号'):
            # 用户登录
            login_page.LoginPage(self.driver).login(
                handler.yaml['username_test']['company_salesman'], handler.yaml['user_password']
            )
        with allure.step('第二步：填写店铺信息'):
            # 页面操作
            create_customer = create_customer_page.CreateCustomerPage(self.driver)
            create_customer \
                .click_new_customer_button() \
                .input_customer_number(handler.random_mobile_phone) \
                .input_user_pwd(handler.yaml['user_password']) \
                .input_customer_name(handler.generate_shop_name()) \
                .input_boss_name(random.choice(handler.yaml['shop_boss_name'])) \
                .select_shop_type() \
                .input_shop_customize_address(handler.yaml['shop_address']) \
                .upload_shop_picture() \
                .click_submit_audit() \
                .assert_create_success()


if __name__ == '__main__':
    unittest.main()
