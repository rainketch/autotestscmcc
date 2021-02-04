
# -*- coding: utf-8  -*-
__author__ = 'snake'


import unittest
from src.case.low_Android8.v430.test_basecase import TestCaseBase
from src.util.util_logger import logger
import time



@unittest.skip("")
class TestTopSearch(TestCaseBase):
    '''
    掌厅--首页--顶部搜索
    '''

    def into_search_page(self):
        '''
        进入搜索页面
        :return:
        '''
        try:
            # 点击首页顶部的搜索按钮
            self.find_element("id", "com.sunrise.scmbhc:id/main_search_search").click()
            time.sleep(2)
            logger.info("成功进入搜索页面！！")
        except Exception as ret:
            logger.war("未找到顶部搜索按钮框，请检查")
            return False

    def resolve_keyborad(self):
        '''
        收起输入法键盘
        :return:
        '''
        self.driver.hide_keyboard()

    def test_homepage_into_topsearch(self):
        '''
        检查能否进入顶部搜索页面
        :return:
        '''
        self.into_search_page()

        # 检查页面中的元素
        search_element = self.find_element("xpath", "//android.widget.TextView[@text='办流量包']")
        text_one = search_element.text
        self.assertEqual("办流量包", text_one, "检查热搜榜1号位文本是否存在！！")

    def test_topsearch_tophotsearch(self):
        '''
        检查热搜榜是否存在
        :return:
        '''
        # 检查热搜榜文字是否存在
        hot_top_search = self.find_element("xpath", "//android.widget.TextView[@text='热搜榜']")
        text1 = hot_top_search.text
        self.assertEqual(text1, "热搜榜", "检查热搜榜元素是否一致")

    def test_top_search_viocesearch(self):
        '''
        检查是否可以正常进入语音搜索页面
        :return:
        '''
        try:
            self.resolve_keyborad()
            time.sleep(2)

            voice_search_button = self.find_element("id", "com.sunrise.scmbhc:id/btn_search_open_voice")
            voice_search_button.click()
        except Exception as ret:
            logger.war("进入搜索页面异常！！")

        voice_search_text = self.find_element("id", "com.sunrise.scmbhc:id/tv_search_voice_tip_2")
        voice_search_text1 = voice_search_text.text
        self.assertIsNotNone(voice_search_text1, "文本不为空就行！！")
        self.find_element("id", "com.sunrise.scmbhc:id/btn_search_voice_close").click()

    def test_top_search_defualtword(self):
        '''
        检查搜索的默认词条
        :return:
        '''
        edit_search = self.find_element("id", "com.sunrise.scmbhc:id/edit_seacher")
        search_defaultword = edit_search.text
        self.assertEqual("服务管家", search_defaultword, "检查默认词条是否一致")

    def test_top_search_inputword(self):
        '''
        检查输入搜索内容能否正常
        :return:
        '''
        try:
            obj = self.driver.find_element_by_id("com.sunrise.scmbhc:id/edit_seacher")
            obj.send_keys(u"5G")
            time.sleep(2)

            search_result = self.find_element("xpath", '//*[@text="5G智享卡"]')
            if search_result is None:
                self.assertEqual(1,2,"搜索页面未找到5G智享卡相关的信息，请检查！！")

        except Exception as ret:
            logger.war("输入内容进行搜索时出现异常！！ 请检查case")
            self.assertEqual(1,2,"搜索时出现异常，请检查！！")























