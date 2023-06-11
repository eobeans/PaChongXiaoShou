# -*- coding:UTF-8 -*-

import time
import os
import random
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

class downloader(object):
    def __init__(self):
        options = Options()
        options.page_load_strategy = 'eager'  # 页面加载策略 normal eager none
        self.driver = webdriver.Chrome(options=options)
        self.server = 'https://www.33yq.org'
        self.target = 'https://www.33yq.org/read/139956/'  # 'https://www.33yq.org/read/143610/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        self.names = []  # 存放章节名
        self.urls = []  # 存放章节链接
        self.nums = 0  # 章节数
        self.fails = []
        self.fail_names = []
        self.fail_indexs = []

    def get_download_url(self):
        self.driver.get(self.target)
        html = self.driver.page_source
        div_bf = BeautifulSoup(html, "html5lib")
        div = div_bf.find_all('div', id='list')
        a_bf = BeautifulSoup(str(div[0]), "html5lib")
        a = a_bf.find_all('a')
        self.nums = len(a)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~章节列表~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(a)
        time.sleep(random.randint(6, 10))  # 设置休息时间
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target_index):
        try:
            self.driver.get(self.urls[target_index])
            time.sleep(random.randint(6, 10))  # 设置休息时间
            html = self.driver.page_source
            div_bf = BeautifulSoup(html, "html5lib")
            texts = div_bf.find_all('div', id='content')
            content_bf = BeautifulSoup(str(texts[0]), "html5lib")
            conts = content_bf.find_all('p')
            conts = conts[1:]  # 首行空白
            for i in range(len(conts)):
                conts[i] = str(conts[i])
                conts[i] = conts[i].replace('<p>', '')  # 去掉<p>
                conts[i] = conts[i].replace('</p>', '\n')  # 去掉</p>

            return conts[0:]

        except:
            self.fail_names.append(self.names[target_index])
            self.fails.append(self.urls[target_index])
            self.fail_indexs.append(target_index)
            print('出错了')
            print(target_index)
            print(self.names[target_index])
            print(self.urls[target_index])
            return ['   出错了']

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    path = 'C:/Users/admin/PycharmProjects/PaChongXiaoShou/33yq/contents/'
    file_name = '偷偷养只小金乌'
    file_path = path + file_name + '.txt'
    if os.path.exists(file_path):
        print('文件存在，重命名')
        file_path = path + file_name + '-' + str(time.time()) + '.txt'

    chromedriver_autoinstaller.install()
    contents = []
    dl = downloader()
    dl.get_download_url()
    for i in range(dl.nums):
        cont = dl.get_contents(i)
        contents.append(cont)
        # dl.writer(dl.names[i], file_path, dl.get_contents(i))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~下载失败章节和链接~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(dl.fail_indexs)
    print(dl.fail_names)
    print(dl.fails)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~正在尝试重新下载~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~正在尝试重新下载~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~正在尝试重新下载~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    old_fail_indexs = dl.fail_indexs.copy()
    rt_fail_indexs = []
    rt_fail_names = []
    rt_fail_urls = []
    for i in old_fail_indexs:
        cont = dl.get_contents(i)
        if cont == ['   出错了'] or cont[0] == '   出错了':
            rt_fail_indexs.append(i)
            rt_fail_names.append(dl.names[i])
            rt_fail_urls.append(dl.urls[i])
        contents[i] = cont.copy()

    for i in range(len(contents)):
        dl.writer(dl.names[i], file_path, contents[i])

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~再次下载失败章节和链接~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(rt_fail_indexs)
    print(rt_fail_names)
    print(rt_fail_urls)
    print('~~~~~~~~~~~~~~~~~~~~~~~下载完成~~~~~~~~~~~~~~~~~~~~~~~')



