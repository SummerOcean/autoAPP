# encoding: utf-8
"""
# @Author : 薛钦耀
# @Software: PyCharm
# @E-mail: xueqinyao@dingtalk.com
# @Time : 2020/11/19 14:48
# @File : return_order_page.py
# @project：同商通汇APP
# @此模块提供：
"""
import time
from salesman_PageObject import create_order_page
from salesman_Middleware.Middleware_Handler import HandlerData
from salesman_Elements.return_order_element import ReturnOrderElement

handler = HandlerData()
returnorderelement = ReturnOrderElement()


class ReturnOrderPage(create_order_page.CreateOrderPage):
    def __init__(self, driver):
        self.driver = driver
        self.exchange_shop_page()

    def exchange_shop_page(self):
        """切换到店铺页面"""
        super().click_shop_button().select_shop()
        handler.logger.info("切换到店铺页面且选择一个店铺")

    def click_return_button(self):
        """点击退货按钮"""
        self.driver.find_element(*returnorderelement.SHOP_RETURN_BUTTON).click()
        handler.logger.info('点击退货按钮')
        return self

    def add_goods_quantity(self):
        """增加退货商品数量"""
        self.add_commodity_quantity()
        return self

    def click_return_goods_list(self):
        """点击退货列表按钮"""
        self.driver.find_element(*returnorderelement.RETURN_LIST_BUTTON).click()
        handler.logger.info('点击退货列表按钮')
        return self

    def click_select_warehouse_list(self):
        """选择仓库：随机"""
        self.driver.find_element(*returnorderelement.SELECT_RETURN_WAREHOUSE).click()
        handler.logger.info('点击仓库选择列表')
        self.random_tap_coordinate(770, 770, 270, 700, Y=True)
        _warehouse_name = self.driver.find_element(*returnorderelement.SELECT_RETURN_WAREHOUSE).text
        handler.logger.info('仓库已选择：{}'.format(_warehouse_name))
        return self

    def click_all_select_button(self):
        """点击全选按钮"""
        self.driver.find_element(*returnorderelement.ALL_SELECT_BUTTON).click()
        handler.logger.info('点击全选按钮')
        return self

    def click_confirm_button(self):
        """点击结算按钮"""
        self.driver.find_element(*returnorderelement.CONFIRM_GOODS_BUTTON).click()
        handler.logger.info('点击结算按钮')
        return self

    def select_return_price_method(self):
        """选择退款方式"""
        self.driver.find_element(*returnorderelement.RETURN_PRICE_METHOD).click()
        time.sleep(0.4)
        self.random_tap_coordinate(780, 780, 480, 610, Y=True)
        handler.logger.info('选择退款方式')
        return self

    def return_order_mark(self, mark_msg):
        """输入退货订单备注"""
        self.driver.find_element(*returnorderelement.ORDER_NOTE).send_keys(mark_msg)
        handler.logger.info('输入退货订单备注')
        return self

    def get_return_goods_message(self):
        """获取退货商品信息"""
        _return_price_method = self.driver.find_element(*returnorderelement.RETURN_PRICE_METHOD).text
        handler.logger.info('退款方式:{}'.format(_return_price_method))
        _return_method = self.driver.find_element(*returnorderelement.RETURN_GOODS_METHOD).text
        handler.logger.info('退货方式:{}'.format(_return_method))
        _goods_quantity = self.driver.find_element(*returnorderelement.RETURN_GOODS_QUANTITY).text
        handler.logger.info('商品数量:{}'.format(_goods_quantity))
        _total_price = self.driver.find_element(*returnorderelement.RETURN_ORDER_QUANTITY).text
        handler.logger.info('合计金额:{}'.format(str(_total_price).split('¥')[1]))
        return self

    def click_submit_order_button(self):
        """点击提交订单按钮"""
        self.driver.find_element(*returnorderelement.SUBMIT_ORDER).click()
        handler.logger.info('点击提交订单按钮')
        return self

    def assert_order_toast(self):
        """判断订单是否提交成功"""
        self.assert_toast_message("提交成功")

