# 测试首页内容

# -*- coding: utf-8  -*-
__author__ = 'snake'

from src.case.low_Android8.v430.test_basecase import TestCaseBase
from src.util.util_adb import exec_cmd
from src.util.util_logger import logger
import time
from src.case.low_Android8.bll.v430.index import _close_msg_alert, back_to_index
import unittest


@unittest.skip("")
class TestNoneScreen(TestCaseBase):
    '''
    测试首页进入负一屏和退出负一屏
    '''

    def test_index_negative_one_screen(self):
        '''
        检查能否进入负一屏页面
        :return:
        '''
        try:
            logger.info("执行滑动进入负一屏命令！！")
            # 滑动屏幕进入负一屏
            exec_cmd("adb shell input touchscreen swipe 0 100 600 100")
            time.sleep(3)
        except Exception as ret:
            logger.info("滑动进入负一屏时出现异常-->{}".format(ret))

        right_statusbar = self.find_element("xpath",
                                            '//*[@resource-id="com.sunrise.scmbhc:id/sildingFinishLayout"]/android.widget.ImageView[1]')
        set_ring = self.find_element("xpath",
                                     '//*[@content-desc="视频彩铃"]/android.view.View[5]')
        if right_statusbar is None or set_ring is None:
            self.assertTrue(False, "未定位到负一屏-->视频彩铃页面元素，请检查！！")

    def test_index_exit_negative_one_screen(self):
        '''
        检查能否退出负一屏
        :return:
        '''
        # 退出负一屏
        try:
            logger.info("执行滑动退出负一屏命令！！")
            exec_cmd("adb shell input touchscreen swipe 800 350 0 350")
        except Exception as ret:
            logger.info("滑动进退出负一屏时出现异常-->{}".format(ret))

        shouye_text = self.find_element("xpath", '//*[@text="首页"]')
        if shouye_text is None:
            self.assertEqual(1, 2, "未能退出到首页，请检查！！")

@unittest.skip("")
class TestIndexBanner(TestCaseBase):
    '''
    测试首页banner位置，进入和退出功能
    '''

    def test_index_check_pointId1(self):
        '''
        检查pointid1号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[1]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid1号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid1号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid1号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId2(self):
        '''
        检查pointid2号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[2]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid2号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid2号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid2号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId3(self):
        '''
        检查pointid3号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[3]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid3号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid3号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid3号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId4(self):
        '''
        检查pointid4号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[4]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid4号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid4号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid4号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId5(self):
        '''
        检查pointid5号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[5]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid5号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid5号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid5号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId6(self):
        '''
        检查pointid6号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[6]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid6号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid6号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid6号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId7(self):
        '''
        检查pointid7号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[6]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid7号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid7号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid7号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)

    def test_index_check_pointId8(self):
        '''
        检查pointid8号位置
        :return:
        '''
        try:
            banner1_text = self.find_element("xpath",
                                             '//*[@resource-id="com.sunrise.scmbhc:id/xbanner_pointId"]/android.widget.ImageView[6]')
            if banner1_text is None:
                self.assertTrue(False, "未找到pointid8号位置，请检查！！")
            banner1_text.click()
            time.sleep(3)
            title_rlayout = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
            if title_rlayout is not None:
                logger.info("成功进入页面!!")
                self.driver.back()
            else:
                logger.war("定位元素失败，未找到-->xpath-->{}".format(title_rlayout))
                back_to_index(self.driver)

            index_text = self.find_element("xpath", '//*[@text="首页"]')
            time.sleep(2)
            if index_text is None:
                self.assertEqual(1, 2, '未能成功返回首页，请检查！！')
        except Exception as ret:
            logger.war("poinid8号位置不存在，或者掌厅出现异常，请检查！！")
            self.assertEqual(1, 2, "掌厅出现异常，未找到pointid8号位置，点击时出现异常")
            logger.info("异常情况-->{}".format(ret))
            back_to_index(self.driver)


class TestOnkeyQuery(TestCaseBase):
    '''
    测试一键查询页面
    '''

    def into_onekeyquery(self):
        '''
        进入一键查询
        :return:
        '''
        try:
            onekeyquery = self.find_element("xpath",
                                            '//*[@resource-id="com.sunrise.scmbhc:id/gridview_main_bis"]/android.widget.LinearLayout[1]')
            if onekeyquery is None:
                self.assertFalse(True, "首页未检查到一键查询入口，请检查！！")
            else:
                onekeyquery.click()
                time.sleep(6)
                _close_msg_alert(self.driver)
        except Exception as ret:
            logger.info("首页未定位到一键查询入口，请检查！！异常情况-->{}".format(ret))

    def test_index_check_onekeyquery(self):
        '''
        检查一键查询入口是否存在
        :return:
        '''

        # 检查一键查询入口
        try:
            onekeyquery = self.find_element("xpath",
                                            '//*[@resource-id="com.sunrise.scmbhc:id/gridview_main_bis"]/android.widget.LinearLayout[1]')
            if onekeyquery is None:
                self.assertEqual(1, 2, "首页未检查到一键查询入口，请检查！！")
        except Exception as ret:
            logger.war("首页未定位到一键查询入口，请检查！！")
            logger.info("异常情况-->{}".format(ret))

    def test_onekeyquery_checkstar(self):
        '''
        检查当前用户的星级是否存在
        :return:
        '''
        # 返回首页，然后进入一键查询页面
        self.into_onekeyquery()
        # 定位星级xpath
        star_xpath = self.find_element("xpath", '//*[@resource-id="starLevel"]')
        if star_xpath is None:
            self.assertEqual(1, 2, "星级不存在，请检查！！")
        else:
            # 获取星级的等级
            user_star = star_xpath.get_attribute("name")
            # 不为空
            if user_star is None or user_star == "":
                self.assertEqual(1, 2, "用户的星级为空！！")
            else:
                logger.info("获取到当前用户的星级为{}".format(user_star))

    def test_onekeyquery_checkjifen(self):
        '''
        检查积分是否存在
        :return:
        '''

        # 定位积分是否存在
        jifen_xpath = self.find_element("xpath", '//*[@resource-id="jifen"]')

        if not jifen_xpath:
            self.assertEqual(1, 2, "一键查询页面积分不存在，请检查")

    def test_onkeyquery_check_dyye(self):
        '''
        检查当月余额数据，不为空/0/--
        '''
        xpath01 = self.find_element("xpath", '//*[@resource-id="yue"]').get_attribute("name")
        logger.info("xpath is{}".format(xpath01))
        if xpath01 is None:
            logger.info("当月余额数据为空，请检查！！")

        try:
            # 提取出其中的数据
            cut_data = float(xpath01.replace("元 当月余额", ""))
            logger.info("当前余额为-->{}".format(cut_data))
        except Exception as ret:
            logger.war("当月余额切割时出现异常，异常金额是{}".format(xpath01))
            self.assertEqual(1, 2, "当月余额切割异常的金额是{}".format(xpath01))

        # 当月余额为空/0时
        if cut_data is None or cut_data == 0:
            logger.info("切割后的当前余额是{}".format(cut_data))
            self.assertEqual(1, 2, "当月余额为空或者0，请检查！！")

        # 当月余额为--时
        if isinstance(cut_data, float):
            self.assertEqual(1, 2, "切割后的当月余额数据出现异常，异常金额为-->{}".format(cut_data))

    def test_onekeyquery_checkchongzhi(self):
        '''
        检查充值是否存在
        :return:
        '''
        chongzhi_xpath = self.find_element("xpath", '//*[@resource-id="yue"]/android.view.View[2]')
        if chongzhi_xpath is None:
            self.assertTrue(False, "充值入口不存在请检查")

    def test_onekeyquery_check_righttop_kf(self):
        '''
        检查右上角在线客服按钮是否存在和是否成功进入
        :return:
        '''
        try:
            # 查找一键查询页面顶部右上角在线客服按钮
            right_top_xpath = self.find_element("xpath",
                                                '//*[@resource-id="com.sunrise.scmbhc:id/ll1"]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]')
            if right_top_xpath is None:
                self.assertEqual(1, 2, "未找到右上角在线客服的xpath，请检查！！")

            # 进入在线客服页面
            right_top_xpath.click()
            time.sleep(2)

            # 查找二次确认框中在线客服xpath
            online_kf_xpath = self.find_element("xpath", '//*[@text="在线客服"]')
            if online_kf_xpath is None:
                self.driver.back()
                self.assertTrue(False, "二次确认框中未找到在线客服xpath，请检查")

            # 点击进入在线客服页面
            online_kf_xpath.click()
            time.sleep(6)

            # 在线客服页面寻找查询账单xpath
            emoji_xpath = self.find_element("xpath",
                                            '//*[@resource-id="mescroll"]/android.view.View[7]')
            if emoji_xpath is None:
                self.driver.back()
                self.assertEqual(1, 2, "在线客服页面未找到查询账单xpath")
            else:
                logger.info("一键查询页面成功定位到在线客服xpath为-->{}".format(emoji_xpath))
                self.driver.back()
        except Exception as ret:
            logger.war("检查一键查询页面右上角在线客服是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查一键查询在线客服时出现错误，可能原因是未定位到十宫格一键查询xpath或者未定位到一键查询页面右上角在线客服xpath")

    def test_onekeyquery_check_righttop_comments(self):
        '''
        检查右上角评价与意见是否存在
        :return:
        '''
        try:
            # 查找一键查询页面右上角意见与评价按钮
            comments_xpath = self.find_element("xpath",
                                               '//*[@resource-id="com.sunrise.scmbhc:id/ll1"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]')
            if comments_xpath is None:
                self.assertEqual(1, 2, "一键查询页面右上角未找到意见与评价按钮，请检查！！")

            # 进入一键与评价页面
            comments_xpath.click()
            time.sleep(2)

            # 查找评价与意见页面的提交按钮的xpath
            commit_btn_xpath = self.find_element("xpath", '//*[@content-desc="提交"]')
            close_page_xpath = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_btn_close"]')
            if commit_btn_xpath is None:
                close_page_xpath.click()
                self.assertEqual(1, 2, "意见与评价页面未找到提交按钮，请检查！！")
            else:
                logger.info("成功定位到意见与评价页面的提交按钮的xpath，-->{}".format(commit_btn_xpath))
                close_page_xpath.click()
        except Exception as ret:
            logger.war("检查一键查询页面右上角意见与评价是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查一键查询意见与评价时出现错误，可能原因是未定位到十宫格一键查询xpath或者未定位到一键查询页面右上角意见与评价xpath")

    def test_onekeyquery_checkpayquery(self):
        '''
        检查查账单按钮是否存在
        :return:
        '''
        payquery = self.find_element("xpath", '//*[@resource-id="xiaofei"]/android.view.View[2]')
        if payquery is None:
            self.assertTrue(False, "账单查询入口不存在请检查")

    def test_onekeyquery_checkzhangmenrecommend(self):
        '''
        检查掌门推荐是否存在
        :return:
        '''
        # 定位语音/短彩信title xpath
        vioceSms_xpath = self.find_element("xpath", '//*[@content-desc="语音/短彩信"]')
        if vioceSms_xpath is None:
            self.assertEqual(1, 2, "一键查询页面未定位到语音短彩信title")
        # 点击语音短彩信title
        vioceSms_xpath.click()
        time.sleep(1)

        # 寻找可能感兴趣位置的广告位
        recommend_xpath = self.find_element("xpath",
                                            '//*[@content-desc="一键查询"]/android.widget.ListView[3]/android.view.View[2]')
        if recommend_xpath is None:
            self.assertEqual(1, 2, "未找到一键查询页面掌门推荐位xpath")
        else:
            logger.info("一键查询页面成功定位到掌门推荐xpath-->{}".format(recommend_xpath))

    def test_onekeyquery_check_meals_avaliable(self):
        '''
        检查套餐可用是否存在数据
        :return:
        '''
        # 定位一键查询页面流量title xpath
        title_xpath = self.find_element("xpath", '//*[@content-desc="流量"]')
        if title_xpath is None:
            self.assertEqual(1, 2, "一键查询页面未定位到流量xpath")
        # 点击流量title xpath
        title_xpath.click()
        time.sleep(1)

        # 定位套餐可用处的数据的xpath
        data_xpath = self.find_element("xpath", '//*[@resource-id="taocan_keyong"]')

        if data_xpath is None:
            self.assertEqual(1, 2, "套餐可用处未定位到套餐可用数据的xpath，请检查！！")
        else:
            # 获取text属性
            text_data = data_xpath.get_attribute("name")

            # 当月数据异常时
            if text_data is None or text_data == "" or text_data == 0:
                self.assertEqual(1, 2, "当月套餐可用数据异常，请检查！")

            try:
                # 对数据进行处理
                data = float(text_data.replace("GB", ""))
            except:
                logger.war("处理流量数据时出现异常，异常金额为{}".format(text_data))
                self.assertEqual(1, 2, "当前流量数据出现异常，异常金额为{}".format(text_data))

            logger.info("当前套餐可用处理后数据为-->{}".format(data))

            # 判断流量数据类型，防止出现“--”类型
            if not isinstance(data, float):
                self.assertEqual(1, 2, "当前流量数据出现异常，异常金额为{}".format(text_data))

    def test_onekeyquery_check_voiceandSMS(self):
        '''
        检查语音、短彩信是否有数据
        :return:
        '''
        # 定位语音/短彩信title xpath
        vioceSms_xpath = self.find_element("xpath", '//*[@content-desc="语音/短彩信"]')
        if vioceSms_xpath is None:
            self.assertEqual(1, 2, "一键查询页面未定位到语音短彩信title")
        # 点击语音短彩信title
        vioceSms_xpath.click()
        time.sleep(1)

        # 查找语音短彩信语音可用数据xpath
        vs_data_xpath = self.find_element("xpath", '//*[@resource-id="yuyin2"]')
        if vs_data_xpath is None:
            self.assertEqual(1, 2, "语音短彩信处未找到语音可用数据的xpath")
        else:
            # 获取语音短彩信数据text
            vx_data = vs_data_xpath.get_attribute("name")

            try:
                # 对数据进行切割/将分钟数去掉
                vx_text = float(vx_data.replace("分钟", ""))
            except:
                logger.war("处理语音数据时出现异常，异常金额为{}".format(vx_data))
                self.assertEqual(1, 2, "当前语音数据出现异常，异常金额为{}".format(vx_data))
            logger.info("处理后数据为-->{}".format(vx_text))

            # 当月数据异常时
            if vx_text is None or vx_text == "" or vx_text == 0:
                logger.war("处理语音数据时出现异常，异常金额为{}".format(vx_data))
                self.assertEqual(1, 2, "语音短彩信数据出现异常，请检查！！")

            # 检查处理后数据类型为”--“的
            if not isinstance(vx_text, float):
                logger.war("处理语音数据时出现异常，异常金额为{}".format(vx_data))
                self.assertEqual(1, 2, "当前语音数据出现异常，异常金额为{}".format(vx_data))

    def test_onekeyquery_check_advert(self):
        '''
        检查该广告位是否存在
        :return:
        '''
        # 查找一键查询页面广告位xpath
        adver_xpath = self.find_element("xpath", '//*[@content-desc="一键查询"]/android.widget.ListView[3]/android.view.View[1]')
        if adver_xpath is None:
            self.assertEqual(1, 2, "一键查询页面未定位到广告位xpath，请检查！！")

    def test_onekeyquery_check_5Gzhixiangka(self):
        '''
        检查5G流量包是否存在
        :return:
        '''
        exec_cmd("adb shell input swipe 500 1500 500 700")
        # 查找流量包位置xpath元素
        g_zhixiang_xpath = self.find_element("xpath",
                                             '//*[@content-desc="一键查询"]/android.widget.ListView[3]/android.view.View[1]')
        if g_zhixiang_xpath is None:
            self.assertEqual(1, 2, "未定位到5G流量包xpath，请检查！！")

            # # 进入5G智享卡页面
            # g_zhixiang_xpath.click()
            # time.sleep(5)
            #
            # # 查找页面中元素
            # menu_xpath = self.find_element("xpath", '//*[@resource-id="menu"]')
            # close_btn = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_btn_close"]')
            # if menu_xpath is None:
            #     self.assertEqual(1, 2, "5G智享卡页面未找到相应元素的xpath")
            #     close_btn.click()
            # else:
            #     logger.info("成功定位到页面中元素的xpath为{}".format(menu_xpath))
            #     close_btn.click()
        # except Exception as ret:
        #     logger.war("检查一键查询5G智享卡是否存在时出现异常，异常原因-->{}".format(ret))
        #     self.assertEqual(1, 2, "检查一键查询5G智享卡时出现错误，可能原因是未定位到十宫格一键查询xpath或者未定位到一键查询页面5G智享卡xpath")

    def test_onekeyquery_check_shenma(self):
        '''
        检查神马出行广告位是否存在
        :return:
        '''
        shenma_xpath = self.find_element("xpath",
                                         '//*[@content-desc="一键查询"]/android.widget.ListView[3]/android.view.View[2]')
        if shenma_xpath is None:
            self.assertEqual(1, 2, "一键查询页面未找到神马出行广告位xpath，请检查")

    def test_onekeyquery_check_yidingyewu(self):
        '''
        检查已订业务查询入口是否存在
        :return:
        '''
        try:
            # 滑动页面到更多查询位置
            exec_cmd("adb shell input swipe 500 1500 500 700")

            # 定位已订业务查询xpath
            #yidingyewu = self.find_element("xpath",
                                           # '//*[@resource-id="com.sunrise.scmbhc:id/self_webview"]/android.widget.RelativeLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.ListView[3]/android.view.View[1]')
            yidingyewu = self.find_element("xpath", '//*[@content-desc="已订业务查询"]')

            if yidingyewu is None:
                self.assertEqual("一键查询页面未找到已定业务xpath，请检查！！")

            # 获取已订业务查询文字
            page_text = yidingyewu.get_attribute("name")
            if page_text is None:
                self.assertEqual(1, 2, "未获取到已订业务查询文字")
            else:
                logger.info("已经获取到的已订业务的文本是-->{}".format(page_text))
                self.assertEqual(page_text, "已订业务查询", "检查已订业务查询文字是否一致")
        except:
            logger.war("页面可能未滑动到已订业务查询处，请检查")
            raise Exception

    def test_onekeyquery_check_yicanjian(self):
        '''
        检查已参加活动入口是否存在
        :return:
        '''
        # 定位一参加活动的xpath
        yicanjia = self.find_element("xpath",
                                     '//*[@content-desc="已参加活动"]')
        if yicanjia is None:
            self.assertEqual(1, 2, "一键查询页面未找到已参加入口，请检查")

        # 获取已参加文字
        page_text = yicanjia.get_attribute("name")
        if page_text is None:
            self.assertEqual(1, 2, "未获取到已参加活动文字")
        else:
            logger.info("已经获取到的已订业务的文本是-->{}".format(page_text))
            self.assertEqual(page_text, "已参加活动", "检查已参加活动文字是否一致")

    def test_onekeyquery_check_jiluquery(self):
        '''
        检查充值记录查询入口是否存在
        :return:
        '''
        # 定位充值记录查询的xpath
        jiluquery = self.find_element("xpath",
                                      '//*[@content-desc="充值记录查询"]')
        if jiluquery is None:
            self.assertEqual(1, 2, "一键查询页面未找到记录查询入口，请检查")

        # 获取充值记录查询文字
        page_text = jiluquery.get_attribute("name")
        if page_text is None:
            self.assertEqual(1, 2, "未获取到记录查询文字")
        else:
            logger.info("已经获取到的已订业务的文本是-->{}".format(page_text))
            self.assertEqual(page_text, "充值记录查询", "检查记录查询文字是否一致")

    def test_onkeyquery_check_dianzifapiao(self):
        '''
        检查电子发票入口是否存在
        :return:
        '''
        dianzifapiao = self.find_element("xpath",
                                         '//*[@content-desc="电子发票 可开12个月"]')
        if dianzifapiao is None:
            self.assertEqual(1, 2, "一键查询页面未找到电子发票入口，请检查!!")

        # 获取电子发票文字
        page_text = dianzifapiao.get_attribute("name")
        if page_text is None:
            self.assertEqual(1, 2, "未获取到电子发票文字")
        else:
            logger.info("已经获取到的已订业务的文本是-->{}".format(page_text))
            self.assertEqual(page_text, "电子发票 可开12个月", "检查电子发票文字是否一致")

    def test_onekeyquery_check_payquery(self):
        '''
        检查账单查询页面当月消费是否有数据
        :return:
        '''
        # 查找一键查询页面更多查询处的账单查询按钮xpath
        payquery_xpath = self.find_element("xpath",
                                           '//*[@content-desc="账单查询"]')
        if payquery_xpath is None:
            self.assertEqual(1, 2, "一键查询页面未找到账单查询入口，请检查！")

        # 进入账单查询页面
        payquery_xpath.click()
        time.sleep(10)

        # 查找账单查询页面的本月消费金额
        pay_xapth = self.find_element("xpath", '//*[@resource-id="monthTotal"]')
        if pay_xapth is None:
            self.driver.back()
            self.assertEqual(1, 2, "未查询到一键查询页面--账单查询--当月消费金额的xpath")

        # 取出当月消费金额
        text_data = pay_xapth.get_attribute("name")

        try:
            vx_text = float(text_data.replace("元", ""))
            logger.info("处理后数据为-->{}".format(vx_text))
        except:
            logger.war("一键查询页面--账单查询--当月消费金额时出现异常，异常金额为{}".format(text_data))
            self.driver.back()
            self.assertEqual(1, 2, "当前一键查询页面--账单查询--当月消费金额出现异常，异常金额为{}".format(text_data))

        # 当月数据异常时
        if vx_text is None or vx_text == "" or vx_text == 0:
            self.driver.back()
            self.assertEqual(1, 2, "一键查询页面--账单查询--当月消费金额数据出现异常，请检查！！")

        # 检查处理后数据类型为”--“的
        if not isinstance(vx_text, float):
            self.driver.back()
            self.assertEqual(1, 2, "当前一键查询页面--账单查询--当月消费金额数据出现异常，异常金额为{}".format(text_data))

        # 退出账单查询页面
        self.driver.back()

    def test_onekeyquery_check_xiangdanuqery(self):
        '''
        检查详单查询页面是否存在流量详单
        :return:
        '''
        # 定位一键查询页面详单查询xpath
        xiangdanquery_xpath = self.find_element("xpath",
                                                '//*[@content-desc="详单查询"]')
        if xiangdanquery_xpath is None:
            self.assertEqual(1, 2, "一键查询页面--详单查询入口不存在，请检查！！")

        # 点击详单查询入口，进入详单查询页面
        xiangdanquery_xpath.click()
        time.sleep(2)

        # 定位详单查询页面流量详单的xpath
        xiangdanliuliang = self.find_element("xpath", '//*[@content-desc="流量详单"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(xiangdanliuliang))
        if xiangdanliuliang is None:
            self.assertEqual(1, 2, "详单查询页面未定位到流量详单xpath")

    def test_onekeyquery_check_tonghuaxiangdan(self):
        '''
        检查详单查询页面是否存在通话详单
        '''
        xiangdantonghua = self.find_element("xpath", '//*[@content-desc="通话详单"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(xiangdantonghua))
        if xiangdantonghua is None:
            self.assertEqual(1, 2, "详单查询页面未定位到通话详单xpath")

    @unittest.skip("")
    def test_onekeyquery_check_smsxiangdan(self):
        '''
        检查详单查询页面是否存在短彩信详单
        '''
        smsxiangdan = self.find_element("xapth", '//*[@content-desc="您的收发短信、彩信记录"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(smsxiangdan))
        if smsxiangdan is None:
            self.assertEqual(1, 2, "详单查询页面未定位到短彩信详单xpath")

    @unittest.skip("")
    def test_onekeyquery_check_taocanfeiyongxiangdan(self):
        '''
        检查详单查询页面是否存在套餐及固定费用详单
        '''
        taocanfeiyongxiangdan = self.find_element("xapth", '//*[@content-desc="您的各类套餐费用等"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(taocanfeiyongxiangdan))
        if taocanfeiyongxiangdan is None:
            self.assertEqual(1, 2, "详单查询页面未定位到套餐及固定费用详单xpath")

    @unittest.skip("")
    def test_onekeyquery_check_addyewujilu(self):
        '''
        检查详单查询页面是否存在增值业务扣费记录
        '''
        addyewujilu = self.find_element("xapth", '//*[@content-desc="如您的彩铃、手机报等信息费"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(addyewujilu))
        if addyewujilu is None:
            self.assertEqual(1, 2, "详单查询页面未定位到增值业务扣费记录xpath")

    def test_oenkeyquery_check_daishouyewu(self):
        '''
        检查详单查询页面是否存在代收费用业务和扣费记录
        '''
        daishouyewu = self.find_element("xpath", '//*[@content-desc="代收费用业务扣费记录"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(daishouyewu))

        if daishouyewu is None:
            self.assertEqual(1, 2, "详单查询页面未定位到代收费用业务扣费记录xpath")

    def test_onekeyquery_check_otherjilu(self):
        '''
        检查详单查询页面是否存在其他费用扣费记录
        '''
        otherjilu = self.find_element("xpath", '//*[@content-desc="其他费用扣费记录"]').get_attribute("name")
        logger.info("定位到的页面元素是{}".format(otherjilu))

        if otherjilu is None:
            self.assertEqual(1, 2, "详单查询页面未定位到其他费用扣费记录xpath")

    def test_onekeyquery_check_onlineservicebutton(self):
        '''
        检查详单查询页面是否存在在线客服
        '''
        onlineservicebutton_xpath = self.find_element("xpath", '//*[@resource-id="drag"]')
        if onlineservicebutton_xpath is None:
            self.assertEqual(1, 2, "详单查询页面未定位到在线客服按钮xpath")
