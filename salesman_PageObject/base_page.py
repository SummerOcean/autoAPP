# encoding: utf-8
"""
# @author: 薛钦耀
# @E-mail:xueqinyao@dingtalk.com
# @software: pycharm
# @file_name: Base_page.py
# @create_time: 2020/8/11 20:35
# @此模块提供：公共页面(通用方法)
"""
import time, random
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from salesman_Middleware.Middleware_Handler import HandlerData
from salesman_Config import ConfigPath

handler = HandlerData()


class BasePage:
    def __init__(self):
        self.caps = handler.yaml['devices_caps']
        # 启动设备，并初始化相关参数
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)

    def starting(self):
        """启动设备"""
        # 隐式等待(全局)
        self.driver.implicitly_wait(10)
        return self.driver

    def assert_toast_message(self, assert_msg):
        """断言弹窗信息"""
        _TOAST_ELEMENT = "//*[@class='android.widget.Toast']"
        _TOAST_TEXT = self.driver.find_element_by_xpath(_TOAST_ELEMENT).text
        assert _TOAST_TEXT == assert_msg
        handler.logger.info('断言成功：{}'.format(assert_msg))

    def find_element(self, by, value):
        """查找元素"""
        try:
            return self.driver.find_element(by, value)
        except Exception as elementError:
            handler.logger.info('元素查找异常:{}'.format(elementError))
            raise elementError

    def get_screenshot(self, picture_name=''):
        """截图"""
        screenshot_time = time.strftime('%Y-%m-%d-%H_%M_%S')
        file_path = ConfigPath.PICTURE_PATH
        return self.driver.get_screenshot_as_file(
            file_path + picture_name + screenshot_time + '.png'
        )

    def random_tap_coordinate(self, random_x1, random_x2, random_y1, random_y2, X=False, Y=False):
        """
        1、在传入中的数字中随机选出一个数字，然后根据该数字来决定点击的坐标范围(根据X或Y参数为真时来决定)
        2、参数X：是否开启X坐标的随机范围，默认不开启
        3、参数Y：是否开启Y坐标的随机范围，默认不开启
        4、随机坐标轴必须开启一个但不能同时开启，否则抛出异常
        PS:请保证当次随机的坐标范围值的有效性
        """
        if not X and not Y:
            raise NameError('X、Y两个参数必须有一个为True，以决定随机轴。')
        elif X and Y:
            raise NameError('只能选择一个坐标轴作为随机轴。')
        elif X:
            x = random.randint(random_x1, random_x2)
            return self.driver.tap([(x, random_y1), (x + 5, random_y2)], 100)
        elif Y:
            y = random.randint(random_y1, random_y2)
            return self.driver.tap([(random_x1, y), (random_x2, y + 5)], 100)
        else:
            raise NameError('输入异常！')

    def select_assign_warehouse(self, assign_warehouse):
        """选择指定仓库"""
        uiautomator_element = [
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}").instance(0);'.format(assign_warehouse)
        ]
        self.driver.find_element(*uiautomator_element).click()

