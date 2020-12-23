# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file: Runner_TestCases.py
# @time: 2020/7/22 16:27
# @此模块提供：收集和执行用例的方法
"""
import pytest
from salesman_Middleware.Middleware_Handler import HandlerData
from salesman_Config import ConfigPath


handler = HandlerData()

if __name__ == '__main__':
    pytest.main(
        [   # 指定测试报告存放路径
            "--alluredir={}AllureSalesman".format(ConfigPath.REPORT_PATH),
            # 指定测试用例路径
            ConfigPath.TestCase_PATH,
            # 向控制台输出打印内容:不会同时输出到文件
            # '-s',
            # 查看每一条用例的详细执行过程
            '-v',
            # 只执行上次执行失败的测试用例
            # '--last-failed',
        ]
    )

    # 生成HTML格式报告
    # handler.reports.report_html()

    # # 发送邮件
    # try:
    #     handler.logger.info('E-mail sending...')
    #     handler.sending_email()
    #     handler.logger.info('E-mail send success!')
    # except Exception as SMTPError:
    #     handler.logger.error('E-mail send failed!!!')
    #     raise SMTPError
