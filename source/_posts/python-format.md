---
title: Python_format
date: 2020-02-11 20:56:10
tags:
    - Python
---
**Python_format&emsp;&emsp;&emsp;一种格式化字符串函数`str.format()`**
>参考教程[网站](https://www.runoob.com/python/att-string-format.html)和[CSDN](https://blog.csdn.net/qq_19691995/article/details/84197252)
<!--more -->

# python_format
str.format()，它增强了字符串格式化的功能。
基本语法是通过 {} 和 : 来代替以前的 % 。

## format 函数可以接受不限个参数，位置可以不按顺序
```py
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
```

## 设置参数
```py
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

'''
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
'''
```

通过字典和列表的另一种写法
```py
>>> hash = {'name':'hoho','age':18}
>>> 'my name is {name},age is {age}'.format(**hash)        #**dict
'my name is hoho,age is 18'

>>> li = ['hoho',18]
>>> 'my name is {} ,age {}'.format(*li)               #*[]迭代列表
'my name is hoho ,age 18'
```

## 向`str.format`传入对象
```py
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

# value 为: 6
```

## 数字格式化
```py
>>> print("{:.2f}".format(3.1415926));
3.14
```
|数字|格式|输出|描述|
|:----:|:----:|:----:|:----:|
|3.1415926|	{:.2f}|	3.14|	保留小数点后两位|
|3.1415926	|{:+.2f}	|+3.14	|带符号保留小数点后两位|
|-1	|{:+.2f}|-1.00	|带符号保留小数点后两位|
|2.71828	|{:.0f}|	3	|不带小数|
|5	|{:0>2d}	|05|	数字补零 |(填充左边, 宽度为2)|
|5	|{:x<4d}|	5xxx|	数字补x (填充右边, 宽度为4)|
|10	|{:x<4d}	|10xx|	数字补x (填充右边, 宽度为4)|
|1000000|	{:,}|	1,000,000	|以逗号分隔的数字格式|
|0.25|	{:.2%}	|25.00%|	百分比格式|
|1000000000	|{:.2e}|	1.00e+09	|指数记法|
|13	|{:>10d}|	        13|	右对齐 (默认, 宽度为10)|
|13	|{:<10d}	|13	|左对齐 (宽度为10)|
|13	|{:^10d}	|    13|	中间对齐 (宽度为10)|
|11|'{:b}'.format(11)  |1011|进制|     
||'{:d}'.format(11)|11||
||'{:o}'.format(11)|13||
||'{:x}'.format(11)|b||
||'{:#x}'.format(11)|0xb||
||'{:#X}'.format(11)|0XB||

- **^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充**
- **+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格**
- **b、d、o、x 分别是二进制、十进制、八进制、十六进制**

## 此外还可以用大括号 {} 来转义大括号
`print ("{} 对应的位置是 {{0}}".format("runoob"))`
*结果为*：**runoob 对应的位置是 {0}**