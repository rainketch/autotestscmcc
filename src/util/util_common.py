# -*- coding: utf-8 -*-
__author__ = 'snake'

import os
import time
import importlib


def data_format_print(str):
    """
    字符串格式化
    :param str:
    :return:
    """
    print(get_current_time() + ":" + str)




def get_current_time(type="d"):
    """
    获取当前时间
    :param type:
    :return:
    """
    if type == "d":
        format_str = "%Y-%m-%d"
    if type == "H":
        format_str = "%Y-%m-%d-%H"
    if type == "M":
        format_str = "%Y-%m-%d-%H-%M"
    if type == "S":
        format_str = "%Y-%m-%d-%H-%M-%S"

    return time.strftime(format_str, time.localtime(time.time()))


def exec_cmd(cmd):
    """
    执行cmd命令并返回实时输出结果
    :param cmd:
    :return:
    """
    try:
        r = os.popen(cmd)
        text = r.read()
        r.close()
    except:
        pass

    return text


def force_wait(secs=3):
    """
    强制登录
    :param secs:
    :return:
    """
    time.sleep(secs)


def wait(driver, secs):
    """
    动态等待
    :param driver: 
    :param secs: 
    :return: 
    """
    driver.implicitly_wait(secs)


if __name__ == "__main__":
    print(get_all_testcases(classpath="../case", kw="test"))
