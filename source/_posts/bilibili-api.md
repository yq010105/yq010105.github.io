---
title: Bilibili_Api
date: 2020-02-14 14:31:32
tags:
  - Python
---

**bilibili 提供的 api 接口(一串 json 字符)**
_让基于 bilibili 的开发更简单_

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
