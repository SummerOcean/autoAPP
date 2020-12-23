# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: __init__.py.py
# @create_time: 2020/10/22 10:15
# @project: ZYSY_同商云商业资源管理系统
# @project: ZYSY_同商通汇APP
# @project: ZYSY_同商捷配APP
# @此模块提供：
"""
import unittest, ddt, json
from ZYTS_HJKJ_PROJECT.ERP_Interface.interface_Middleware.Middleware_Handler import HandlerData
from ZYTS_HJKJ_PROJECT.ERP_Interface.interface_Common.requests_handler import RequestsHandler

handler = HandlerData()
login_data = handler.excel.read_data('')


@ddt.ddt()
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        handler.logger.info('登录接口前置条件')

    @classmethod
    def tearDownClass(cls):
        handler.logger.info('登录接口后置条件')

    @ddt.data(*login_data)
    def test_login(self, data_info):
        handler.logger.info('当前用例名:{}'.format(data_info['case_name']))
        handler.logger.info('正在访问接口...')
        response = RequestsHandler(
            url=handler.Yaml['host']['test_url'] + data_info['url'],
            method=data_info['method']
        ).visit_requests(
            headers=json.loads(),
            data=json.loads()
        )
        handler.logger.info('接口访问结束')
        try:
            data_info = json.loads(data_info['expected'])
            handler.logger.info('正在断言code...')

            handler.logger.info('code断言成功')
            handler.logger.info('正在断言message...')

            handler.logger.info('message断言成功')
            handler.excel.write_data('', data_info['case_id'] + 1, 9, 'PASS')
        except Exception as error:
            handler.logger.error('断言异常：{}'.format(error))
            handler.excel.write_data('', data_info['case_id'] + 1, 9, 'case_failed')
            raise error


if __name__ == '__main__':
    unittest.main()
