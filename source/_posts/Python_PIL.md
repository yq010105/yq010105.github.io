---
title: Python中PIL库的学习
top: false
cover: false
date: 2020-03-31 22:08:08
toc: true
categories: 学习力
tags:
    - Python
summary: 学习Python中的PIL库，慢慢学
password:
---

<!--more-->

# 0. 零散的知识

## 0.1 截取电脑屏幕

*从左上角开始截取，获得八张图片的简单例子*

```python
from PIL import ImageGrab

for i in range(1,9):
    j = i * 50
    im = ImageGrab.grab((0,0,j,j))
    # im.show()
    im.save('E:/learn/py/PIL/'+str(i)+'.jpg','JPEG')
```