---
title: Python中numpy库的学习
date: 2020-02-21 12:06:22
summary: Python中numpy轮子，用来处理数据
categories: 学习力
tags:
  - Python
---

<!--more-->

**函数引用，命名为 np：`import numpy as np`**

# 1. np.linspace()

**用来创建等差数列**

```py
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

start:返回样本数据开始点
stop:返回样本数据结束点
num:生成的样本数据量，默认为50
endpoint：True则包含stop；False则不包含stop
retstep：If True, return (samples, step), where step is the spacing between samples.(即如果为True则结果会给出数据间隔)
dtype：输出数组类型
axis：0(默认)或-1
```

eg:

```py
>>> np.linspace(2.0, 3.0, num=5)
array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
>>> np.linspace(2.0, 3.0, num=5, retstep=True)
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
```

> [原文链接](https://blog.csdn.net/Asher117/article/details/87855493)

# 2. np.arange()

**函数返回一个有终点和起点的固定步长的排列，如[1,2,3,4,5]，起点是 1，终点是 5，步长为 1**

- 1）一个参数时，参数值为终点，起点取默认值 0，步长取默认值 1
- 2）两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值 1
- 3）三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长。其中步长支持小数

```py
#一个参数 默认起点0，步长为1 输出：[0 1 2]
a = np.arange(3)

#两个参数 默认步长为1 输出[3 4 5 6 7 8]
a = np.arange(3,9)

#三个参数 起点为0，终点为3，步长为0.1 输出[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4 1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9]
a = np.arange(0, 3, 0.1)
```

> [原文链接](https://blog.csdn.net/qq_41550480/article/details/89390579)

# 3. np.random()

## 3.1 np.random.randint

low、high、size 三个参数。默认 high 是 None,如果只有 low，那范围就是[0,low)。如果有 high，范围就是[low,high)

```py
>>> np.random.randint(2, size=10)
array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])

>>> np.random.randint(1, size=10)
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

>>> np.random.randint(5, size=(2, 4))
array([[4, 0, 2, 1],
       [3, 2, 2, 0]])
```

> [原文链接](https://blog.csdn.net/weixin_42029738/article/details/81977492)

## 3.2 numpy.random.randn()与 rand()

- numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值
- numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中

```py

import numpy as np

arr1 = np.random.randn(2,4)
print(arr1)
print('******************************************************************')
arr2 = np.random.rand(2,4)
print(arr2)

'''
正负数都有
[[-1.03021018 0.5197033 0.52117459 -0.70102661]

[ 0.98268569 1.21940697 -1.095241 -0.38161758]]

******************************************************************
正数部分
[[ 0.19947349 0.05282713 0.56704222 0.45479972]

[ 0.28827103 0.1643551 0.30486786 0.56386943]]
'''
```

## 3.3 np.random.seed()

**seed( ) 用于指定随机数生成时所用算法开始的整数值**

- 1.如果使用相同的 seed( )值，则每次生成的随即数都相同
- 2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同
- 3.设置的 seed()值仅一次有效

![seed示例](/img/np/random_seed.webp)

## 3.4 np.random.normal([loc,scale,size])

正态(高斯)分布

```py
mu,sigma = 0,0.1
s = np.random.normal(mu,sigma,10)
print(s)
'''
 [-0.14154151 -0.04927673  0.01828343  0.05323477  0.05350814 -0.14129784
  0.06566983 -0.05441259 -0.01597307  0.16633013]
'''
```
