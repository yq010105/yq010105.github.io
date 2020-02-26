---
title: Spider Example
date: 2020-02-10 16:43:47
top: true
coverImg: /img/cover/spiderex.jpg
img: /img/cover/spiderex.jpg
categories: 技术力
summary: 自己动手编写的几个python爬虫小栗子
cover: true
tags:
  - Spider
  - Python
---

> **自己动手做的 python 爬虫**&emsp;&emsp;&emsp;[GitHub 链接](https://github.com/yq010105/spider_learn "github")
> WARNING :逻辑混乱，语法不顺！！！

<!-- more -->

# 1. 爬取 bilibili 每日排行榜数据

- **使用 XPath 爬取,并将数据保存到 csv 文件中**
- **文件名使用该排行榜所在时间段**

```python
import requests
import csv
import lxml.html

url = 'https://www.bilibili.com/ranking/'
html = requests.get(url).content.decode()
# print(html)

selector = lxml.html.fromstring(html)

title = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/a/text()')
# print(len(title))

link = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[1]/a/@href')
# print(link[0])
# cover = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[1]/a/div/img/@src')
# print(cover[0])

up_name = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/a/span/text()')
# print(up_name[5])
up_videoplay = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/span[1]/text()')

time = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[2]/div/span/text()')
time_num = time[0]
str1 = time_num.replace(' 的数据综合得分，每日更新一次','')
str2 = str1.replace('统计所有投稿在 ','')
time_num2 = str2

headers = ['up_name','title','link']
rows = []
for i in range(100):
    rows.append([up_name[i],title[i],link[i]])

with open(f'{time_num2}.csv','w',encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
```

- **csv 部分展示**
  `2020年02月07日 - 2020年02月10日`
  ![bilibili_csv](/img/bilibili_csv.png)

# 2. 爬取 baidu 上搜到的图片(初级)

## 2.1 thumbURL

- _分辨率极低_

```py
import re
import requests
import os

def download(html):
    #通过正则匹配
    pic_url = re.findall('"thumbURL":"(.*?)",',html, re.S)
    i = 1
    for key in pic_url:
        print("开始下载图片："+key +"\r\n")
        try:
            pic = requests.get(key, timeout=10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        #保存图片路径
        main_path="E:/baidu/" #文件保存路径，如果不存在就会被重建
        if  not os.path.exists(main_path):#如果路径不存在
            os.makedirs(main_path)
        dir = "E:/baidu/" + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
def main():
        url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=result&pos=history&word=siyueshinide'
        result = requests.get(url)
        download(result.text)


if __name__ == '__main__':
        main()
```

## 2.2 objURL

_分辨率较高，但有的图爬不了_

```py
import re
import requests
import os
import json

def download(html):
    #通过正则匹配
    pic_url = re.findall('"objURL":"(.*?)",',html, re.S)
    # for pic_url_li in pic_url:
        # pic_url_js = '{'+'"link"'+':' +pic_url_li+'}'
        # pic_url_py = json.loads(pic_url_li)
    # print(pic_url)
    # exit()
    i = 1
    for key in pic_url:
        print("开始下载图片："+key +"\r\n")
        try:
            pic = requests.get(key, timeout=10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        except requests.exceptions.ReadTimeout:
            print('requests.exceptions.ReadTimeout')
            continue
        #保存图片路径
        main_path="E:/baidu/" #文件保存路径，如果不存在就会被重建
        if  not os.path.exists(main_path):#如果路径不存在
            os.makedirs(main_path)
        dir = "E:/baidu/" + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
def main():
        url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=result&pos=history&word=siyueshinide'
        result = requests.get(url)
        download(result.text)


if __name__ == '__main__':
        main()
```

## 2.3 baidu 面向对象

- 输入想爬取的关键词，自动爬取(只能下 30 张)

```py
import requests
import re
import os


def get_id(search_id):
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + search_id
    return url

def get_obj():
    url = get_id(search_id)
    html = requests.get(url).content.decode()
    obj_URL = re.findall('"objURL":"(.*?)",',html,re.S)
    return obj_URL

def save_pic():
    obj_url = get_obj()
    i = 1
    for objurl in obj_url:
        print('开始下载图片'+'\t'+'第'+str(i)+'张')
        try :
            pic = requests.get(objurl,timeout = 10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        except requests.exceptions.ReadTimeout:
            print('requests.exceptions.ReadTimeout')
            continue
        global search_id
        main_path = r'E:\learn\py\git\spider\spider_learn\baidu\pic\\' + search_id +'\\'
        if not os.path.exists(main_path):
            os.makedirs(main_path)
        dir = "E:\learn\py\git\spider\spider_learn\\baidu\pic\\" +search_id +'\\'+ search_id+ str(i) + '.jpg'
        with open(dir,'wb') as f:
            f.write(pic.content)
        i += 1


if __name__ =='__main__':
    search_id = input('请输入要下载的内容:')
    save_pic()
```

## 2.4 baidu_more

- **进一步升级，可以爬任意数量图片**

```py
import requests
import re
import os
from multiprocessing.dummy import Pool


def get_urls(search_id):
    total = (input('请输入要几页----30张一页----：'))
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + search_id+ '&pn='
    t = 0
    URLS = []
    while t < int(total)*30:
        URL = url + str(t)
        t = t + 30
        URLS.append(URL)
    return URLS

def get_obj(url):
    html = requests.get(url).content.decode()
    obj_URL = re.findall('"objURL":"(.*?)",',html,re.S)
    return obj_URL

def save_pic():
    pool=Pool(5)
    objurls = pool.map(get_obj,URLS)
    i = 1
    for objurl in objurls:
        for obj in objurl:
            print('开始下载图片'+'\t'+'第'+str(i)+'张')
            try :
                pic = requests.get(obj,timeout = 10)
            except requests.exceptions.ConnectionError:
                print('图片无法下载')
                continue
            except requests.exceptions.ReadTimeout:
                print('requests.exceptions.ReadTimeout')
                continue
            global search_id
            main_path = patha +'\\' + search_id +'\\'
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            dir = main_path + search_id+ str(i) + '.jpg'
            with open(dir,'wb') as f:
                f.write(pic.content)
            i += 1


if __name__ =='__main__':
    search_id = input('请输入要下载的内容:')
    URLS = get_urls(search_id)
    patha = input('输入文件保存路径----示例:E:\\baidu----:')
    save_pic()
```

# 3. 爬取 ins 上的图片(初级版)

- _分辨率低_

```python
import requests
import json
import lxml.html
import re
import os

# 获取src
def get_src():
    url = 'https://www.instagram.com/baaaakuuuu'
    html = requests.get(url).content.decode()
    selector = lxml.html.fromstring(html)
    script = selector.xpath('/html/body/script[1]/text()')[0].strip()
    # print(script)
    # print(type(script))       #str
    # exit()
    # for script_in in script :
        # try:
        #     script_dic = json.loads(script_in)
        # print(script_dic)
    src = re.findall(r'"thumbnail_resources":\[(.*?)\]',script,re.S)
    # print(src[0]) #str
    # print(type(src[0]))
    # exit()
    return src

# 获取图片链接
def get_picurl():
    src = get_src()
    # print(src)
    # exit()
    pic_url_lst = []
    for src_ls in src :         #"config_height":480},{ ... ,"config_width":640,"config_height":640}
        thumb = re.findall(r'"config_height":480},{(.*?),"config_width":640,"config_height":640}',src_ls)[0]
        thumb_json = '{' + thumb + '}'
        # print(thumb_json)
        # exit()
        thumb_py = json.loads(thumb_json)
        pic_url = thumb_py['src']
        # print(pic_url)
        # exit()
        pic_url_lst.append(pic_url)
    # print(pic_url_lst)
    # exit()
    return pic_url_lst


# 将图片链接保存
def save_pic():
    pic_url_lst = get_picurl()
    i = 1
    # print(pic_url_lst)
    # exit()
    for pic_con in pic_url_lst:
        # print(pic_con)
        # exit()
        try:
            pic = requests.get(pic_con, timeout=10)
            main_path = 'E:/ins/'
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            path = 'E:/ins/' + 'baku' + str(i) + '.jpg'
            with open(path,'wb') as f:
                f.write(pic.content)
                print(f'第{i}张已下载')
            i +=1
        except requests.exceptions.ConnectionError:        #requests.exceptions.ConnectionError
            print('图片无法下载')
            continue
    return

save_pic()
```

**学习如何爬取高分辨率图片 ing**
