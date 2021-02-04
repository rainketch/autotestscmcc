
# -*- coding: utf-8  -*-
__author__ = 'snake'


import unittest
from src.case.low_Android8.v430.test_basecase import TestCaseBase
import time
from src.util.util_logger import logger
from src.case.low_Android8.bll.v430.index import close_broadband_alerts,close_index_alerts
from src.util.util_adb import exec_cmd

@unittest.skip("")
class Test_BroadBand(TestCaseBase):
    '''
    宽带专区测试
    '''
    def into_broadbandpage(self):
        '''
        进入宽带页面
        '''
        # 从十宫格位置进入智慧家庭页面
        bankuandai_button = self.find_element("xpath",
                                              '//*[@resource-id="com.sunrise.scmbhc:id/gridview_main_bis"]/android.widget.LinearLayout[3]')
        if bankuandai_button is None:
            self.assertEqual(1,2, "十宫格处为定位到智慧家庭入口，请检查！！")
        bankuandai_button.click()
        time.sleep(5)

        # 关闭进入页面后的各种弹窗
        close_broadband_alerts(self.driver)

    def test_checkkuandai_button(self):
        '''
        检查办宽带的图标是否存在
        :return:
        '''
        bankuandai_button = self.find_element("xpath",
                                              '//*[@resource-id="com.sunrise.scmbhc:id/gridview_main_bis"]/android.widget.LinearLayout[3]')
        if bankuandai_button is None:
            self.assertEqual(1, 2, "未找到宫格办理宽带图标，请检查！！")

    def test_kuandai_check_wifihotmap(self):
        '''
        检查宽带页面wifi热力图是否存在和是否成功进入页面
        :return:
        '''

        # 进入宽带专区页面
        self.into_broadbandpage()
        try:
            # 查找wifi热力图入口
            wifi_hotmap = self.find_element("xpath", '//*[@content-desc="WiFi热力图"]')
            if wifi_hotmap is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到wifi热力图！")
            else:

                # 进入wifi热力图页面
                wifi_hotmap.click()
                time.sleep(3)

                # 查找wifi热力图元素
                pagecontent = self.find_element("xpath", '//*[@content-desc="第一步:搜索户型"]')
                if pagecontent is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "未定位到wifi热力图页面相关元素，请检查！！")
                else:
                    logger.info("成功进入wifi热力图页面！！")
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面wifi热力图是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面wifi热力图时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到wifi热力图xpath")


    def test_kuandai_check_yijianzhenduan(self):
        '''
        检查一键诊断入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 查找一键诊断入口
            yijianzhenduan_xpath = self.find_element("xpath", '//*[@content-desc="一键诊断"]')
            if yijianzhenduan_xpath is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到一键诊断入口！！")
            else:

                # 进入一键诊断页面
                yijianzhenduan_xpath.click()
                time.sleep(5)

                # 查找一键诊断页面元素
                pagetitle_xpath = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/title_rlayout"]')
                if pagetitle_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "未找到一键诊断页面title，请检查")
                else:
                    logger.info("已经进入一键诊断页面，已定位到页面title-->xpath为{}".format(pagetitle_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面一键诊断是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面一键诊断时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到一键诊断xpath")

    def test_kuandai_check_shuxiang_service(self):
        '''
        检查舒享服务入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 定位智慧家庭页面舒享服务xpath
            shuxiang_service = self.find_element("xpath", '//*[@content-desc="舒享服务"]')
            if shuxiang_service is None:
                self.assertEqual(1, 2, "未定位到智慧家庭页面舒享服务入口xpath，请检查！！")
            else:
                # 进入舒享服务页面
                shuxiang_service.click()
                time.sleep(2)

                # 查找舒享服务页面元素
                page_xpath = self.find_element("xpath", '//*[@content-desc="舒享服务"]/android.view.View[1]')
                if page_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "未定位到舒享服务页面元素，请检查")
                else:
                    logger.info("已经进入舒享服务页面，已定位到页面元素-->xpath为{}".format(page_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面舒享服务是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面舒享服务时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到舒享服务xpath")

    def test_kuandai_service_enginor(self):
        '''
        检查服务工程师入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 查找智慧家庭--服务工程师xpath
            enginer_xpath = self.find_element("xpath", '//*[@content-desc="智慧家庭"]/android.widget.ListView[2]/android.view.View[4]')
            if enginer_xpath is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到服务工程师xpath，请检查")
            else:
                # 进入服务工程师页面
                enginer_xpath.click()
                time.sleep(2)

                # 非宽带用户查看中服务工程师页面元素
                no_broadband_xpath = self.find_element("xpath", '//*[@content-desc="null_com"]')
                if no_broadband_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "服务工程师页面未找到相关的页面元素，请检查")
                else:
                    logger.info("已经进入服务工程师页面，定位到的xpth是{}".format(no_broadband_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面服务工程师页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面服务工程师时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到服务工程师xpath")

    def test_kuandai_query_progress(self):
        '''
        检查进度查询入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 查找智慧家庭页面--进度查询xpath
            progress_xpath = self.find_element("xpath", '//*[@content-desc="进度查询"]')
            if progress_xpath is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到进度查询xpath，请检查！！")
            else:
                # 进入进度查询页面
                progress_xpath.click()
                time.sleep(5)

                # 查找进度查询页面元素
                progress_page_xpath = self.find_element("xpath", '//*[@content-desc="bannar"]')
                if progress_page_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "在进度查询页面未找到相关的页面元素，请检查！！")
                else:
                    logger.info("成功进入进度查询页面，页面中定位到元素的xpath是-->{}".format(progress_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面进度查询页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面进度查询时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到进度查询xpath")

    def test_kuandai_check_onekeyrenew(self):
        '''
        检查一键续费是否存在
        :return:
        '''
        try:
            # 查找智慧家庭页面--一键续费xpath
            onekeyrenew_xpath = self.find_element("xpath", '//*[@content-desc="一键续费"]')
            if onekeyrenew_xpath is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到一键续费xpath，请检查！！")
            else:
                # 进入一键续费页面
                onekeyrenew_xpath.click()
                time.sleep(2)

                # 检查充值页面的弹窗，如果存在则关闭
                close_index_alerts(self.driver)

                # 查找一键续费页面中立即充值按钮的xpath
                charge_btn_xpath = self.find_element("xpath", '//*[@resource-id="com.sunrise.scmbhc:id/charge_btn"]')
                if charge_btn_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "一键续费页面未找到相关的xpath元素，请检查")
                else:
                    logger.info("成功进入一键续费页面，页面中定位到元素的xpath是-->{}".format(charge_btn_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面一键续费页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面一键续费时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到一键续费xpath")

    def test_kuandai_check_hejiahuan(self):
        '''
        检查合家欢入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 查找智慧家庭页面--合家欢xpath
            hejiahuan_xpath = self.find_element("xpath", '//*[@content-desc="合家欢"]')
            if hejiahuan_xpath is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到合家欢xpath，请检查！！")
            else:
                # 进入合家欢页面
                hejiahuan_xpath.click()
                time.sleep(2)

                # 查找合家欢页面中banner图标的xpath
                hejiahuan_banner_xpath = self.find_element("xpath", '//*[@content-desc="合家欢"]/android.view.View[1]')
                if hejiahuan_banner_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "合家欢页面未找到相关的xpath元素，请检查！！")
                else:
                    logger.info("成功进入合家欢页面，页面中定位到元素的xpath是-->{}".format(hejiahuan_banner_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面合家欢页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面合家欢时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到合家欢xpath")

    def test_kuandai_check_family_member(self):
        '''
        检查家庭成员+入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 查找智慧家庭页面--家庭成员+xpath
            familymember_xpath = self.find_element("xpath", '//*[@content-desc="宽带成员+"]')
            if familymember_xpath is None:
                self.assertEqual(1, 2, "智慧家庭页面未找到家庭成员+的xpath，请检查！！")
            else:
                # 进入家庭成员+页面
                familymember_xpath.click()
                time.sleep(2)

                # 查找家庭成员+页面中去开通按钮的xpath
                page_prompt_xpath = self.find_element("xpath", '//*[@content-desc="去开通"]')
                if page_prompt_xpath is None:
                    self.driver.back()
                    self.assertEqual(1, 2, "家庭成员+页面未找到去开通按钮xpath元素，请检查！！")
                else:
                    logger.info("成功进入家庭成员+页面，页面中定位到元素的xpath是-->{}".format(page_prompt_xpath))
                    self.driver.back()
        except Exception as ret:
            logger.war("检查宽带页面家庭成员+页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面家庭成员+时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到家庭成员+xpath")

    def test_kuandai_check_bdpassword(self):
        '''
        检查宽带密码入口是否存在和是否成功进入页面
        :return:
        '''
        try:
            # 向左滑动屏幕进入宽带密码页面
            exec_cmd("adb shell input touchscreen swipe 958 1150 100 1150")
            time.sleep(1)
            # 暂时无法查找智慧家庭页面--宽带密码xpath

            # 进入宽带密码页面--暂时使用点击坐标的方法进入（使用手机为oppo）
            exec_cmd("adb shell input touchscreen tap 154 1047")
            time.sleep(2)

            # 非宽带用户查找宽带密码页面中提示框的的xpath
            no_broadband_xpath = self.find_element("xpath", '//*[@content-desc="null_com"]')
            if no_broadband_xpath is None:
                self.driver.back()
                exec_cmd("adb shell input touchscreen swipe 100 1150 985 1150")
                self.assertEqual(1, 2, "宽带密码页面未找到相关的xpath元素，请检查！！")
            else:
                logger.info("成功进入宽带密码页面，页面中定位到元素的xpath是-->{}".format(no_broadband_xpath))
                self.driver.back()
                exec_cmd("adb shell input touchscreen swipe 100 1150 985 1150")

        except Exception as ret:
            logger.war("检查宽带页面宽带密码页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面宽带密码时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到宽带密码xpath")

    def test_kuandai_check_passwordreset(self):
        '''
        检查电视付费密码重置入口是否存在和是否成功进入
        :return:
        '''
        try:
            # 向左滑动屏幕进入电视付费密码重置页面
            exec_cmd("adb shell input touchscreen swipe 958 1150 100 1150")
            time.sleep(1)

            # 进入密码重置页面--暂时使用点击坐标的方法进入（使用手机为oppo）
            exec_cmd("adb shell input touchscreen tap 406 1047")
            time.sleep(2)

            # 查找密码重置页面中下一步按钮的xpath
            next_step_xpath = self.find_element("xpath", '//*[@content-desc="下一步"]')
            if next_step_xpath is None:
                self.driver.back()
                self.driver.back()
                self.assertEqual(1, 2, "密码重置页面未找到相关的xpath元素，请检查！！")
            else:
                self.driver.back()
                self.driver.back()
                logger.info("成功进入密码重置页面，页面中定位到元素的xpath是-->{}".format(next_step_xpath))
        except Exception as ret:
            logger.war("检查宽带页面密码重置页面是否存在时出现异常，异常原因-->{}".format(ret))
            self.assertEqual(1, 2, "检查宽带页面密码重置时出现错误，可能原因是未定位到十宫格智慧家庭xpath或者未定位到密码重置xpath")

