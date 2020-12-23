# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail: xueqinyao@dingtalk.com
# @software: pycharm
# @file: test_salesman_return_goods.py
# @time: 2020/2/21 10:46
# @project: 同商通汇APP
# @此模块提供：退货流程
"""
import unittest, allure
from salesman_PageObject import base_page, login_page, return_order_page
from salesman_Middleware.Middleware_Handler import HandlerData

handler = HandlerData()


@allure.feature('店铺')
class ReturnGoodsOrder(unittest.TestCase):
    def setUp(self):
        self.driver = base_page.BasePage().starting()

    def teardown(self):
        self.driver.quit()

    @allure.story('店铺商品退货')
    @allure.description('描述：商品退货的正向业务流程')
    def test_return_goods_order(self):
        """商品退货流程"""
        # 登录
        login_page.LoginPage(self.driver).login(
            handler.yaml['username_test']['company_salesman'], handler.yaml['user_password']
        )
        # 页面操作
        returnorderpage = return_order_page.ReturnOrderPage(self.driver)
        returnorderpage \
            .click_return_button() \
            .add_goods_quantity() \
            .click_return_goods_list() \
            .click_select_warehouse_list() \
            .click_all_select_button() \
            .click_confirm_button() \
            .select_return_price_method() \
            .return_order_mark("测试退货备注") \
            .get_return_goods_message() \
            .click_submit_order_button() \
            .assert_order_toast()


if __name__ == '__main__':
    unittest.main()
