# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: create_order_element.py
# @create_time: 2020/11/13 11:11
# @project: 同商通汇APP
# @此模块提供：
"""
from appium.webdriver.common.mobileby import MobileBy


class CreateOrderElement:
    """店铺-下单页面元素"""
    # 点击下单按钮
    ORDER_BUTTON = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("下单").instance(0)']
    # 选择商品
    SELECT_COMMODITY_wangzai = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("300ml|原味|(罐)*1").instance(0);']
    # 点击仓库列表
    WAREHOUSE_LIST_SELECT = [MobileBy.ID, "tv_detail_commodity_repertory"]
    # 获取库存数量
    WAREHOUSE_QUANTITY = [MobileBy.ID, 'tv_detail_commodity_repertory_count']
    # 点击加入购物车
    ADD_SHOPPING_CART_TWO = [MobileBy.ID, "ll_popup_detail_buy_bottom"]
    # 添加商品数量
    ADD_COMMODITY_QUANTITY = [MobileBy.ID, "add"]
    # 选择购物车中的所有商品
    ALL_COMMODITY = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全选").instance(0);']
    # 点击结算按钮
    SETTLE_ACCOUNTS = [MobileBy.ID, "tv_cart_bottom_confirm"]
    # 点击 查看明细并支付
    DETAIL_AND_PAY = [MobileBy.ID, "tv_cart_split_order_item_confirm"]
    # 订单备注
    ORDER_MARK = [MobileBy.ID, 'tv_cart_order_commodity_amount_note']
    # 商品总数
    COMMODITY_QUANTITY = [MobileBy.ID, 'tv_cart_order_totalcount']
    # 商品总金额
    COMMODITY_TOTAL_PRICE = [MobileBy.ID, 'tv_cart_order_totalprice']
    # 订单配送方式
    ORDER_DELIVERY_MODE = [MobileBy.ID, 'tv_cart_order_commodity_amount_send']
    # 订单支付方式
    ORDER_PAY_MODE = [MobileBy.ID, 'tv_cart_order_waytopay']
    # 点击提交订单按钮
    SUBMIT_ORDER = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提交订单").instance(0);']
    # 获取下单成功提示
    ORDER_SUCCESS = [MobileBy.XPATH, "//*[@text='下单成功！']"]
    # 返回工作台按钮
    BACK_OPERATING_FLOOR = [MobileBy.ID, "tv_order_succeed_back_to_ws"]
    # 继续下单按钮 carry on
    CARRY_ON_ORDER = [MobileBy.ID, "tv_order_succeed_back_to_sm"]

