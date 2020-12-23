# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail: xueqinyao@dingtalk.com
# @software: pycharm
# @file: display_wait.py
# @time: 2020/2/12 0:58
# @此模块提供：显示等待的几种办法（一般用来处理打开APP后的升级或广告弹窗处理(可放在初始化函数中)）
"""

# 一、
# # 此种方法不推荐(拖长整个代码的运行时间)
# time.sleep(10)
# if len(self.driver.find_elements_by_id("com.hjkj.hjmall:id/tv_commodity_detail_addtocart")) >= 1:
#     self.driver.find_element_by_id("com.hjkj.hjmall:id/tv_commodity_detail_addtocart").click()

# 二、
# # 显示等待15秒，在设定时间内不断检查元素是否出现，一旦出现则点击元素，不一定会一直等到15秒
# WebDriverWait(self.driver, 15).until(lambda x: len(self.driver.find_elements_by_id("tv_commodity_detail_addtocart")) >= 1)
# self.driver.find_element_by_id("com.hjkj.hjmall:id/tv_commodity_detail_addtocart").click()

# # 三、
# # 使用excepted_conditions方法来进行显示等待操作
# # 不足：如果元素不出现,下面的点击操作将会报错
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# WebDriverWait(self.driver, 15).until(
#     expected_conditions.visibility_of_element_located((By.ID, "tv_commodity_detail_addtocart"))
# )
# self.driver.find_element_by_id("com.hjkj.hjmall:id/tv_commodity_detail_addtocart").click()

# # 四、
# # 嵌套函数
# import datetime
# from selenium.webdriver.support.wait import WebDriverWait
# def one(dri):
#     def loaded(driver):
#         print(datetime.datetime.now())
#         if len(driver.find_elements_by_id("com.hjkj.hjmall:id/tv_commodity_detail_addtocart")) >= 1:
#             driver.find_element_by_id("com.hjkj.hjmall:id/tv_commodity_detail_addtocart").click()
#             return True
#         else:
#             return False
#     try:
#         WebDriverWait(dri, 15).until(loaded(dri))
#     except:
#         print("no update")
