# -*- coding:UTF-8 -*-
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class downloader(object):
    def __init__(self):
        options = Options()
        options.page_load_strategy = 'eager'  # 页面加载策略 normal eager none
        self.driver = webdriver.Chrome(options=options)

    def get_download_url(self):
        self.driver.get('https://www.baidu.com')
        self.driver.get('https://www.33yq.org')
        html = self.driver.page_source
        print(html)
        self.driver.get('https://www.baidu.com')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chromedriver_autoinstaller.install()

    # PROXY = "202.109.157.66:9000"
    # webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "proxyType": "MANUAL"
    # }
    #
    # with webdriver.Chrome() as driver:
    #     driver.get("https://selenium.dev")


    # options = Options()
    # options.page_load_strategy = 'normal'  # 页面加载策略 normal eager none
    # driver = webdriver.Chrome(options=options)
    #
    # driver.get('https://www.baidu.com')
    #
    # driver.get('http://www.spiderpy.cn/')
    #
    # driver.get('https://www.baidu.com')
    #
    # dl = downloader()
    # dl.get_download_url()

    old_fail_indexs = [2,3,5,7,8]
    for i in old_fail_indexs:
        print(i)