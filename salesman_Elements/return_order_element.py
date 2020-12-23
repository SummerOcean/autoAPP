# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: return_order_element.py
# @create_time: 2020/11/13 11:13
# @project: 同商通汇APP
# @此模块提供：退货流程的页面元素
"""
from appium.webdriver.common.mobileby import MobileBy


class ReturnOrderElement:
    """店铺页面：退货"""
    # 选择店铺
    SELECT_SHOP = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SFSF烟酒店").instance(0)']
    # 点击 退货
    SHOP_RETURN_BUTTON = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("退货").instance(0)']
    # 增加一个商品的数量
    ADD_RETURN_GOODS = [MobileBy.ID, 'com.hjkj.hjmall:id/add']
    # 点击 退货列表按钮 进入确认页
    RETURN_LIST_BUTTON = [MobileBy.ID, 'com.hjkj.hjmall:id/tv_sales_return_list']
    # 退货仓库 下拉框
    SELECT_RETURN_WAREHOUSE = [MobileBy.ID, "com.hjkj.hjmall:id/tv_src_item_warehouse"]
    # 点击全选按钮
    ALL_SELECT_BUTTON = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全选").instance(0)']
    # 结算按钮
    CONFIRM_GOODS_BUTTON = [MobileBy.ID, 'tv_sales_return_confirm_confirm']
    # --------------------未用元素-----------------
    # 退货单价 按钮
    RETURN_PRICE_BUTTON = [MobileBy.ID, "com.hjkj.hjmall:id/tv_src_item_commodity_autoprice"]
    # 输入 自定义单价
    CUSTOMIZE_PRICE = [MobileBy.CLASS_NAME, "android.widget.EditText"]
    # 点击 自定义单价 确定按钮
    SURE_CUSTOMIZE_PRICE = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定").instance(0)']
    # 输入后的退货单价 并断言价格
    INPUT_RETURN_PRICE = [MobileBy.ID, "com.hjkj.hjmall:id/tv_src_item_commodity_autoprice"]
    # 商品数量
    SURE_COMMODITY_QUANTITY = [MobileBy.ID, "com.hjkj.hjmall:id/num"]
    # -------------------------------------
    # 输入订单备注
    ORDER_NOTE = [MobileBy.ID, "com.hjkj.hjmall:id/tv_sales_return_order_company_amount_note"]
    # 选择 退款方式
    RETURN_PRICE_METHOD = [MobileBy.ID, 'com.hjkj.hjmall:id/tv_sales_return_order_waytopay']
    # 获取 退货方式
    RETURN_GOODS_METHOD = [MobileBy.ID, "tv_sales_return_order_company_amount_send"]
    # 获取 商品数量
    RETURN_GOODS_QUANTITY = [MobileBy.ID, 'com.hjkj.hjmall:id/tv_sales_return_order_totalcount']
    # 获取 订单金额：合计金额
    RETURN_ORDER_QUANTITY = [MobileBy.ID, 'com.hjkj.hjmall:id/tv_sales_return_order_totalprice']
    # 点击 提交订单 按钮
    SUBMIT_ORDER = [MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("提交订单").instance(0)']
