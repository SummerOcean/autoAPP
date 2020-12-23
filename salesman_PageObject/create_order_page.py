# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: shop_order_page.py
# @create_time: 2020/11/18 15:17
# @project: 同商通汇APP
# @此模块提供：下单流程
"""
import time
from salesman_Middleware.Middleware_Handler import HandlerData
from salesman_PageObject import base_page
from salesman_Elements.create_order_element import CreateOrderElement

handler = HandlerData()
createorder = CreateOrderElement()


class CreateOrderPage(base_page.BasePage):
    """同商通汇APP店铺下单页面"""
    def __init__(self, driver):
        self.driver = driver
        handler.logger.info('正在初始化页面:店铺下单...')
        self.click_shop_button()

    def click_shop_button(self):
        """在主页点击‘店铺’按钮,以切换至店铺列表"""
        self.driver.tap([(150, 1540), (150, 1540)], 100)
        handler.logger.info('在主页点击‘店铺’按钮,以切换至店铺列表')
        return self

    def select_shop(self):
        """选择一个下单的店铺"""
        time.sleep(0.8)
        self.random_tap_coordinate(450, 450, 250, 1400, Y=True)
        handler.logger.info('选择一个下单的店铺')
        return self

    def click_order_button(self):
        """点击下单按钮"""
        self.driver.find_element(*createorder.ORDER_BUTTON).click()
        handler.logger.info('点击下单按钮')
        return self

    def select_commodity(self):
        """选择商品：旺仔牛奶 原味 300ml 1x1"""
        self.driver.find_element(*createorder.SELECT_COMMODITY_wangzai).click()
        handler.logger.info('选择商品：旺仔牛奶 原味 300ml 1x1')
        return self

    def select_warehouse(self, assign_warehouse_name=False):
        """
        选择仓库：
        1、默认随机选择
        2、指定仓库：需要传入仓库名称
        """
        self.driver.find_element(*createorder.WAREHOUSE_LIST_SELECT).click()
        if assign_warehouse_name:
            self.select_assign_warehouse(assign_warehouse_name)
            handler.logger.info('选择仓库(指定)：{}'.format(assign_warehouse_name))
            self.get_warehouse_total()
            return self
        time.sleep(0.4)
        self.random_tap_coordinate(450, 450, 700, 1450, Y=True)
        time.sleep(0.5)
        warehouse_name = self.driver.find_element(*createorder.WAREHOUSE_LIST_SELECT).text
        handler.logger.info('选择仓库(随机)：{}'.format(warehouse_name))
        self.get_warehouse_total()
        return self

    def get_warehouse_total(self):
        """获取已选择仓库库存"""
        warehouse_total = self.driver.find_element(*createorder.WAREHOUSE_QUANTITY).text
        handler.logger.info('商品{}'.format(warehouse_total))

    def add_shopping_cart(self):
        """加入购物车"""
        # 加入购物车：进入商品规格选择页面
        self.random_tap_coordinate(680, 680, 1550, 1550, X=True)
        # 确认将商品加入购物车
        self.driver.find_element(*createorder.ADD_SHOPPING_CART_TWO).click()
        handler.logger.info('加入购物车')
        return self

    def select_shopping(self):
        """点击购物车按钮，进入购物车页面"""
        time.sleep(0.4)
        self.random_tap_coordinate(370, 370, 1550, 1550, X=True)
        handler.logger.info('点击购物车按钮，进入购物车页面')
        return self

    def add_commodity_quantity(self):
        """添加商品数量"""
        goods_quantity = ''
        for goods_quantity in range(1, 5):
            self.driver.find_element(*createorder.ADD_COMMODITY_QUANTITY).click()
        handler.logger.info('添加商品数量:{}'.format(goods_quantity))
        return self

    def select_all_commodity(self):
        """勾选全部商品"""
        self.driver.find_element(*createorder.ALL_COMMODITY).click()
        handler.logger.info('勾选全部商品')
        return self

    def click_settle_accounts(self):
        """点击结算按钮"""
        self.driver.find_element(*createorder.SETTLE_ACCOUNTS).click()
        handler.logger.info('点击结算按钮')
        return self

    def click_detail_pay(self):
        """点击查看明细并支付按钮"""
        self.driver.find_element(*createorder.DETAIL_AND_PAY).click()
        handler.logger.info('点击查看明细并支付按钮')
        return self

    def input_order_mark(self, mark_msg):
        """输入订单备注"""
        self.driver.find_element(*createorder.ORDER_MARK).send_keys(mark_msg)
        handler.logger.info('输入订单备注')
        return self

    def get_order_quantity_money(self):
        """获取订单的商品数及总金额"""
        # 商品总数
        _commodity_quantity = self.driver.find_element(*createorder.COMMODITY_QUANTITY).text
        handler.logger.info('订单商品总数：{}'.format(_commodity_quantity))
        # 商品总金额
        _commodity_total_price = self.driver.find_element(*createorder.COMMODITY_TOTAL_PRICE).text
        handler.logger.info('订单商品总金额：{}'.format(str(_commodity_total_price).split('¥')[1]))
        return self

    def get_order_delivery_pay(self):
        """获取订单支付方式及配送方式"""
        # 支付方式
        _order_pay = self.driver.find_element(*createorder.ORDER_PAY_MODE).text
        handler.logger.info('支付方式为：{}'.format(_order_pay))
        # 配送方式
        _order_delivery = self.driver.find_element(*createorder.ORDER_DELIVERY_MODE).text
        handler.logger.info('配送方式为：{}'.format(_order_delivery))
        return self

    def click_submit_order(self):
        """点击提交订单按钮"""
        self.driver.find_element(*createorder.SUBMIT_ORDER).click()
        handler.logger.info('点击提交订单按钮')
        return self

    def get_order_success_msg(self):
        """获取下单成功页面提示信息"""
        order_success = self.driver.find_element(*createorder.ORDER_SUCCESS).text
        handler.logger.info(order_success)
        return self

    def click_back_button(self):
        """点击返回工作台按钮"""
        self.driver.find_element(*createorder.BACK_OPERATING_FLOOR).click()
        handler.logger.info('点击返回工作台按钮')
        return self

    def click_carry_order(self):
        """点击继续下单按钮"""
        self.driver.find_element(*createorder.CARRY_ON_ORDER).click()
        handler.logger.info('点击继续下单按钮')
        return self

