from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import os


class Driver():
    def __init__(self):
        self.proxy = ""
    def get_new_proxy(self):
        file_path = Path(r"D:\proxy_server\data.txt")

        with file_path.open('r') as file:
            first_line = file.readline()
        self.proxy = first_line
        print(self.proxy)

    def get_new_driver(self):
        ## Example Proxy
        PROXY = self.proxy
        ## Create WebDriver Options to Add Proxy

        options = Options()
        options.add_experimental_option("detach", True)

        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "proxyType": "MANUAL",

        }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
        print(options)
        executable_path = "/webdrivers"
        os.environ["webdriver.chrome.driver"] = executable_path
        options.add_extension('CSFloat_Market_Checker.crx')

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        return driver
