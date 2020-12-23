# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file: Read_Yaml.py
# @time: 2020/6/3 15:41
# @此模块提供：读取yaml文件数据的通用方法
"""
import yaml


def read_yaml(file_path):
    """读取yaml文件的方法"""
    with open(file_path, "r", encoding="utf-8") as file:
        config_data = yaml.load(file, Loader=yaml.SafeLoader)
    return config_data
