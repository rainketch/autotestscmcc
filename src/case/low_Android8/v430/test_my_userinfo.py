"""
    我的-手机号-用户信息
"""
# -*- coding: utf-8  -*-
__author__ = 'snake'


import unittest, time
from src.case.v350.test_basecase import TestCaseBase


class TestCaseUserInfo(TestCaseBase):

    # 重写父类setUp方法，用来执行_click_my_button()方法，没有必要尽量不要重新
    def setUp(self):
        # 点击我的按钮
        super().setUp()
        self._click_my_button()

    def test_user_name(self):
        """
        检查用户姓名: 姓名不为空且包含'*'号
        :return:
        """
        user_name = self.find_element("id", "com.sunrise.scmbhc:id/user_name", timeout=30).text
        self.assertIn("*", user_name, "判断姓名是否存在*")

    def test_user_state(self):
        """
        检查用户号码状态，检查是否存在'号码状态：正常'关键字
        :return:
        """
        user_state = self.find_element("id", "com.sunrise.scmbhc:id/user_state", timeout=30).text
        self.assertIn("号码状态：正常", user_state, "判断姓名是否存在号码状态关键字")

    def test_user_phone(self):
        """
        检查用户号码，不为空
        :return:
        """
        user_info_phone = self.find_element("id", "com.sunrise.scmbhc:id/user_phone", timeout=30).text
        self.assertIsNotNone(user_info_phone, "用户号码不为空")

    def test_user_area(self):
        """
        检查用户归属地：当前号卡归属地是成都：'号码归属：成都'
        :return:
        """
        user_phone_area = self.find_element("id", "com.sunrise.scmbhc:id/user_area", timeout=30).text
        self.assertIn(user_phone_area, "号码归属：成都", "检查用户号码归属地为成都")

    def test_user_star(self):
        """
        检查用户星级：不为空/如果是无星级，则是不显示星级
        :return:
        """
        user_star_level = self.find_element("xpath", "//android.widget.TextView[@text='无星级']", timeout=30)
        if user_star_level is None:
            user_start = self.find_element("id", "com.sunrise.scmbhc:id/id_my_mobile_txt_show", timeout=30).text
            self.assertIsNotNone(user_start, "检查用户星级不为空, text={}".format(user_start))

    def test_user_star_score(self):
        """
        检查用户星级分：不为空
        :return:
        """
        star_xpath = "//android.widget.TextView[@text='星级分：']/following-sibling::android.widget.TextView"
        user_start = self.find_element("xpath", star_xpath, timeout=30).text
        self.assertIsNotNone(user_start,"检查用户星级分不为空")

    def test_user_star_expiry_date(self):
        """
        检查用户星级有效期：不为空
        :return:
        """
        star_xpath = "//android.widget.TextView[@text='星级有效期：']/following-sibling::android.widget.TextView"
        user_star_expiry_date = self.find_element("xpath", star_xpath, timeout=30).text
        self.assertIsNotNone(user_star_expiry_date, "检查用户星级有效期不为空")

    def test_user_certification(self):
        """
        检查用户实名认证：不为空
        :return:
        """
        certifi_xpath = "//android.widget.TextView[@text='实名认证：']/following-sibling::android.widget.TextView"
        user_certification = self.find_element("xpath", certifi_xpath, timeout=30).text
        self.assertIsNotNone(user_certification, "检查用户实名认证不为空")

    def test_user_net_years(self):
        """
        检查用户网龄：不为空
        :return:
        """
        year_xpath = "//android.widget.TextView[@text='网龄：']/following-sibling::android.widget.TextView"
        user_net_years = self.find_element("xpath", year_xpath, timeout=30).text
        self.assertIsNotNone(user_net_years, "检查用户网龄不为空")

    def test_user_use_years(self):
        """
        检查入网时间：不为空
        :return:
        """
        user_year_xpath = "//android.widget.TextView[@text='入网时间：']/following-sibling::android.widget.TextView"
        user_use_net_years = self.find_element("xpath", user_year_xpath, timeout=30).text
        self.assertIsNotNone(user_use_net_years, "检查用户入网时间不为空")

    def _click_my_button(self):
        """
        点击我的按钮
        :return:
        """
        # 点击我的
        my_btn = "//android.widget.TextView[@text='我的']"
        menu_layout = "com.sunrise.scmbhc:id/menubottomlayout"
        menu_layout_obj = self.find_element("id", menu_layout)
        menu_layout_obj.find_element("xpath", my_btn).click()

        # 进入个人信息页面
        self.find_element("id", "com.sunrise.scmbhc:id/id_my_mobile_number").click()