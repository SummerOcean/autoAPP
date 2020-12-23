# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file: Report.py
# @time: 2020/6/9 18:08
# @此模块提供：自动匹配且运行测试用例的方法
"""
import unittest
from salesman_Libs import HTMLTestRunnerNew


class ReportHtml(object):

    def __init__(self,
                 search_path=None,
                 match_name=None,
                 level_dir=None,
                 html_file=None,
                 report_title=None,
                 report_description=None,
                 tester=None
                 ):
        self.search_path = search_path
        self.match_name = match_name
        self.level_dir = level_dir
        self.html_file = html_file
        self.report_title = report_title
        self.report_description = report_description
        self.tester = tester

    def discover_file(self):
        discover = unittest.defaultTestLoader.discover(
            start_dir=self.search_path,
            pattern=self.match_name,
            top_level_dir=self.level_dir
        )
        return discover

    def report_html(self):
        with open(self.html_file, 'wb+') as htmlfile:
            execute = HTMLTestRunnerNew.HTMLTestRunner(
                stream=htmlfile,
                title=self.report_title,
                description=self.report_description,
                tester=self.tester
            )
            execute.run(
                self.discover_file()
            )

