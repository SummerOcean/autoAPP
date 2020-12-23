# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file: Middleware_Handler.py
# @time: 2020/6/14 17:42
# @此模块提供：初始化配置(中间调用层)
"""
import os, random, datetime, time
from os import path
from salesman_Config import ConfigPath
from salesman_Common import Log, Read_Yaml, Report, Send_email


class HandlerData(object):
    # 读取yaml配置文件
    yaml = Read_Yaml.read_yaml(ConfigPath.YAML_PATH)

    # 初始化日志
    _LOG_CONFIG = yaml['log']
    _LOG_TIME = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
    _LOG_NAME = _LOG_CONFIG['Logname'] + _LOG_TIME + ".log"
    logger = Log.LoggerHandler(
        name=_LOG_CONFIG['name'],
        file_path=_LOG_CONFIG['file_path'] + _LOG_NAME,
        file_level=_LOG_CONFIG['file_level'],
        get_logger_level=_LOG_CONFIG['get_logger_level'],
        handler_level=_LOG_CONFIG['handler_level'],
    )

    # 初始化测试报告
    _REPORT_CONFIG = yaml['report']
    # _REPORT_TIME = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    _REPORT_TIME = datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
    _REPORT_NAME = _REPORT_CONFIG['html_name'] + _REPORT_TIME + '.html'
    reports = Report.ReportHtml(
        search_path=_REPORT_CONFIG['search_path'],
        match_name=_REPORT_CONFIG['match_name'],
        level_dir=None,
        html_file=_REPORT_CONFIG['html_path'] + _REPORT_NAME,
        report_title=_REPORT_CONFIG['report_title'],
        report_description=_REPORT_CONFIG['report_description'],
        tester=_REPORT_CONFIG['tester']
    )

    def sending_email(self):
        """初始化发送邮件"""
        # 定义HTML格式的正文内容
        _HTML_TEXT = '''
                        <html>
                        <body>
                        <h3>致远建议：</h3>
                        <h4>txt、log附件可手机预览,HTML附件请用电脑查看。</h4>
                        <a><img src="cid:image1" width="950" height="580"></a>
                        </body>
                        </html>
                      '''
        _EMAIL_CONFIG = self.yaml['sendemail']
        _NEW_FILE_PATH = self.yaml['find_new_file']
        Send_email.SendEmail(
            from_address=_EMAIL_CONFIG['from_address'],
            to_address=_EMAIL_CONFIG['to_address'],
            from_header=_EMAIL_CONFIG['from_header'],
            to_header=_EMAIL_CONFIG['to_header'],
            mail_subject=_EMAIL_CONFIG['mail_subject'],
            report_file=self.Find_New_file(_NEW_FILE_PATH['report_file']),
            log_file=self.Find_New_file(_NEW_FILE_PATH['log_file']),
            html=_HTML_TEXT,
            random_picture=self.Random_picture(),
            email_from_server=_EMAIL_CONFIG['email_from_server'],
            email_from_username=_EMAIL_CONFIG['email_from_username'],
            email_from_password=_EMAIL_CONFIG['email_from_password'],
        ).send_email(
            add_report=True,
            add_log=True,
            debug=False
        )

    def Random_picture(self):
        """随机选取一张图片,并返回完整路径"""
        _PICTURE_PATH = self.yaml['random_picture']['picture_path']
        _RANDOM_PICTURE = str(random.randint(1, 77))
        _PICTURE = _PICTURE_PATH + _RANDOM_PICTURE + ".jpg"
        self.logger.info('本次图片:{}'.format(_PICTURE))
        return _PICTURE

    def Find_New_file(self, file_path):
        """筛选最新文件,并返回完整路径"""
        lists = os.listdir(file_path)
        # getmtime：根据文件时间排序
        lists.sort(key=lambda find_file: path.getmtime(file_path + "\\" + find_file))
        # 将最新文件与该路径拼接
        new_file_path = path.join(file_path, lists[-1])
        self.logger.info("本次文件:{}".format(new_file_path))
        return new_file_path

    @staticmethod
    def generate_shop_name():
        """生成一个店铺名称"""
        return "Test店铺" + str(time.time() * 1000)[8:13]

    @property
    def random_mobile_phone(self):
        """生成11位数字号码"""
        tamps = time.time() * 10
        return str(tamps).split('.')[0]


# if __name__ == '__main__':
#     print(HandlerData().yaml['shop_boss_name'])
