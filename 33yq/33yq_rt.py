# -*- coding:UTF-8 -*-

import time
import os
import random
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def writer(name, path, text):
    write_flag = True
    with open(path, 'a', encoding='utf-8') as f:
        f.write(name + '\n')
        f.writelines(text)
        f.write('\n\n')


if __name__ == '__main__':
    path = 'C:/Users/admin/PycharmProjects/PaChongXiaoShou/33yq/contents/'
    file_name = '混在洪武当咸鱼'
    file_path = path + file_name + '-补充.txt'
    if os.path.exists(file_path):
        print('文件存在，重命名')
        file_path = path + file_name + '-' + str(time.time()) + '.txt'

    chromedriver_autoinstaller.install()
    options = Options()
    options.page_load_strategy = 'eager'  # 页面加载策略 normal eager none
    driver = webdriver.Chrome(options=options)
    contents = []
    names = ['第三百零一章 你吕家的报应到了！', '第三百六十七章 这两个混账！', '第三百九十四章 咱让你抓你就抓啊！',
             '第四百三十六章 我宁愿让那地方荒着！']
    urls = ['https://www.33yq.org/read/138923/84801991.shtml', 'https://www.33yq.org/read/138923/88259471.shtml',
            'https://www.33yq.org/read/138923/89310641.shtml', 'https://www.33yq.org/read/138923/90602848.shtml']

    fail_names = []
    fail_urls = []

    for i in range(len(urls)):
        try:
            driver.get(urls[i])
            time.sleep(random.randint(6, 10))  # 设置休息时间
            html = driver.page_source
            div_bf = BeautifulSoup(html, "html5lib")
            texts = div_bf.find_all('div', id='content')
            content_bf = BeautifulSoup(str(texts[0]), "html5lib")
            conts = content_bf.find_all('p')
            conts = conts[1:]  # 首行空白
            for cont_index in range(len(conts)):
                conts[cont_index] = str(conts[cont_index])
                conts[cont_index] = conts[cont_index].replace('<p>', '')  # 去掉<p>
                conts[cont_index] = conts[cont_index].replace('</p>', '\n')  # 去掉</p>
            contents.append(conts)

        except:
            fail_names.append(names[i])
            fail_urls.append(urls[i])
            print('出错了')
            print(names[i])
            print(urls[i])

    for i in range(len(contents)):
        writer(names[i], file_path, contents[i])

    print('~~~~~~~~~~~~~~~~~~~~~~~~~结束补充下载~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~失败的章节名和链接~~~~~~~~~~~~~~~~~~~~~~~')
    print(fail_names)
    print(fail_urls)
