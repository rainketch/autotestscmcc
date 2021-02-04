import os
import requests
from src.util.util_common import force_wait
import subprocess


class AppiumServer:
    def __init__(self, url="127.0.0.1", ap=4723, bp=5723, sp=6723):
        self.ap = ap
        self.bp = bp
        self.sp = sp
        self.url = url

    def start_server(self):
        node_server_path = ".\\libs\\nodejs\\node.exe"
        appium_server_path = ".\\libs\\appium\\build\\lib\\main.js"
        chrome_driver_path = ".\\libs\\chromedriver\\chromedriver.exe"
        command = "{} {} --address {} --port {} --bootstrap-port {} --selendroid-port {} --chromedriver.exe.exe-executable {} --no-reset " \
                  "--session-override".format(node_server_path, appium_server_path, self.url, self.ap, self.bp, self.sp, chrome_driver_path)

        # si = subprocess.STARTUPINFO()
        # si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # # si.wShowWindow = subprocess.SW_HIDE # default
        # subprocess.run(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.system(command)


def is_appium_server_running(ap=4724, to=30):
    """
    判断appium-server是否运行
    :param ap:
    :param timeout:
    :return:
    """
    timeout = 1
    while True:
        try:
            if timeout > to:
                return False
            url = "http://localhost:{}/wd/hub/status".format(ap)
            res = requests.get(url, timeout=timeout)
            res_json = res.json()
            return res_json["status"] == 0
        except:
            force_wait(1)
            timeout = timeout + 1
