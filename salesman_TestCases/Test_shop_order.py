# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail: xueqinyao@dingtalk.com
# @software: pycharm
# @file: test_salesman_order.py
# @time: 2020/2/14 14:48
# @project: 同商通汇APP
# @此模块提供：业务员下单的操作流程
"""
import unittest, allure
from salesman_PageObject import base_page, login_page, create_order_page
from salesman_Middleware.Middleware_Handler import HandlerData

handler = HandlerData()


@allure.feature('下单')
class CreateShopOrder(unittest.TestCase):
    def setUp(self):
        self.driver = base_page.BasePage().starting()

    def tearDown(self):
        self.driver.quit()

    @allure.story('业务员下单')
    @allure.description('描述:业务员帮助店铺下单的正向业务流程')
    def test_create_order(self):
        """同商通汇APP-下单流程"""
        login_page.LoginPage(self.driver).login(
            handler.yaml['username_test']['company_salesman'], handler.yaml['user_password']
        )
        # 操作页面
        createorder = create_order_page.CreateOrderPage(self.driver)
        createorder \
            .select_shop() \
            .click_order_button() \
            .select_commodity() \
            .select_warehouse('SFBP致远3号仓库') \
            .add_shopping_cart() \
            .select_shopping() \
            .add_commodity_quantity() \
            .select_all_commodity() \
            .click_settle_accounts() \
            .click_detail_pay() \
            .input_order_mark('automator marks') \
            .get_order_quantity_money() \
            .get_order_delivery_pay() \
            .click_submit_order() \
            .get_order_success_msg() \
            .click_back_button()


if __name__ == '__main__':
    unittest.main()
