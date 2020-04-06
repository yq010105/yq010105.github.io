---
title: Python学习中遇到的问题
date: 2020-02-04 23:01:44
summary: Python的一些问题，包括bug，还有编辑器的使用问题等等
categories: 无力
tags:
  - Python
  - Questions
---

<!--more-->

# 1. 新版 pycharm 问题

**使用 Pycharm 遇到的问题**
_VS code 天下第一_

## 问题 1：pycharm 双击打不开

已解决：可能时进程中已经有了 pycharm，在任务管理器里结束进程，然后重新打开

## 问题 2：pycharm 打开后回有两个窗口，而且不能再窗口上操作

重装可以解决，但不知道什么原因，猜测可能是打开文件太多，加载不了

# 2. Python的一些BUG

写程序用一分钟，找BUG需要一天

## 2.1 class传参的一些问题

*takes 2 positional arguments but 30 were given*
大概就是只需要两个位置参数，但是我给了30个，`黑人问号？？？`

就是这个程序， 主要就是用多线程来爬取图片，然后到第二部，获得子页面的图片url资源地址时出错，无法解决

```python
import threading
import time
import requests
import lxml.html
import re
import os
from multiprocessing import Pool

# 创建 Thread 的子类
class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def getresult(self):
        return self.result

# 创建爬取图片的类
class WallGet(object):
    def __init__(self, headers, pages):
        self.headers = headers
        self.pages = pages

    # 很快就完了
    def get_url(self):
        pages = self.pages
        url_pics = []
        page = 1
        while page <= int(pages):
            url = 'https://wallhaven.cc/search?categories=010&purity=100&resolutions=1280x800&sorting=relevance&order=desc&page=' + \
                str(page)
            html = requests.get(url, headers=self.headers).content.decode()
            selector = lxml.html.fromstring(html)

            url_pic = selector.xpath(
                '//*[@id="thumbs"]/section/ul/li/figure/a/@href')
            url_pics.append(url_pic)
            page += 1
        urls = []
        for url_pic in url_pics:
            for url in url_pic:
                urls.append(url)
        return urls

    # 单个图片url的获取
    def get_picurl(self, url):
        html2 = requests.get(url, headers=self.headers).content.decode()
        img_url = re.findall(r'"wallpaper" src="(.*?)"', html2, re.S)[0]
        print(img_url)
        return img_url

    def down_img(self, imgurls):
        i = 1
        for imgurl in imgurls:
            print(f'下载图片第{i}张')
            try:
                pic = requests.get(imgurl, timeout=10)
            except requests.exceptions.ConnectionError:
                print('图片无法下载')
                continue
            except requests.exceptions.ReadTimeout:
                print('requests.exceptions.ReadTimeout')
                continue

            main_path = r'E:\\wallhaven\\'
            if not os.path.exists(main_path):
                os.makedirs(main_path)

            dir = 'E:\\wallhaven\\' + str(i) + '.jpg'

            with open(dir, 'wb') as f:
                f.write(pic.content)
            i += 1

# 运行主程序
def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}
    pages = input('输入要多少页： ')
    wallget = WallGet(headers, pages)
    urls = wallget.get_url()
    print('每页图片链接获取完成')
    print(urls)
    
    # 调试的时候这句话出现问题
    # th = MyThread(wallget.get_picurl,(urls[0]))
    # th.start()
    # 同样，直接用也会出现问题
    th2 = threading.Thread(target= wallget.get_picurl,args=(urls[0]))
    th2.start()
    # print(th.getresult())
    exit()


    l = []
    for url in urls:
        th = MyThread(wallget.get_picurl, (url))
        th.start()
        l.append(th)

    for i in l:
        i.join()
    
    print('图片url资源地址获取完成')
    print()

if __name__ == "__main__":
    main()
```

*出错提示信息*

```c
Exception in thread Thread-1:
Traceback (most recent call last):
  File "D:\py\lib\threading.py", line 917, in _bootstrap_inner
    self.run()
  File "D:\py\lib\threading.py", line 865, in run
    self._target(*self._args, **self._kwargs)
TypeError: get_picurl() takes 2 positional arguments but 30 were given
```