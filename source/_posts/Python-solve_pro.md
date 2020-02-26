---
title: Python_solve_problems
date: 2020-02-17 17:09:35
summary: 用python模拟学习生活中遇到的问题，便于解决理解，大部分可能都是学概率统计的时候遇到的问题
categories: 技术力
tags:
  - Python
  - Questions
---

**这篇主要是记录一些生活学习中遇到的一些难题,想不通,就用 python 模拟出来**
_虽然模拟出来了，但不会有可能还是不会 hhh_

<!--more-->

# 1. 概率类问题

## 1.1 一道小题，材料力学老师引出

_24 个朋友生日问题_

```
一年中同一天收到2个或2个以上朋友生日聚会邀请的概率
A 、小于10%  B、20%  C、40%  D、大于50%
```

_将其大致概括就是：身边有 24 个朋友，他们中有两个人或两个以上的人同一天生日的概率是多少_
**为了简单，就只算两个人生日相同的概率**

```py
import random

def get_same():
    ris = []
    for i in range(24):  # 24个人，生成24个随机数
        ri = random.randint(1, 365)  # 随机数范围则是一年365天
        ris.append(ri)

    d = 0
    for j in range(24):     # 循环来比较随机数
        for k in range(j+1, 24):
            if ris[j] == ris[k]:
                d += 1
                # print(ris[k])
            else:
                continue
    return d        # 如果有相同，不管有几个，d都不是0
    # 即如果d=0，说明这24个人里无同一天生日

def get_gailv():
    su = 0      # 总次数
    suancal = 0  # 无相同，即d=0的次数
    for h in range(0, 10000):   # 10000次
        # print(h)
        suan = get_same()
        if suan == 0:   # 如果suan为0，说明生日都不同
            suancal = suancal + 1
        su += 1
    return suancal/su    # 24 人生日都不同的概率

gailvs = []
for j in range(10):     # 重复10次获得概率
    gailv = get_gailv()
    gailvs.append(gailv)
print(gailvs)
```

**结果为**
**[0.4609, 0.4626, 0.4719, 0.4608, 0.4528, 0.4607, 0.467, 0.4575, 0.4549, 0.4577]**

_可以发现没有超过 0.5 的概率，说明生日都不相同的概率是大于 0.5 的，也就是说这 24 个人有超过 50%的概率是有两个或两个以上生日是同一天的_
**接下来分析原因：**
不难猜想出，如果只有两个人，这两个人生日同一天概率很小，随着人数的增多，出现生日相同的概率越来越大
可以反过来思考，计算每个人生日都不同的概率
两个人不同：364/365
三个人不同：364/365 _ 363/365
四个人不同：364/365 _ 363/365 \* 362/365
以此类推：当 24 个人生日不同时的概率：

```py
total = 1
j = 365
ren = int(input('请输入人数：'))    # 24人
for i in range(ren-1):
    j = j - 1
    total = j * total

fenmu = 365 ** (ren-1)
print(total/fenmu) # 0.4616557420854712
```

可以计算出概率为 0.46，即可以得出有两人或两人以上的概率为 0.54
