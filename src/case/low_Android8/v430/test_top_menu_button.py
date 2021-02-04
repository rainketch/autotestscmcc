
# -*- coding: utf-8  -*-
__author__ = 'snake'

from src.case.low_Android8.v430.test_basecase import TestCaseBase
from src.util.util_logger import logger
from src.case.low_Android8.bll.v430.index import back_to_index
import time
import unittest

@unittest.skip("")
class TestHomePageTop1(TestCaseBase):
    def into_top_messagecenter(self):
        '''
        进入顶部消息中心页面
        :return:
        '''
        messagecenter = self.find_element("xpath",
                                                  '//*[@resource-id="com.sunrise.scmbhc:id/layout_massage"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]')

        if messagecenter is None:
            self.assertEqual(1, 2, "首页未定位到消息中心按钮，请检查！！")
        messagecenter.click()
        time.sleep(5)

    def test_top_onlinecustomservice(self):
        '''
        检查能否进入顶部在线客服页面
        :return:
        '''
        try:
            online_custome_servie = self.find_element("xpath",'//*[@resource-id="com.sunrise.scmbhc:id/layout_massage"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')

            if online_custome_servie is None:
                self.assertEqual(1, 2, "首页顶部未定位到在线客服按钮，请检查！！")
            online_custome_servie.click()
            time.sleep(5)

            exist_text = self.find_element("xpath", '//*[@content-desc="剩余通用流量"]')
            if exist_text is None:
                back_to_index(self.driver)
                self.assertEqual(1, 2, "未定位带在线客服页面内容-->{},请检查是否进入该页面".format(exist_text))
            else:
                logger.info("成功定位到页面中剩余通用流量")
                back_to_index(self.driver)
        except Exception as ret:
            self.assertEqual(1,2, "首页未找到在线客服按钮")


    def test_top_intomessagepage(self):
        '''
        检查能否进入消息中心页面
        :return:
        '''
        self.into_top_messagecenter()


        mail_139 = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/name_message_center_detail_push_top_139"]')
        service_center = self.find_element("xpath",
                                           '//*[@resource-id="com.sunrise.scmbhc:id/name_message_center_detail_push_top_server_center"]')

        if mail_139 is None or service_center is None:
            self.assertEqual(1, 2, "消息中心页面未定位到139邮箱或者服务中心xpath，请检查是否进入消息中心页面！！")
        logger.info("消息中心页面成功定位到139邮箱或者服务中心xpath")


    def test_top_checkmessagecenter_content(self):
        '''
        检查消息中心内容
        :return:
        '''

        mail_139 = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/name_message_center_detail_push_top_139"]')
        if mail_139 is None:
            self.assertFalse(True, "未定位到139邮箱，请检查是否进入小心中心页面！！")

        # 消息中心内容存在的情况
        content_id = self.find_element("id", "com.sunrise.scmbhc:id/ll_msg_detail_title")
        if content_id is None:
            logger.info("未找到消息中心内容")
            self.assertTrue(True, "消息中心内容")

        # 消息中心内容为空
        empty_message = self.find_element("id", "com.sunrise.scmbhc:id/msg_footview_tv").text
        if empty_message is None:
            self.assertTrue(True, "未定位到相关的为空的元素，请检查！！")
        logger.info("消息中心内容为空时定位到的元素是{}".format(empty_message))



    def test_top_mesaagecenter_empty(self):
        '''
        检查清空按钮是否存在
        :return:
        '''
        try:
            empty_content = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/ll1"]')
            if empty_content is None:
                self.assertFalse(True, "未定位到清空按钮")
        except:
            logger.war("定位清空为本是出现异常，请检查！！")
            self.assertFalse(True, "定位文本时出现异常")

    def test_top_checkaddbutoon(self):
        '''
        检查首页顶部加号是否存在
        :return:
        '''
        back_to_index(self.driver)

        topbutton = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/layout_massage"]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]')
        if topbutton is None:
            self.assertFalse(True, "首页顶部按钮不存在，请检查！！")
        else:
            logger.info("首页顶部成功定位到加号按钮")



    def test_top_checkscmccpj(self):
        '''
        检查是否成功进入掌厅评价页面
        :return:
        '''
        try:
            # 定位首页顶部加号按钮
            topaddbutton = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/layout_massage"]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]')

            if topaddbutton is None:
                self.assertFalse(True, "首页顶部加号按钮不存在，请检查！！")
            else:
                # 点击顶部加号按钮
                topaddbutton.click()

                # 定位掌厅评价按钮xpath
                scmcpj = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_list"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')
                if scmcpj is None:
                    self.assertFalse(True, "未定位到掌厅评价按钮，请检查！！")
                else:
                    # 点击掌厅评价按钮
                    scmcpj.click()
                    time.sleep(3)

                    # 定位掌厅评价页面的提交按钮的xpath
                    commit_button = self.find_element("xpath", '//*[@content-desc="提交"]')

                    if commit_button is None:
                        self.driver.back()
                        self.assertEqual(1,2, "未定位到服务评价页面中的提交按钮，请检查！！")
                    else:
                        logger.info("成功定位到掌厅评价页面的xpath")
                        self.driver.back()
        except Exception as ret:
            logger.war("检查掌厅评价页面时出现异常-->{}".format(ret))

@unittest.skip("")
class TestSyisandmayi(TestCaseBase):
    def test_top_checkintosyis(self):
        '''
        检查能否成功进入扫一扫页面
        :return:
        '''
        # 定位掌厅首页加号按钮xpath
        topbutton = self.find_element("xpath",
                                      '//*[@resource-id="com.sunrise.scmbhc:id/layout_massage"]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]')

        if topbutton is None:
            self.assertFalse(True, "首页顶部加号按钮不存在，请检查！！")
        else:
            # 点击掌厅首页的加号按钮
            topbutton.click()
            time.sleep(2)

            # 定位扫一扫按钮xpath
            syis = self.find_element("xpath",'//*[@resource-id="com.sunrise.scmbhc:id/title_list"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]')
            if syis is None:
                self.assertEqual(1,2, "未定位到扫一扫，请检查!!")
            else:
                # 点击扫一扫按钮
                syis.click()
                time.sleep(2)

                # 定位扫一扫页面中的元素
                syis_text = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/ll1"]')
                if syis_text is None:
                    self.driver.back()
                    self.assertEqual(1,2,"未定位到扫一扫页面元素")
                else:
                    self.driver.back()
                    logger.info("成功定位到扫一扫页面中的元素")

    def test_top_satisfiedforyou(self):
        '''
        检查能否进入满意为您页面
        :return:
        '''

        # 定位掌厅首页加号按钮xpath
        topaddbutton = self.find_element("xpath",
                                      '//*[@resource-id="com.sunrise.scmbhc:id/layout_massage"]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]')

        if topaddbutton is None:
            self.assertFalse(True, "首页顶部加号按钮不存在，请检查！！")
        else:
            # 点击加号按钮
            topaddbutton.click()
            time.sleep(1)

            # 定位加号菜单下的满意为您按钮xpath
            satisfied_text = self.find_element("xpath",'//*[@resource-id="com.sunrise.scmbhc:id/title_list"]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]')
            if satisfied_text is None:
                self.assertEqual(1,2,"未定位到满意为您，请检查！！")
            else:
                # 点击满意为您按钮
                satisfied_text.click()
                time.sleep(3)
                # 定位满意为您页面中的客户满意度调研问卷图片的xpath
                satisfied_image = self.find_element("xpath",'//*[@content-desc="banner"]')
                if satisfied_image is None:
                    self.assertEqual(1,2,"满意为您页面中未定位到问卷图片的xpath，请检查！！")
                else:
                    logger.info("成功进入满意为您页面，且成功定位到问卷图片的xpath")










