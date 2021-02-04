# coding=utf-8

from src.util.util_xml import get_phone_config
from src.util.util_xml import get_project_config
from src.util.util_adb import is_connect_devices
from src.util.util_appium_server import AppiumServer, is_appium_server_running
from src.util.util_adb import restart_adb_server
from src.case.high_Android8.v430.test_basecase import TestCaseBase
from src.util.util_htmltestrunner_debug import HTMLTestRunner
from src.util.util_logger import logger
from src.util.util_excel import read_excel
from src.util.util_email import EmailReportTemplate, Mail
import os
from multiprocessing import Process
import time
import unittest


class AutoTestScmcc:
    def __init__(self):
        pass

    def generate_device_config(self, connected_device_info, current_version):
        '''
        生成手机的配置文件
        :return:
        '''
        # 创建配置文件
        dev_list = list()
        ap, bp, sp = 4720, 4721, 4722
        for dev in connected_device_info:
            ap, bp, sp = ap + 3, bp + 3, sp + 3
            dev["ap"], dev["bp"], dev["sp"] = ap, bp, sp
            dev["vn"] = current_version
            dev_list.append(dev)

    def _start_appium_servers(self, devices, ap=4721, bp=4722, sp=4723):
        '''
        多线程启动appium服务
        :param devices:
        :param ap:  appium-port
        :param bp:  bootstrap-port
        :param sp:  selendroid-port
        :return:
        '''
        for _ in devices:
            ap, bp, sp = ap + 3, bp + 3, sp + 3
            server = AppiumServer(ap=ap, bp=bp, sp=sp)
            p = Process(target=server.start_server)
            p.start()

        logger.info("等待20S启动AppiumServer")
        time.sleep(20)

    def _stop_appium_server(self):
        '''
        关闭appium服务
        :return:
        '''
        os.system("taskkill /f /im node.exe")

    def _get_test_suite(self, version="v430", kw="test_", device=None):
        '''
        获取测试组件
        :return:
        '''
        test_suites = list()
        test_suite = unittest.TestSuite()
        for dir in os.listdir("./src/case/{}".format(version)):
            if kw in dir:
                module = dir.split(".")[0]
                exec("from src.case.{} import {}".format(version, module))
                cless = list(eval(module).__dict__)[-1]

                exec("from src.case.{}.{} import {}".format(version, module, cless))
                print(eval(cless))
                test_suites.append(TestCaseBase.parametrize(eval(cless), param=device))
        test_suite.addTests(test_suites)
        return test_suite

    # def _run_case(self, report_path=None, device=None, version="v430", test_suite=None):
    #     '''
    #     执行case
    #     :return:
    #     '''
    #     start_test_time = time.strftime('%Y-%m-%D-%H-%M')
    #     print("开始执行手机【{}】的测试用例".format(device["band"]))
    #     test_suites = test_suite
    #     title = "xxx自动测试报告-{}".format(device["band"])
    #     description = "version:{},执行人:欣网测试组".format(version)
    #     with open("{}-{}-测试报告.html".format(report_path, device["band"], start_test_time), "wb") as f:
    #         runner = HTMLTestRunner(stream=f, verbosity=2, title=title, description=description, retry=1)
    #         result = runner.run(test_suites)

    def _generate_results(self, runner, result, version):
        """
        生成测试测试报告的邮件结果
        :param runner:
        :param result:
        :return:
        """
        s_id, f_id, e_id = 1, 1, 1
        success, errors, failures = [], [], []
        sorted_result = runner.sortResult(result.result)
        cases = read_excel("./doc/掌厅-原生页面和H5页面.xls", version)
        for cid, (cls, cls_results) in enumerate(sorted_result):
            for tid, (n, t, o, e) in enumerate(cls_results):
                module = self._get_case_module(cases, t._testMethodName)
                if n == 0:  # success
                    res = (s_id, module, t, "成功")
                    success.append(res)
                    s_id += 1
                if n == 1:  # fail
                    res = (f_id, module, t, "失败")
                    failures.append(res)
                    f_id += 1
                if n == 2:  # error
                    res = (e_id, module, t, "错误")
                    errors.append(res)
                    e_id += 1

        return success, errors, failures

    def _remove_retry_pass_result(self, success, errors, failures):
        '''
        结果去重处理
        :return:
        '''
        logger.info("开始对结果进行去重处理")
        if len(errors) == 0 and len(failures) == 0:
            logger.info("没有发现失败的case！")
            return success, errors, failures

        # 如果重新retry后的case在success中存在，那么则认为case通过
        for e in errors:
            for s in success:
                if e[2] == s[2]:
                    errors.remove(e)

        # 如果重新retry后的case在success中存在，那么则认为case通过
        for f in failures:
            for s in success:
                if f[2] == s[2]:
                    failures.remove(f)

        # 失败结果去重
        for f in failures:
            print(f)
            if f[2]._testMethodDoc is not None and "retry" in f[2]._testMethodDoc:
                failures.remove(f)
            print(failures)

        # 错误结果去重
        for e in errors:
            print(e)
            if e[2]._testMethodDoc is not None and "retry" in e[2]._testMethodDoc:
                errors.remove(e)
            print(errors)

        return success, errors, failures

    def _get_case_module(self, cases, case):
        '''
        获取case名
        :param cases:
        :param case:
        :return:
        '''
        try:
            for c in cases:
                if c[8].strip().lower() == case.strip().lower():
                    return c[1].strip() + "-" + c[2].strip() + "-" + c[6].strip()
        except Exception as ret:
            logger.info(ret)

        return ""

    def _send_mail(self, receiver, receive_title, receive_desc):
        '''
        发送邮件内容
        :param receiver: 收件人
        :param receive_title: 标题
        :param receive_desc: 内容
        :return:
        '''
        try:
            mail = Mail("694661248@qq.com", "", "smtp.qq.com")
            mail.send_mail(receiver, receive_title, receive_desc)
        except Exception as ret:
            logger.info(ret)

    def _push_result(self, success, errors, failures, start_testing_time, device_name, version):
        '''
        收集结果并发送报告
        :param success:
        :param errors:
        :param failures:
        :param start_testing_time:
        :param device_name:
        :param version:
        :return:
        '''
        logger.info("测试结果收集完成，开始发送邮件！！")
        receiver = ["18380430706@139.com"]  # 收件人

        if errors:
            logger.info("发现错误的case:-->{}".format(errors))
            report_title = "【错误反馈】-【{}】-{}".format(device_name, start_testing_time)
            report_desc = EmailReportTemplate().set_content(errors)

            try:
                self._send_mail(receiver, report_title, report_desc)
            except Exception as ret:
                logger.info(ret)

        if failures:
            logger.info("发现失败的case:-->{}".format(failures))
            report_title = "【失败反馈】-【{}】-欣网测试反馈{}-{}".format(device_name, version, start_testing_time)
            report_desc = EmailReportTemplate().set_content(failures)

            try:
                self._send_mail(receiver, report_title, report_desc)
            except Exception as ret:
                logger.info(ret)

    def run(self, connect_device=None):
        '''
        项目运行的入口
        '''
        # 1、读取机型配置文件信息

        logger.info("重新启动adb")
        restart_adb_server()
        time.sleep(10)
        all_config_devices = get_phone_config()
        all_project_info = get_project_config()

        global project_info
        for project_info in all_project_info:
            project_info = project_info

        # 2、获取链接的机型信息与配置文件进行匹配，并返回当前链接的机型的所有信息
        connected_device_info = is_connect_devices(all_config_devices)
        for connect_device in connected_device_info:
            connect_device = connect_device


        if len(connected_device_info) == 0 or len(connected_device_info) > 1:
            logger.error("未发现已连接的手机或手机数量大于1，终止本次测试")
            return False

        # 3、获取当前项目的版本
        # run_version = version.get("version")
        # ret = re.sub("[.]","", run_version).lower()
        current_project_version = project_info.get("version")
        curremnt_phone_version = connect_device.get("platformVersion")
        logger.info("已经获取到的当前项目的版本是:{}".format(current_project_version))
        logger.info("已经获取到当前连接的手机的系统版本是:{}".format(curremnt_phone_version))


        # 5.多线程运行appium服务器
        os.system("taskkill /f /im node.exe")
        self._start_appium_servers(connected_device_info)

        # 6.判断appium是否运行
        if is_appium_server_running() is False:
            print("appium-server启动失败,终止本次测试")
            return False

        # 7.创建测试报告文件夹
        reports = "./reports"
        if not os.path.exists(reports):
            os.mkdir(reports)

        logger.info("appium-server启动成功！！")

        # 8.收集测试用例
        # 1、
        # testsuite = self._get_test_suite()
        # print(testsuite)

        if float(curremnt_phone_version) < 8.0:
            logger.info("当前执行手机系统版本小于8.0")
            testsuite = unittest.TestLoader()
            testcase = testsuite.discover(r"./src/case/low_Android8/v430")
            for c in testcase:
                print(c)
        else:
            logger.info("当前执行手机系统版本大于8.0")
            testsuite = unittest.TestLoader()
            testcase = testsuite.discover(r"./src/case/high_Android8/v430")
            for c in testcase:
                print(c)

        # # 3、
        # setting.run_case = {Tag.ALL}  # 运行全部测试用例
        # # setting.run_case = {Tag.SMOKE}  # 只运行SMOKE标记的测试用例
        # # setting.run_case = {Tag.SMOKE, Tag.V1_0_0}   # 只运行SMOKE和V1_0_0标记的测试用例
        #
        # setting.check_case_doc = False  # 关闭检测是否编写了测试用例描述
        # setting.full_case_name = True
        # setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
        # setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
        # setting.sort_case = True  # 是否按照编写顺序，对用例进行排序
        # setting.create_report_by_style_1 = True  # 测试报告样式1
        # setting.create_report_by_style_2 = True  # 测试报告样式2
        # setting.show_print_in_console = True
        #
        # runner = TestRunner()
        # runner.add_case_dir(r"./src/case/v430")
        # runner.run_test(report_title="掌厅自动化测试")

        # 9.运行测试
        start_dir = "./src/case/{}/".format(current_project_version)
        start_testing_time = time.strftime('%Y-%m-%d-%H-%M')
        title, description = "四川移动掌厅自动测试报告", "version：{} 执行人：欣网四川区测试组".format(current_project_version)
        with open("{}/{}-测试报告.html".format(reports, start_testing_time), "wb") as f:
            runner = HTMLTestRunner(stream=f, verbosity=2, title=title, description=description, retry=0)
            result = runner.run(testcase)

        # self._run_case(report_path=reports, device=connect_device, version=current_version, test_suite=testsuite)
        # 10.对测试结果进行收集并处理
        logger.info("测试用例执行完成，开始收集结果！！")
        success, errors, failures = self._generate_results(runner, result, current_project_version)
        success, errors, failures = self._remove_retry_pass_result(success, errors, failures)

        # 11.将测试结果发送邮件
        # self._push_result(success, errors, failures, start_testing_time, connect_device, current_version)

        # 12.关闭appium服务
        logger.info("关闭appium-server服务")
        os.system("taskkill /f /im node.exe")


if __name__ == "__main__":
    autotest = AutoTestScmcc()
    autotest.run()

