from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import proxy_setup
import settings
import data
import time


def run():
    def auth():
        time.sleep(1)
        data.update_auth_data()
        login_button = driver.find_element(By.CLASS_NAME, "_2QgFEj17t677s3x299PNJQ")
        driver.find_element(By.CLASS_NAME, "_2eKVn6g5Yysx9JmutQe7WV").send_keys(settings.login)
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(settings.password)
        login_button.click()
        # driver.find_element(By.CLASS_NAME, "_3PDBFJ_verUpV38hX7qRqL Panel Focusable").send_keys(sda)
        time.sleep(settings.wait_for_sda)
    def get_new_proxy():
        with open("D:\\proxy_server\data.txt", 'r') as file:
            first_line = file.readline()
        print(first_line)
        return first_line


    base = proxy_setup.Driver()
    base.get_new_proxy()
    driver = base.get_new_driver()


    driver.get("https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_600__global-header")
    driver.maximize_window()
    auth()
    data.update_skin_link()
    driver.get(settings.skin_link)

if __name__ == "__main__":
    run()