# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail: xueqinyao@dingtalk.com
# @software: pycharm
# @file: caps_demo.py
# @time: 2020/2/11 22:44
# @此模块提供：初始化相关caps参数的方法
# @caps设置官方地址：http://appium.io/docs/en/writing-running-appium/caps/
"""

# # 方法一：以字典形式传递参
# from appium import webdriver
#
# caps = {"deviceName": "127.0.0.1:62001", "platformName": "android", "appPackage": "com.hjkj.hjmall",
#         "appActivity": "com.hjkj.hjmall.welcome.SplashActivity"}
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


# # 方法二：
# from appium import webdriver
#
# caps = {}
# # 设备地址及端口号
# # caps["deviceName"] = "127.0.0.1:62001"  # 夜神模拟器
# caps["deviceName"] = "192.168.1.4:5555"  # 小米手机
#
# # 设备系统
# caps["platformName"] = "android"
# # 对应的包名
# caps["appPackage"] = "com.hjkj.hjmall"
# # 对应app包的入口
# caps["appActivity"] = "com.hjkj.hjmall.welcome.SplashActivity"
#
# # 设置可输入中文
# caps["unicodeKeyboard"] = True
# # 如果为True,下次启动时不清理APP的缓存数据
# caps["noReset"] = True
# # 让Appium自动确定您的应用所需的权限，并在安装时将其授予应用，默认为false。如果noReset为true，则此功能不起作用。
# caps["autoGrantPermissions"] = True
# # 当查找操作失败时，打印当前页面源。默认为false。
# caps["printPageSourceOnFindFailure"] = True
#
# # # 指定对哪一台设备进行操作,(有deviceName的设置后，一般不用此参数)
# # caps["udid"] = ""
#
# # 启动设备，并初始化相关参数
# self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# # 隐式等待(全局)
# self.driver.implicitly_wait(20)
