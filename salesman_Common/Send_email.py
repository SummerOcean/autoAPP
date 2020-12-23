# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file: Send_email.py
# @time: 2020/7/13 17:12
# @此模块提供：发送邮件(邮件为附件形式)的方法
"""
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header


class SendEmail(object):
    message = MIMEMultipart()
    smtp = smtplib.SMTP()

    def __init__(self,
                 from_address=None,
                 to_address=None,
                 from_header="薛钦耀",
                 to_header="我",
                 mail_subject="自动化测试报告_致远",
                 report_file=None,
                 log_file=None,
                 html="""<html><body><h3>python发送的邮件...</h3></body></html>""",
                 random_picture=None,
                 email_from_server=None,
                 email_from_username=None,
                 email_from_password=None
                 ):
        self.email_from_server = email_from_server
        self.from_address = from_address
        self.to_address = to_address
        self.email_from_username = email_from_username
        self.email_from_password = email_from_password
        self.report_file = report_file
        self.log_file = log_file
        self.from_header = from_header
        self.to_header = to_header
        self.mail_subject = mail_subject
        self.html = html
        self.random_picture = random_picture

    def email_title(self):
        # 发件人抬头名称
        self.message['From'] = Header(self.from_header, 'utf-8')
        # 收件人抬头名称
        self.message['To'] = Header(self.to_header, 'utf-8')
        # 邮件主题
        self.message['Subject'] = Header(self.mail_subject, 'utf-8')
        # html页面内容
        self.message.attach(MIMEText(self.html, 'html', 'utf-8'))
        # 构造图片
        self.email_picture()

    def email_picture(self):
        # 随机读取一张图片
        choice_image = self.random_picture
        image = open(choice_image, "rb")
        message_image = MIMEImage(image.read())
        image.close()
        # 定义图片ID 并在HTML中引用
        message_image.add_header('Content-ID', '<image1>')
        # 将读取出的图片添加到邮件中
        self.message.attach(message_image)

    def email_attachment(self, file):
        try:
            # 读取文件内容
            new_file = open(file, 'rb+')
            attachment = MIMEText(new_file.read(), "base64", "utf-8")
            attachment["Content-Type"] = 'application/octet-stream'
            new_file.close()
            # 将路径去掉，只取文件名称
            file_name = os.path.basename(file)
            # 设置附件的名称
            attachment.add_header('Content-Disposition', 'attachment', filename=('gbk', '', file_name))
            self.message.attach(attachment)
        except Exception as error:
            raise error

    def send_email(self, add_report=True, add_log=False, debug=False):
        self.email_title()
        if add_report:
            self.email_attachment(self.report_file)
        if add_log:
            self.email_attachment(self.log_file)
        try:
            self.smtp.connect(self.email_from_server)
            if debug:
                # 查看与邮箱服务器交互的信息
                self.smtp.set_debuglevel(1)
            self.smtp.login(self.email_from_username, self.email_from_password)
            self.smtp.sendmail(self.from_address, self.to_address, self.message.as_string())
            self.smtp.quit()
        except Exception as error:
            raise error
