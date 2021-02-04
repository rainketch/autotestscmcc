'''
首页-官方充值
'''

# -*- coding: utf-8  -*-
__author__ = 'snake'

import unittest
from src.case.high_Android8.v430.test_basecase import TestCaseBase
from src.case.high_Android8.bll.v430.index import _close_msg_alert

@unittest.skip("")
class TestCasegfcz(TestCaseBase):

    # def test_gfcz_checknumber(self):
    #     '''
    #     充值号码应该与登录号码一致
    #     :return:
    #     '''
    #     # 进入我的页面获取用户登录的手机号码
    #     my_btn = "//android.widget.TextView[@text='我的']"
    #     menu_layout = "com.sunrise.scmbhc:id/menubottomlayout"
    #
    #
    #     menu_layout_obj = self.find_element("id", menu_layout)
    #     menu_layout_obj.find_element("xpath", my_btn).click()
    #     self.find_element("id", "com.sunrise.scmbhc:id/id_my_mobile_number").click()
    #
    #     user_number = self.find_element("id", "com.sunrise.scmbhc:id/user_phone", timeout=30)
    #     user_info_phone = user_number.text
    #     # 获取用户充值页面号码
    #     self.driver.back()
    #     self.find_element("xpath", "//android.widget.TextView[@text='首页']").click()
    #
    #     time.sleep(1)
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     user_chongzhi_index_number = self.find_element("id", "com.sunrise.scmbhc:id/mPhoneNumber")
    #     user_chongzhi_number = user_chongzhi_index_number.text
    #     self.assertEquals(user_chongzhi_number, user_info_phone, "检查用户号码与首页号码一致")


    def test_gfcz_checktext(self):
        '''
        检查官方充值，品质保障文本
        :return:
        '''
        # 进入我的页面
        my_btn = "//android.widget.TextView[@text='我的']"
        self.find_element('xpath', my_btn).click()
        # 进入官方充值页面
        self.find_element('xpath', "//android.widget.LinearLayout[@resource-id='com.sunrise.scmbhc:id/my_mobile_myBalance']/android.widget.LinearLayout[1]").click()

        _close_msg_alert(self.driver)

        text_id = "com.sunrise.scmbhc:id/title_tv"
        official_index = self.find_element("id", text_id)
        official_text = official_index.text
        self.assertEqual("官方充值", official_text, "检查文字的一致性")


    def test_gfcz_checkzfb(self):
        '''
        检查支付方式中存在支付宝
        :return:
        '''
        # 进入我的页面
        my_btn = "//android.widget.TextView[@text='我的']"
        self.find_element('xpath', my_btn).click()

        # 进入官方充值页面
        self.find_element('xpath',
                          "//android.widget.LinearLayout[@resource-id='com.sunrise.scmbhc:id/my_mobile_myBalance']/android.widget.LinearLayout[1]").click()

        _close_msg_alert(self.driver)
        zhifubao_tubiao = "//android.widget.GridView[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[1]"
        zhifubao_shortcut = self.find_element("xpath", zhifubao_tubiao)
        if zhifubao_shortcut is not None:
            self.assertEquals(True, True, "支付宝快捷方式存在")
        else:
            self.assertEquals(True, False, "支付宝快捷方式不存在")

    #
    # def test_gfcz_checkweixin(self):
    #     '''
    #     检查微信快捷方式存在
    #     :return:
    #     '''
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     weixin_tubiao = "//android.widget.GridView[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[2]"
    #     weixin_shortcut = self.find_element("xpath", weixin_tubiao)
    #     if weixin_shortcut is not None:
    #         self.assertEquals(True, True, "微信快捷方式存在")
    #     else:
    #         self.assertEquals(True, False, "微信快捷方式不存在")
    #
    # def test_gfcz_checkhebzh(self):
    #     '''
    #     检查和包支付快捷方式存在
    #     :return:
    #     '''
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     hebaozf_tubiao = "//android.widget.GridView[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[3]"
    #     hebaozh_shortcut = self.find_element("xpath", hebaozf_tubiao)
    #     if hebaozh_shortcut is not None:
    #         self.assertEquals(True, True, "和包支付快捷方式存在")
    #     else:
    #         self.assertEquals(True, False, "和包支付快捷方式不存在")
    #
    # def test_gfcz_checklinks(self):
    #     '''
    #     检查交费记录查询链接
    #     :return:
    #     '''
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     # 跳转到交费记录查询页面
    #     jfjl = "//android.widget.ListView[@resource-id='com.sunrise.scmbhc:id/charge_listview']/android.widget.LinearLayout[1]"
    #     self.find_element("xpath", jfjl).click()
    #
    #     # 检查提示语是否正确，正确则证明跳转正常
    #     pageone = "//android.widget.TextView[@resource-id='com.sunrise.scmbhc:id/recharge_record_tips']"
    #     pageoneifexist = self.find_element("xpath", pageone)
    #     if pageoneifexist is not None:
    #         self.assertEquals(1, 1, "交费记录页面跳转后页面正常显示")
    #     else:
    #         self.assertEquals(1, 2, "交费记录页面不存在或者交费记录异常")
    #
    # def test_czjf_checkhuodxize(self):
    #     '''
    #     检查和包95折活动细则
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #     time.sleep(1)
    #
    #     # 跳转到活动细则页面
    #     self.driver.swipe(100, 800, 100, 100)
    #     time.sleep(2)
    #     obj = self.find_element("id", "com.sunrise.scmbhc:id/rl_rule_tips")
    #     self.assertIsNotNone(obj, "活动细则页面不为空")
    #
    # def test_gfcz_zhifubao10jine(self):
    #     '''
    #     检查支付宝支付10元的显示
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     # 选择支付方式和充值金额
    #     zhbshortcut = "//android.widget.GridView[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[1]"
    #     clickshortcut = self.find_element("xpath", zhbshortcut)
    #     clickshortcut.click()
    #     time.sleep(1)
    #
    #     zhifujine = "//android.widget.TextView[@text='10元支付9.98元']"
    #     zhifujineid = self.find_element("id", "com.sunrise.scmbhc:id/yh_gridview")
    #     objs = zhifujineid.find_elements("id", "com.sunrise.scmbhc:id/txt")
    #
    #     objs[0].click()
    #
    #     oopb = self.find_element("id", "com.sunrise.scmbhc:id/money_num")
    #     oopb1 = oopb.text
    #     actual = self.find_element("id", "com.sunrise.scmbhc:id/money_actual_num")
    #     actualmoney = actual.text
    #
    #     if oopb1 == "9.98" and actualmoney == "10":
    #         self.assertEquals(1, 1, "支付宝支付10元显示正确")
    #     else:
    #         self.assertEquals(1, 2, "支付宝支付10元异常")
    #
    # def test_gfcz_zhifubaojine200jine(self):
    #     '''
    #     检查支付宝支付200元的界面显示
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     # 选择支付方式和充值金额
    #     zhbshortcut = "//android.widget.GridView" \
    #                   "[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[1]"
    #     clickshortcut = self.find_element("xpath", zhbshortcut)
    #     clickshortcut.click()
    #     time.sleep(1)
    #
    #     zhifujineid = self.find_element("id", "com.sunrise.scmbhc:id/yh_gridview")
    #     objs = zhifujineid.find_elements("id", "com.sunrise.scmbhc:id/txt")
    #     logger.info(len(objs))
    #     objs[4].click()
    #
    #     zhifu = self.find_element("id", "com.sunrise.scmbhc:id/money_num")
    #     zhifujine = zhifu.text
    #     actual = self.find_element("id", "com.sunrise.scmbhc:id/money_actual_num")
    #     actualmoney = actual.text
    #
    #     if zhifujine == "199.6" and actualmoney == "200":
    #         self.assertEquals(1, 1, "支付宝支付200元显示正常")
    #     else:
    #         self.assertEquals(1, 2, "支付宝支付200元异常")
    #
    # def test_gfcz_weixinzhif50(self):
    #     '''
    #     检查微信支付50元金额的显示
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     # 选择微信支付
    #     weixinshortcut = "//android.widget.GridView" \
    #                      "[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[2]"
    #     clickshortcut = self.find_element("xpath", weixinshortcut)
    #     clickshortcut.click()
    #     time.sleep(1)
    #     # 选择微信支付金额
    #     zhifujineid = self.find_element("id", "com.sunrise.scmbhc:id/yh_gridview")
    #     objs = zhifujineid.find_elements("id", "com.sunrise.scmbhc:id/txt")
    #     logger.info(len(objs))
    #     objs[2].click()
    #
    #     # 判断支付金额和实际到账金额显示
    #     zhifu = self.find_element("id", "com.sunrise.scmbhc:id/money_num")
    #     zhifujine = zhifu.text
    #     actual = self.find_element("id", "com.sunrise.scmbhc:id/money_actual_num")
    #     actualmoney = actual.text
    #
    #     if zhifujine == "49.9" and actualmoney == "50":
    #         self.assertEquals(1, 1, "微信支付50元显示正常")
    #     else:
    #         self.assertEquals(1, 2, "微信支付50元异常")
    #
    # def test_gfcz_weixinzhif100(self):
    #     '''
    #     检查微信支付100元的界面显示
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     # 选择微信支付
    #     weixinshortcut = "//android.widget.GridView" \
    #                      "[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[2]"
    #     clickshortcut = self.find_element("xpath", weixinshortcut)
    #     clickshortcut.click()
    #     time.sleep(1)
    #
    #     # 选择微信支付金额
    #     zhifujineid = self.find_element("id", "com.sunrise.scmbhc:id/yh_gridview")
    #     objs = zhifujineid.find_elements("id", "com.sunrise.scmbhc:id/txt")
    #     logger.info(len(objs))
    #     objs[3].click()
    #
    #     # 判断支付金额和实际到账金额显示
    #     zhifu = self.find_element("id", "com.sunrise.scmbhc:id/money_num")
    #     zhifujine = zhifu.text
    #     actual = self.find_element("id", "com.sunrise.scmbhc:id/money_actual_num")
    #     actualmoney = actual.text
    #
    #     if zhifujine == "99.8" and actualmoney == "100":
    #         self.assertEquals(1, 1, "微信支付100元显示正常")
    #     else:
    #         self.assertEquals(1, 2, "微信支付100元异常")
    #
    # def test_gfcz_hebaozhif30(self):
    #     '''
    #     检查和包充值30元的显示
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #
    #     # 页面滑动到底部
    #     time.sleep(2)
    #     self.driver.swipe(100, 300, 100, 100)
    #
    #     # 选择和包支付
    #     hebaoshortcut = "//android.widget.GridView" \
    #                     "[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[3]"
    #     clickshortcut = self.find_element("xpath", hebaoshortcut)
    #     clickshortcut.click()
    #     time.sleep(1)
    #
    #     # 选择支付金额
    #     zhifujineid = self.find_element("id", "com.sunrise.scmbhc:id/yh_gridview")
    #     objs = zhifujineid.find_elements("id", "com.sunrise.scmbhc:id/txt")
    #     objs[0].click()
    #
    #     # 判断支付金额和实际到账金额显示
    #     zhifu = self.find_element("id", "com.sunrise.scmbhc:id/money_num")
    #     zhifujine = zhifu.text
    #     actual = self.find_element("id", "com.sunrise.scmbhc:id/money_actual_num")
    #     actualmoney = actual.text
    #
    #     if zhifujine == "30" and actualmoney == "30+1.8":
    #         self.assertEquals(1, 1, "和包支付30元显示正常")
    #     else:
    #         self.assertEquals(1, 2, "和包支付30元异常")
    #
    # def test_gfcz_hebaozhif300(self):
    #     '''
    #     检查和包支付300元界面显示
    #     :return:
    #     '''
    #     # 跳转到官方充值页面
    #     guanfangchongzhi = self.find_element('xpath', "//android.widget.TextView[@text='官方充值']")
    #     guanfangchongzhi.click()
    #     time.sleep(2)
    #     self.driver.swipe(100, 800, 100, 100)
    #     time.sleep(2)
    #
    #     # 选择和包支付
    #     payments = self.find_element("id", "com.sunrise.scmbhc:id/gv_pay")
    #     hebao_pay = payments.find_elements("id", "com.sunrise.scmbhc:id/item_pay_mode_parent")
    #     hebao_pay[2].click()
    #     # hebaoshortcut = "//android.widget.GridView" \
    #     #                 "[@resource-id='com.sunrise.scmbhc:id/gv_pay']/android.widget.LinearLayout[3]"
    #     # clickshortcut = self.find_element("xpath", hebaoshortcut)
    #     # clickshortcut.click()
    #
    #     # 选择支付金额
    #     zhifujineid = self.find_element("id", "com.sunrise.scmbhc:id/yh_gridview")
    #     objs = zhifujineid.find_elements("id", "com.sunrise.scmbhc:id/txt")
    #     objs[4].click()
    #
    #     # 判断支付金额和实际到账金额显示
    #     zhifu = self.find_element("id", "com.sunrise.scmbhc:id/money_num")
    #     zhifujine = zhifu.text
    #     actual = self.find_element("id", "com.sunrise.scmbhc:id/money_actual_num")
    #     actualmoney = actual.text
    #
    #     if zhifujine == "300" and actualmoney == "300+18":
    #         self.assertEquals(1, 1, "和包支付300元显正常")
    #     else:
    #         self.assertEquals(1, 2, "和包支付300元异常")