---
title: Python中schedule库的学习
top: false
cover: false
date: 2020-03-31 22:08:30
toc: true
categories: 学习力
tags: 
    - Python
summary: Python中的schedule库的使用
password:
---

<!--more-->

# 0. 零散的知识

## 0.1 定时截屏

>版权声明：本文为CSDN博主「欧阳不小辉」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明
>[原文链接](https://blog.csdn.net/a180736/java/article/details/79159859)

```python
import time 
import schedule
from PIL import ImageGrab 

c = 0 
def screen():
    im = ImageGrab.grab()        #截屏
    im.save('F:\python egs\Image\image/'+str(c)+'.jpg','JPEG') 

schedule.every(1).seconds.do(screen)#执行定时截屏

while True:                                 
        schedule.run_pending()
        c = c+1
        time.sleep(1)
```