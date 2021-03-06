# -*- coding: utf-8 -*-
"""
首页相关业务代码
"""
__author__ = 'snake'

import time
from src.util.util_logger import logger
from src.util.util_appium_tools import find_element


def back_to_index(driver):
    """
    返回到首页
    :return: True:成功; False:失败
    """
    logger.info("开始执行back_to_index方法")

    timeout = 1
    while True:
        try:
            _close_app_update_alert(driver)
            _close_msg_alert(driver)

            if timeout > 5:
                logger.war("定位首页失败，失败原因:重试第5次失败, 返回值:False")
                return False

            time.sleep(3)

            # 这里判断activity
            home_activity = ".ui.activity.home.HomeActivity"
            if driver.current_activity != home_activity:
                logger.info("首页activity->{}".format(home_activity))
                logger.info("当前activity->{}".format(driver.current_activity))
                raise Exception("重试中")
            else:
                my_btn = "//android.widget.TextView[@text='我的']"
                home_btn = "//android.widget.TextView[@text='首页']"
                menu_layout = "com.sunrise.scmbhc:id/menubottomlayout"

                logger.info("第{}次定位首页和我的按钮,方式->by_xpath, 首页->{},我的->{}".format(timeout, home_btn, my_btn))
                menu_layout_obj = find_element(driver, "id", menu_layout)
                my = find_element(menu_layout_obj, "xpath", my_btn)
                home = find_element(menu_layout_obj,"xpath",home_btn)
                # my = find_element(menu_layout, "xpath", '//*[@text="我的"]')
                # home = find_element(menu_layout, "xpath", '//*[@text="首页"]')

                if my is not None and home is not None:
                    while True:
                        logger.info("发现首页和我的按钮.定位首页成功, 执行点击操作")
                        home.click()
                        time.sleep(5)
                        logger.info("成功定位首页元素,方法退出, 返回True")
                        banner_xpath = find_element(driver, "xpath",'//*[@resource-id="com.sunrise.scmbhc:id/banner_img"]',timeout=3)
                        if banner_xpath:
                            logger.info("成功定位banner框，返回首页顶部成功！！")
                            return True
                else:
                    logger.war("只发现首页或我的按钮，重试")
                    raise Exception("重试")

        except:
            logger.war("定位首页失败,等待3秒开始第{}次重试".format(timeout))
            time.sleep(3)
            timeout = timeout + 1
            # 退出了app
            if driver.current_activity == ".Launcher":
                logger.war("当前页面退出了app，正在重新启动app")
                driver.launch_app()

            if driver.current_activity != ".ui.activity.loading.LoadingActivity":
                logger.info("开始点击返回按钮")
                driver.back()
                logger.info("成功点击返回按钮")
                _close_app_update_alert(driver)
                _close_msg_alert(driver)




def close_index_alerts(driver):
    """
    关闭首页各种弹框
    :param driver:
    :return:
    """
    # 极端情况可能初选3中弹窗同时出现
    logger.info("开始执行close_index_alerts方法")

    timeout = 1
    while True:
        try:
            if timeout > 10:
                logger.war("定位首页手机号元素失败，失败原因:重试第10次失败")
                logger.info("当前activity->{}".format(driver.current_activity))
                logger.info("尝试返回到主页重新定位")
                return back_to_index(driver)

            logger.info("第{}次开始定位首页扫描二维码,方式->by_id, 值->com.sunrise.scmbhc:id/sm_scanimg".format(timeout))
            driver.find_element_by_id("com.sunrise.scmbhc:id/main_top_view")
            logger.info("成功定位首页扫描加号元素,方法退出, 返回True")
            return True

        except:
            logger.war("定位首页扫描加号元素失败,等待1秒开始第{}次重试".format(timeout))
            time.sleep(1)
            timeout = timeout + 1
            _close_app_update_alert(driver)
            _close_msg_alert(driver)

    logger.info("定位首页扫描二维码元素失败,返回值:False")
    return False

def close_broadband_alerts(driver):
    '''
    关闭进入宽带页面后的各种弹窗
    '''
    logger.info("开始执行close_broadband_alerts方法")
    try:
        while True:
            pagexpath = driver.find_element_by_xpath('//*[@content-desc="goto"]')
            if pagexpath is not None:
                pagexpath.click()

    except Exception as ret:
        logger.info("页面中未找到下一步xpath,已经在智慧家庭宽带页面，方法退出, 返回True")
        return False




def _close_index_alerts_by_back(driver):
    """
    通过返回键关闭弹窗
    :param driver:
    :return:
    """
    logger.info("开始执行_close_index_alerts_by_back方法")

    timeout = 1
    while True:
        try:
            if timeout > 5:
                logger.war("通过返回键关闭弹窗失败, 返回值:False")
                return False

            logger.info("第{}次开始定位首页扫描二维码,方式->by_id, 值->com.sunrise.scmbhc:id/sm_scanimg".format(timeout))
            driver.find_element_by_id("com.sunrise.scmbhc:id/sm_scanimg")
            logger.info("成功定位首页扫描二维码元素,方法退出, 返回True")
            return True

        except:
            timeout = timeout + 1
            logger.war("定位首页扫描二维码元素失败,等待1秒开始第{}次重试".format(timeout))
            time.sleep(3)

def close_msg_alert(driver):
    _close_msg_alert(driver)


def _close_msg_alert(driver):
    """
    检查是否有alert,有则关闭；无则不用管
    :param driver:
    :return:
    """
    logger.info("开始执行_close_msg_alert方法")
    try:
        logger.info("开始定位首页推荐弹出框元素,方式->by_id, 值->com.sunrise.scmbhc:id/pop_image_close")
        driver.find_element_by_id("com.sunrise.scmbhc:id/pop_image_close").click()
        logger.info("成功定位首页推荐弹出框元素,方法退出, 返回True")
        return True

    except Exception as e:
        logger.war("未发现首页推荐弹出框元素,方法退出, 返回False")

    return False

def _login_msg_alert(driver):
    """
    检查登录成功后是否有alert,有则关闭；无则不用管
    :param driver:
    :return:
    """
    logger.info("开始执行_login_msg_alert方法")
    try:
        logger.info("开始定位登录成功后有无服务提醒确认框,方式->by_xpath, 值->//android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        logger.info("成功定位登录成功后有无服务提醒确认框元素,方法退出, 返回True")
        return True

    except Exception as e:
        logger.war("未发现登录成功后提醒确认框元素,方法退出, 返回False")

    return False



def _close_app_update_alert(driver):
    """
    检查是否有alert,有则关闭；无则不用管
    :param driver:
    :return:
    """
    logger.info("开始执行_close_app_update_alert方法")
    try:
        logger.info("开始定位首页app更新类型弹出框元素,方式->by_id, 值->com.sunrise.scmbhc:id/d_two_title_tv")
        title = driver.find_element_by_id("com.sunrise.scmbhc:id/d_two_title_tv")
        if title.text == "下线通知":
            logger.info("发现下线通知, 信息为->{}".format(title))
            driver.find_element_by_id("com.sunrise.scmbhc:id/confirmButton").click()
            logger.info("点击下线通知重新登录按钮")
            logger.info("点击返回按钮")
            driver.back()
        else:
            logger.info("发现更新通知, 信息为->{}".format(title))
            driver.find_element_by_id("com.sunrise.scmbhc:id/cancelButton").click()
            logger.info("点击现更新通知取消按钮,方法退出,返回True")

        return True

    except Exception as e:
        logger.war("未发现首页app更新类型弹出框元素,方法退出, 返回False")

    return False

