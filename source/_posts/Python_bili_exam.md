---
title: Python_Bilibili_Api
date: 2020-02-14 14:31:32
summary: 用bilibili提供的api基于python做出的几个小栗子，获取信息
categories: 技术力
tags:
  - Python
  - Bilibili
---

**bilibili 提供的 api 接口(一串 json 字符)**
_让基于 bilibili 的开发更简单_
**我基于 python 写的几个使用 api 获取信息的例子**

<!--more-->

# 1. bilibili 用户基本信息(name，level，关注，粉丝)获取

`https://api.bilibili.com/x/space/upstat?mid=UUID&jsonp=jsonp`_up 信息，名字，等级，视频总播放量，文章总浏览数_
`https://api.bilibili.com/x/relation/stat?vmid=UUID&jsonp=jsonp`_up 信息，关注数，黑名单，粉丝数_

**简单的代码获取 up 信息**

```py
import json
import requests

mid = input('输入要查询的up的uid：')
url_space = 'https://api.bilibili.com/x/space/acc/info?mid=' + mid
url_relation = 'https://api.bilibili.com/x/relation/stat?vmid='+mid
space = requests.get(url_space).content.decode()
relation =requests.get(url_relation).content.decode()
# print(type(html))
dict_space = json.loads(space)
dict_rela = json.loads(relation)
# print(dict)
up_name = dict_space["data"]["name"]
up_level = dict_space['data']['level']

up_following_num = dict_rela['data']['following']
up_follower_num = dict_rela['data']['follower']

print(f'up名字是:{up_name}')
print(f'up等级达到:{up_level}级')
if int(up_level)>=5:
    print('----哇是个大佬！！！----')
print(f'up关注了{up_following_num}个人')
if int(up_following_num)>=700:
    print('----铁定是个dd！！！----')
print(f'up有{up_follower_num}个粉丝')
```

**示例：**

```py
输入要查询的up的uid：2
up名字是:碧诗
up等级达到:6级
----哇是个大佬！！！----
up关注了191个人
up有804598个粉丝
```

# 2. bilibili 统计某视频评论区，并生成词云

- **获取某视频评论区评论**

```py
import json
import requests
from multiprocessing.dummy import Pool
import re
import os

av = input('请输入视频的av号:')
p_total = input('请输入评论要几页:')

def get_urls():
    urls = []
    p = 1
    while p <= int(p_total):
        url = 'http://api.bilibili.com/x/v2/reply?jsonp=jsonp&;pn=' + str(p) + '&type=1&oid=' + av
        urls.append(url)
        p += 1
    return urls

def get_name_con(url):
    html = requests.get(url).content.decode()
    yh_names = re.findall(r'"uname":"(.*?)","sex":',html,re.S)
    yh_contents = re.findall(r'"message":"(.*?)","plat"',html,re.S)
    del yh_contents[0]
    yh_contents2 = []
    for yh_content in yh_contents:
        yh_contents2.append(yh_content.replace('\\n',' '))
    # print(yh_contents2)
    # exit()
    return yh_names,yh_contents2

def get_names_cons():
    pool = Pool(5)
    urls = get_urls()
    namecons = pool.map(get_name_con,urls)
    names = []
    cons = []
    for namecon in namecons:
        name = namecon[0]
        for n in name :
            names.append(n)
        con = namecon[1]
        for c in con:
            cons.append(c)
    return names,cons

def save():
    tumple = get_names_cons()
    namelst = tumple[0]
    conlst = tumple[1]
    # print(len(conlst))
    # # print(type(namelst))
    # print(len(namelst))
    # exit()
    if len(namelst) != len(conlst):
        tot = len(conlst)
    g = 0
    main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\txt' #修改路径-自定义
    if not os.path.exists(main_path):
        os.makedirs(main_path)

    dir1 = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\txt\\' + 'comment'  + '.txt'  # 自定义文件名
    with open(dir1,'w',encoding='utf-8') as fb:
        for g in range(tot):
            # fb.write(namelst[g])
            # fb.write('\t\t\t')
            fb.write(conlst[g])
            # fb.write('\n')
            g += 1

if __name__ == '__main__':
    save()
    print('----已完成----',end='\t')
    print(f'此视频已获得 {p_total} 页的评论')
```

- **将生成的评论 txt 文件统计为词云**

```py
from wordcloud import WordCloud
import PIL .Image as image
import jieba

def trans_cn(text):
    word_list = jieba.cut(text)
    result = ' '.join(word_list)
    return result

def wc():
    dir1 = './txt/comment.txt'
    with open(dir1,encoding='utf-8') as f:
        text = f.read()
        text = trans_cn(text)
        WordCloud2 = WordCloud(
            font_path = 'C:\\windows\\Fonts\\simfang.ttf'
        ).generate(text)
        image_produce = WordCloud2.to_image()
        image_produce.show()
        WordCloud2.to_file('./txt/comment.png')

wc()
```

**示例：av2**
![图片示例](/img/bilibili/comment.png)

# 3. 获取 bilibili 主页各个分区的视频封面和 av 号

`https://www.bilibili.com/index/ding.json`_首页 api，每刷新一次，信息就会改变一次_
_获取的视频信息也就不同，所以可以一直获取信息(理论上来说)_
_缺点是每次只能获取十张图片信息_
_用的是 wb 写入文件，所以即使文件有一样的也会被覆盖..._

```py
import requests
import re
import os
import json

print('-douga-teleplay-kichiku-dance-bangumi-fashion-life-ad-guochuang-movie-music-technology-game-ent--')
fenqu = input('请输入爬取分区:')
if fenqu == '':
    fenqu1 = 'shuma'
else :
    fenqu1 = fenqu

html = requests.get(
    'https://www.bilibili.com/index/ding.json').content.decode()

dict_html = json.loads(html)
i = 0
aids = []
pics = []

for i in range(10):
    aid = dict_html[fenqu][str(i)]['aid']
    pic = dict_html[fenqu][str(i)]['pic']
    aids.append(aid)
    pics.append(pic)

j = 1
h = j-1
for h in range(10):
    main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\pic\\'+fenqu1
    if not os.path.exists(main_path):
        os.makedirs(main_path)
    try:
        piccc = requests.get(pics[h])
    except requests.exceptions.ConnectionError:
        print('图片无法下载')
        continue
    except requests.exceptions.ReadTimeout:
        print('requests.exceptions.ReadTimeout')
        continue
    dir = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\pic\\' + \
         fenqu1 + '\\'  +'av' + str(aids[h]) + '.jpg'
    with open(dir, 'wb') as f:
        print(f'正在爬取第{j}张图')
        f.write(piccc.content)
    j += 1
    h += 1

print('----完成图片爬取----')
```

_略微修改后_
_可能就是因为有重复的，会覆盖前面已下载的_
_爬个 5 次本该有 50 张，但才有 20 几张(dance 区)_
_可能 dance 区首页视频比较少吧，游戏区很多_
**不管了反正这个爬虫也没什么用 hhh**

```py
import requests
import re
import os
import json

def get_pic():
    if fenqu == '':
        fenqu1 = 'shuma'
    else :
        fenqu1 = fenqu

    html = requests.get(
        'https://www.bilibili.com/index/ding.json').content.decode()

    dict_html = json.loads(html)
    i = 0
    aids = []
    pics = []

    for i in range(10):
        aid = dict_html[fenqu][str(i)]['aid']
        pic = dict_html[fenqu][str(i)]['pic']
        aids.append(aid)
        pics.append(pic)

    j = 1
    h = j-1
    for h in range(10):
        main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\pic\\'+fenqu1
        if not os.path.exists(main_path):
            os.makedirs(main_path)
        try:
            piccc = requests.get(pics[h])
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        except requests.exceptions.ReadTimeout:
            print('requests.exceptions.ReadTimeout')
            continue
        dir = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\pic\\' + \
            fenqu1 + '\\'  +'av' + str(aids[h]) + '.jpg'
        with open(dir, 'wb') as f:
            print(f'正在爬取第{j}张图')
            f.write(piccc.content)
        j += 1
        h += 1

to = int(input('请输入你要爬多少次---一次最多十张：'))
print('-douga-teleplay-kichiku-dance-bangumi-fashion-life-ad-guochuang-movie-music-technology-game-ent--')
fenqu = input('请输入爬取分区:')
for i in range(to):
    get_pic()
    print(f'----完成第{i}次图片爬取----')
```

> [Github 源码链接](https://github.com/yq010105/spider_learn/tree/master/bilibili/bilibili_api)

# 4. 主站上的实时人数

_所用 api 接口_`https://api.bilibili.com/x/web-interface/online?&;jsonp=jsonp`

```py
import requests
import json
import time

def print_num():
    index = requests.get(
    'https://api.bilibili.com/x/web-interface/online?&;jsonp=jsonp').content.decode()
    dict_index = json.loads(index)
    all_count = dict_index['data']['all_count']
    web_online = dict_index['data']['web_online']
    play_online = dict_index['data']['play_online']
# 应该是人数和实时在线人数
    print(f'all_count:{all_count}')
    print(f'web_online:{web_online}')
    print(f'play_online:{play_online}')


for i in range(100):
    print(f'第{i+1}次计数')
    print_num()
    time.sleep(2)
```

# 5. 用户的粉丝数

_只能获取一页，b 站最多是五页，多了就会有限制_

```py
import requests
import json
import csv
import os
import time

uid = input('请输入查找的up主的uid:')
url = 'https://api.bilibili.com/x/relation/followers?vmid=' + \
    uid + '&ps=0&order=desc&jsonp=jsonp'

html = requests.get(url).content.decode()
dic_html = json.loads(html)

index_order = dic_html['data']['list']
mids, mtimes, unames, signs = [], [], [], []
for i in index_order:
    mid = i['mid']
    mids.append(mid)
    mtime = i['mtime']
    mmtime = time.asctime(time.localtime(mtime))
    mtimes.append(mmtime)
    uname = i['uname']
    unames.append(uname)
    sign = i['sign']
    signs.append(sign)
# print(index_order)
# print(mids)
headers = ['uid', '注册时间', 'up姓名', '个性签名']
rows = []
j = 0
for j in range(len(mids)):
    rows.append([mids[j], mtimes[j], unames[j], signs[j]])

main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\csv'
if not os.path.exists(main_path):
    os.makedirs(main_path)

dir = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\csv\\' + \
    'follers' + '.csv'

with open(dir, 'w', encoding='utf-8') as f:
    fb = csv.writer(f)
    fb.writerow(headers)
    fb.writerows(rows)


print('----最多只显示一页的粉丝数，也就是50个----')
print(f'共有{len(mids)}个粉丝')
```
