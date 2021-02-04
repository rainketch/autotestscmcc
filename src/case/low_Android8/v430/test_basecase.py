# coding=utf-8
import unittest

from selenium.webdriver.support.wait import WebDriverWait
from src.util.util_appium_driver import get_driver
from src.util.util_logger import logger
from src.case.low_Android8.bll.v430.index import _close_msg_alert
import time
from utx import *


class TestCaseBase(unittest.TestCase):

    def __init__(self, methodName="runTest", param=None):
        super(TestCaseBase, self).__init__(methodName)
        self.__param = param

    @classmethod
    def setUpClass(cls):
        logger.info("*"*100)
        cls.driver = get_driver()
        logger.info("初始化-->{}类".format(cls.__class__))
        time.sleep(10)
        _close_msg_alert(cls.driver)
        # logger.info("开始执行返回首页")
        # back_to_index(cls.driver)
        # logger.info("返回首页成功！！")
        #
        # logger.info("*" * 100)
        # if one_key_login(cls.driver) is False:
        #     logger.info("判断掌厅登录状态失败，app启动异常!")
        #     raise Exception("判断掌厅登录状态失败，app启动异常!!")




    @classmethod
    def tearDownClass(cls):
        logger.info("*"*100)
        cls.driver.quit()



    def setUp(self):
        logger.info("*"*100)
        logger.info("开始执行用例->{}.{}".format(self.__class__, self._testMethodName))
        logger.info("*" * 100)


        # self.driver = get_driver()
        # # logger.info("初始化-->{}类".format(self.__class__))
        # logger.info("开始执行返回首页")
        # back_to_index(self.driver)
        # logger.info("返回首页成功！！")
        #
        # logger.info("*" * 100)
        # if one_key_login(self.driver) is False:
        #     logger.info("判断掌厅登录状态失败，app启动异常!")
        #     raise Exception("判断掌厅登录状态失败，app启动异常!!")
        # time.sleep(5)



    def tearDown(self):
        self.driver._switch_to.context(self.driver.contexts[0])
        logger.info("结束执行用例->{}.{}".format(self.__class__, self._testMethodName))
        # self.driver.close_app()


    def find_elements(self, by="id", value="", timeout=10):
        """
        在运行次数内等待并获取结果, 默认10秒超时
        :param driver:
        :param by:
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
        :param value:
        :param timeout:
        :return:
        """
        try:
            logger.info("开始执行find_elements方法")
            elements = WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(by=by, value=value))
            logger.info("成功定位元素集,by->{}, value={}, 返回元素->{}".format(by, value, elements))
            return elements
        except:
            logger.war("定位元素失败,by->{}, value={}, 返回None".format(by, value))
            logger.info("当前activity->{}".format(self.driver.current_activity))

        return None
    #
    def find_element(self, by="id", value="", timeout=10):
        """
        在运行次数内等待并获取结果, 默认10秒超时
        :param driver:
        :param by:
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
        :param value:
        :param timeout:
        :return:
        """
        logger.info("开始执行find_element方法")
        try:
            element = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(by=by, value=value))
            logger.info("成功定位元素,by->{}, value={}, 返回元素->{}".format(by, value, element))
            return element
        except:
            logger.war("定位元素失败,by->{}, value={}, 返回None".format(by, value))
            logger.info("当前activity->{}".format(self.driver.current_activity))

        return None

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        #     print(suite)
        # print(suite)
        return suite