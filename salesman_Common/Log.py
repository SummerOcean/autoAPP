# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file: Log.py
# @time: 2020/6/3 15:46
# @此模块提供：记录运行日志的方法
"""
import logging


class LoggerHandler(logging.Logger):
    """记录日志的类，继承于logging.logger对象"""
    def __init__(self,
                 name=None,
                 file_path=None,
                 file_level="INFO",
                 get_logger_level="DEBUG",
                 handler_level="DEBUG",
                 formatter="%(pathname)s--%(asctime)s--%(levelname)s--%(lineno)s: %(message)s"
                 ):
        # 继承于Logger类 (等同于logger = logging.getLogger())
        super().__init__(name, get_logger_level)

        # 得到一个日志收集器
        self.setLevel(get_logger_level)

        # 向控制台输出
        handler = logging.StreamHandler()
        handler.setLevel(handler_level)
        self.addHandler(handler)

        # 将控制台输出器和文件输出器 设置格式化参数
        formatter = logging.Formatter(formatter)
        handler.setFormatter(formatter)

        if file_path:
            # 向文件输出
            file_handler = logging.FileHandler(file_path)
            file_handler.setLevel(file_level)
            self.addHandler(file_handler)
            file_handler.setFormatter(formatter)


# if __name__ == '__main__':
#     logger = LoggerHandler()
#     logger.info("info")
#     logger.debug("debug")
#     logger.warning("warning")
#     logger.error("error")
#     logger.critical("critical")
