from appium import webdriver
from src.util.util_xml import get_project_config, get_phone_config
from src.util.util_adb import is_connect_devices
from src.util.util_logger import logger
from src.util.util_adb import adb_slide_unlock
import re
from src.util.util_common import exec_cmd


class AppiumDriver:
    def __init__(self, device_name, platform_name, platform_version, app_package, app_activity, url):
        desired_caps = {}
        desired_caps['udid'] = device_name
        desired_caps['deviceName'] = device_name  # adb devices查到的设备名
        desired_caps['platformName'] = platform_name
        desired_caps['platformVersion'] = platform_version
        desired_caps['appPackage'] = app_package  # 被测App的包名
        desired_caps['appActivity'] = app_activity  # 启动时的Activity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['autoAcceptAlerts'] = True  # 自动设置弹窗警告，类似于权限申请
        desired_caps['recreateChromeDriverSessions'] = True
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # desired_caps['automationName'] = "UIAutomator2"

        # desired_caps['permissionPatterns'] = '[\\\"继续安装\\\",\\\"下一步\\\",\\\"好\\\",\\\"允许\\\",\\\"确定\\\",\\\"我知道\\\"]'

        self.android_driver = webdriver.Remote(url, desired_caps)

    def get_android_driver(self):
        return self.android_driver




def get_driver():
    # 判断哪些设备已经连接
    devices = get_phone_config()
    devices = is_connect_devices(devices)
    if len(devices) == 0 or len(devices) > 1:
        logger.error("未发现已连接的手机或手机数量大于1，终止本次测试...")
        return False

    ap, bp, sp = 4724, 4725, 4726
    for device in devices:
        # 获取设备信息并生成driver对象
        device_name = device["deviceName"]
        app_package = device["appPackage"]
        app_activity = device["appActivity"]
        platform_name = device["platformName"]
        platform_version = device["platformVersion"]
        url = "http://localhost:{}/wd/hub".format(str(ap))
        ap = ap + 3

        # 如果安卓版本大于5.1,appium解锁貌似失效（在vivo和oppo上面，其他机型没测试），并使用adb滑动解锁

        try:
            # if device_name == "88e3ab786d24":
            #     exec_cmd("adb shell input keyevent 26")
            # else:
                adb_slide_unlock(uuid=device_name, slide_dire="up")
        except:
            logger.error("自定义滑动解锁失败!")

        # 获取driver对象
        ad = AppiumDriver(device_name, platform_name, platform_version, app_package, app_activity, url)

        return ad.get_android_driver()