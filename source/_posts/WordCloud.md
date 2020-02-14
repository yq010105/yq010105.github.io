---
title: WordCloud
date: 2020-02-13 20:23:53
tags:
  - Python
---

- **wordcloud 一个可以生成词云的 python 包**
  <!--more-->

# 1. wordcloud 代码(英文)

```py
from wordcloud import WordCloud
import PIL .Image as image
import numpy as np # 自定义图片

dir = './bi.txt'

with open(dir) as fp:
    text = fp.read()
    # print(text)
    # exit()
    mask = np.array(image.open('F:\download\\1.png'))   #自定义词云形状
    WordCloud = WordCloud(
        mask = mask,
    ).generate(text)
    image_produce = WordCloud.to_image()
    image_produce.show()        #  生成的文件在：C:\Users\20180\AppData\Local\Temp\jieba.cache中
```

# 2. wordcloud 代码实现(中文)

- **jieba 库**

```py
from wordcloud import WordCloud
import PIL .Image as image
import numpy as np # 自定义图片
import jieba # 中文

def trans_cn(text):
    word_list = jieba.cut(text)
    result = ' '.join(word_list)
    return result

dir = './bi.txt'

with open(dir) as fp:
    text = fp.read()
    # print(text)
    # exit()
    text = trans_cn(text)
    mask = np.array(image.open('F:\download\\1.png'))
    WordCloud = WordCloud(
        mask = mask,
        font_path ='C:\\windows\\Fonts\\msyh.ttc'
    ).generate(text)
    image_produce = WordCloud.to_image()
    image_produce.show()
```

> 参考[简书网站](https://www.jianshu.com/p/c986f5017ca7)

# 3. 将 python 词云生成的图片保存下来

```py
import jieba

from wordcloud import WordCloud


with open("./bi.txt") as fp:
    txt = fp.read()  # 读取文本

words = jieba.lcut(txt)  # 精确分词

nextword = ' '.join(words)    #空格连接字符

wordshow = WordCloud(background_color='white',
                     width=800,
                     height=800,
                     max_words=800,
                     max_font_size=100,
                     font_path="msyh.ttc",    #用微软雅黑作为字体显示效果

                     ).generate(nextword)

wordshow.to_file('bilibili_rank.png')  #转换成图片
```

> [参考网站](https://blog.csdn.net/qq_41709494/article/details/89213176)
