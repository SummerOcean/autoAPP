# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: Config.py
# @create_time: 2020/9/1 18:29
# @此模块提供：
"""
from os import path

# 项目配置文件路径
CONFIG_PATH = path.dirname(path.abspath(__file__))

# 项目根路径
ROOT_PATH = path.dirname(CONFIG_PATH)

# 测试报告路径
REPORT_PATH = path.join(ROOT_PATH, r'salesman_Reports\\')

# 测试日志路径
LOG_PATH = path.join(ROOT_PATH, r'salesman_Logs\\')

# 测试用例路径
TestCase_PATH = path.join(ROOT_PATH, r'salesman_TestCases\\')

# 图片路径
PICTURE_PATH = path.join(ROOT_PATH, r'salesman_Images\Screenshot\\')

# yaml配置文件路径
YAML_PATH = path.join(CONFIG_PATH, r'SalesmanConfig.yaml')


# if __name__ == '__main__':
#     print(CONFIG_PATH)
#     # print(ROOT_PATH)
#     # print(REPORT_PATH)
#     # print(PICTURE_PATH)
#     print(YAML_PATH)
