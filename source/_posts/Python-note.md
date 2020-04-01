---
title: Python-Note
date: 2020-02-09 15:38:38
summary: Python 语言学习笔记本
categories: 学习力
tags:
  - Python
  - Note
---

**有一定的 python 自学基础，基础不扎实**
**python，边学爬虫，边把不会的 python 知识不全**

<!-- more -->

# 1. 文件管理（txt）

```py
fd = open('file.txt','w',encoding='utf-8')      #utf-8 or GBK
fd.write(content)
fd.close()
```

其中 content 可以是字符串，变量，\t ......

<hr/>

|  r   |   w    |   a    |
| :--: | :----: | :----: |
| 只读 | 覆盖写 | 添加写 |

## 1.1 文件的readlines和readline

```python
f.readlines()# 全部读取最后返回一个列表存所有的类,每行后面都会带有“\n”
f.readline()# 读取一列数据
```


# 2. csv 文件

## 2.1 列表序列数据

- headers :表头
- rows :内容
- f*csv = csv.writer(f)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\_f 为 open('file.txt','w',encoding='utf-8')*
- f_csv.writerow(headers)
- f_csv.writerows(rows)

```py
import csv

headers = ['class','name','sex','height','year']

rows = [
        [1,'xiaoming','male',168,23],
        [1,'xiaohong','female',162,22],
        [2,'xiaozhang','female',163,21],
        [2,'xiaoli','male',158,21]
    ]

with open('test.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
```

_注意：如果打开 csv 文件出现空行的情况，那么需要添加一个参数 newline=”_
`with open('test.csv','w',newline='')as f:`

| class |   name    |  sex   | height | year |
| :---: | :-------: | :----: | :----: | :--: |
|   1   | xiaoming  |  male  |  168   |  23  |
|   1   | xiaohong  | female |  162   |  22  |
|   2   | xiaozhang | female |  163   |  21  |
|   2   |  xiaoli   |  male  |  158   |  21  |

## 2.2 字典序列数据

- headers :表头
- rows :内容
- f_csv = DictWriter(f,headers)
- f_csv.writeheader()
- f_csv.writerows(rows)

```py
import csv

headers = ['class','name','sex','height','year']

rows = [
        {'class':1,'name':'xiaoming','sex':'male','height':168,'year':23},
        {'class':1,'name':'xiaohong','sex':'female','height':162,'year':22},
        {'class':2,'name':'xiaozhang','sex':'female','height':163,'year':21},
        {'class':2,'name':'xiaoli','sex':'male','height':158,'year':21},
    ]

with open('test2.csv','w',newline='')as f:
    f_csv = csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
```

| class |   name    |  sex   | height | year |
| :---: | :-------: | :----: | :----: | :--: |
|   1   | xiaoming  |  male  |  168   |  23  |
|   1   | xiaohong  | female |  162   |  22  |
|   2   | xiaozhang | female |  163   |  21  |
|   2   |  xiaoli   |  male  |  158   |  21  |

## 2.3 csv 文件的读

```py
import csv
with open('test.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row)

'''result
['class', 'name', 'sex', 'height', 'year']
['1', 'xiaoming', 'male', '168', '23']
['1', 'xiaohong', 'female', '162', '22']
['2', 'xiaozhang', 'female', '163', '21']
['2', 'xiaoli', 'male', '158', '21']
'''

with open('test.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row[0])

'''result
class
1
1
2
2
'''
```

> 参考[网站](https://blog.csdn.net/katyusha1/article/details/81606175 "CSDN")

# 3. with open () as 读写文件

```py
# 读文件
with open('file.txt','r',) as f:
    print(f.read())
# 不需调用f.close()
# 如果文件过大则用read(size)比较保险
# 如果文件是配置文件readlines()较为方便


# 写文件
with open('file.txt','w',encoding='utf-8') as f:
    f.write('Hello World !')
# 文本文件    encoding 字符编码：gbk，utf-8
# 二进制文件  rb模式读取:图片,视频
```

> 参考[网站](https://blog.csdn.net/xrinosvip/article/details/82019844 "CSDN")

# 4. os 中创建文件夹

```py
import os

main_path = 'E:/os/'    #创建一个路径
if not os.path.exists(main_path):   #如果该路径不存在
    os.makedirs(main_path)  #则新建一个路径
```

**删除文件:**`os.remove(path)`

# 5. 将图片保存在文件夹中

```py
dir = '文件路径' + name +'.jpg'     #文件名
url_get = requests.get(url)         #从url中获取图片信息
with open(dir,'wb') as f:           #打开图片文件，保存图片信息
    f.writer(url_get.content)
```

# 6. try...except 语句

## 6.1 **语法**

```py
#python 异常处理
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
```

## 6.2 **使用 except 而不带任何异常类型**

```py
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
```

**以上方式 try-except 语句捕获所有发生的异常。但这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常**

## 6.3 **使用 except 而带多种异常类型**

```py
try:
    正常的操作
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
```

## 6.4 **try-finally 语句**

```py
try:
<语句>
finally:
<语句>    #退出try时总会执行
raise
```

## 6.5 **异常的参数**

```py
try:
    正常的操作
   ......................
except ExceptionType, Argument:
    你可以在这输出 Argument 的值...
```

## 6.6 **用户自定义异常**

- 通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自 Exception 类，通过直接或间接的方式
- 以下为与 RuntimeError 相关的实例,实例中创建了一个类，基类为 RuntimeError，用于在异常触发时输出更多的信息
- 在 try 语句块中，用户自定义的异常后执行 except 块语句，变量 e 是用于创建 Networkerror 类的实例

```py
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
```

- **在你定义以上类后，你可以触发该异常，如下所示：**

```py
try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args
```

|           异常名称            |                        描述                        |
| :---------------------------: | :------------------------------------------------: |
|         BaseException         |                   所有异常的基类                   |
|          SystemExit           |                   解释器请求退出                   |
|       KeyboardInterrupt       |             用户中断执行(通常是输入^C)             |
|           Exception           |                   常规错误的基类                   |
|         StopIteration         |                 迭代器没有更多的值                 |
|         GeneratorExit         |        生成器(generator)发生异常来通知退出         |
|         StandardError         |              所有的内建标准异常的基类              |
|        ArithmeticError        |               所有数值计算错误的基类               |
|      FloatingPointError       |                    浮点计算错误                    |
|         OverflowError         |                数值运算超出最大限制                |
|       ZeroDivisionError       |            除(或取模)零 (所有数据类型)             |
|        AssertionError         |                    断言语句失败                    |
|        AttributeError         |                  对象没有这个属性                  |
|           EOFError            |             没有内建输入,到达 EOF 标记             |
|       EnvironmentError        |                 操作系统错误的基类                 |
|            IOError            |                 输入/输出操作失败                  |
|            OSError            |                    操作系统错误                    |
|         WindowsError          |                    系统调用失败                    |
|          ImportError          |                 导入模块/对象失败                  |
|          LookupError          |                 无效数据查询的基类                 |
|          IndexError           |              序列中没有此索引(index)               |
|           KeyError            |                  映射中没有这个键                  |
|          MemoryError          |     内存溢出错误(对于 Python 解释器不是致命的)     |
|           NameError           |            未声明/初始化对象 (没有属性)            |
|       UnboundLocalError       |               访问未初始化的本地变量               |
|        ReferenceError         | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
|         RuntimeError          |                  一般的运行时错误                  |
|      NotImplementedError      |                   尚未实现的方法                   |
|      SyntaxError Python       |                      语法错误                      |
|       IndentationError        |                      缩进错误                      |
|         TabError Tab          |                     和空格混用                     |
|          SystemError          |                一般的解释器系统错误                |
|           TypeError           |                  对类型无效的操作                  |
|          ValueError           |                   传入无效的参数                   |
|     UnicodeError Unicode      |                     相关的错误                     |
|  UnicodeDecodeError Unicode   |                    解码时的错误                    |
|  UnicodeEncodeError Unicode   |                     编码时错误                     |
| UnicodeTranslateError Unicode |                     转换时错误                     |
|            Warning            |                     警告的基类                     |
|      DeprecationWarning       |               关于被弃用的特征的警告               |
|         FutureWarning         |           关于构造将来语义会有改变的警告           |
|        OverflowWarning        |        旧的关于自动提升为长整型(long)的警告        |
|   PendingDeprecationWarning   |              关于特性将会被废弃的警告              |
|        RuntimeWarning         |      可疑的运行时行为(runtime behavior)的警告      |
|         SyntaxWarning         |                  可疑的语法的警告                  |
|          UserWarning          |                 用户代码生成的警告                 |

> 参考[教程](https://www.runoob.com/python/python-exceptions.html)

# 7. python 小知识点

## 7.1 换行符 '\n' 和 回车符 '\r' 的区别？

```
换行符就是另起一新行，光标在新行的开头；
\n
回车符就是光标回到一旧行的开头；(即光标目前所在的行为旧行)
\r
在解析文本或其他格式的文件内容时，常常要碰到判定回车式换行的地方
这个时候就要注意既要判定"\r\n"又要判定"\n"。
```

## 7.2 Python 中 import, from...import,import...as 的区别

```py
import datetime
print(datetime.datetime.now())
```

以上代码实现输出系统当前时间，是引入整个 datetime 包，然后再调用 datetime 这个类中的 now()方法

```py
from datetime import datetime
print(datetime.now())
```

这里是从 datetime 包中只导入 datetime 这个类，让后再调用 datetime 这个类中的 now()方法实现同样的目的

```py
import datetime as dt
print(dt.datetime.now())
```

假如你嫌 datetime 这个包名称太长，想要给它取个别名，以后每次用到它的时候都用它的别名代替它，这时就需要用到 import…as

## 7.3 Python 中[ : n]、[m : ]、[-1]、[:-1]、[::-1]、[2::-1]和[1:]的含义

```py
[m : ] 代表列表中的第m+1项到最后一项

[ : n] 代表列表中的第一项到第n项



import numpy as np
a=[1,2,3.4,5]
print(a)
[ 1 2 3 4 5 ]

print(a[-1])     取最后一个元素
结果：[5]

print(a[:-1])     除了最后一个取全部
结果：[ 1 2 3 4 ]

print(a[::-1])     取从后向前（相反）的元素
结果：[ 5 4 3 2 1 ]

print(a[2::-1])     取从下标为2的元素翻转读取
结果：[ 3 2 1 ]

print(a[1:])     取第二个到最后一个元素
结果：[2 3 4 5]
```

## 7.4 python 浮点数保留几位小数

```py
a = 5.026

b = 5.000

round(a,2)
# 5.03

round(b,2)
# 5.0

'%.2f' % a
# '5.03'

'%.2f' % b
# '5.00'

float('%.2f' % a)
# 5.03

float('%.2f' % b)
# 5.0
```

# 8. python 中陌生的函数

_自己还不太熟悉的_

## 8.1 `str.split()` **对字符串进行切片--返回一个列表**

- 语法`str.split(str="", num=string.count(str)).`

* str：分隔符，默认为所有的空字符，包括空格、换行、指标
* num：分割次数，默认为-1，即分割所有

```py
# example
txt = "Google#Runoob#Taobao#Facebook"

# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)

print(x)         #['Google', 'Runoob#Taobao#Facebook']
```

> 参考教程：[RUNOOB](https://www.runoob.com/python/att-string-split.html "runoob.com")

## 8.2 `str.find()` **检测字符串中是否包含子字符串 str**

- _如果包含子字符串返回开始的索引值，否则返回-1_

* 语法`str.find(str, beg=0, end=len(string))`
* str -- 指定检索的字符串
* beg -- 开始索引，默认为 0
* end -- 结束索引，默认为字符串的长度

```py
# example
str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2);          #15
print str1.find(str2, 10);      #15
print str1.find(str2, 40);      #-1,查不到返回-1
```

## 8.3 `string.join()`

- 语法 `'sep'.join(seq)`_以 sep 作为分隔符，将 seq 所有的元素合并成一个新的字符串_ _返回值：返回一个以分隔符 sep 连接各个元素后生成的字符串_
- sep：分隔符。可以为空
- seq：要连接的元素序列、字符串、元组、字典

```py
>>> seq1 = ['hello','good','boy','doiido'] #对序列操作
>>> print ' '.join(seq1)
hello good boy doiido
>>> print ':'.join(seq1)
hello:good:boy:doiido

# 对字符串操作
>>> seq2 = "hello good boy doiido"
>>> print ':'.join(seq2)
h:e:l:l:o: :g:o:o:d: :b:o:y: :d:o:i:i:d:o

# 对元组操作
>>> seq3 = ('hello','good','boy','doiido')
>>> print ':'.join(seq3)
hello:good:boy:doiido

# 对字典操作
>>> seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
>>> print ':'.join(seq4)
boy:good:doiido:hello
```

- **另一个 `os.path.join()`**

* 语法 `os.path.join(path1[,path2[,......]])`

```py
 # 合并目录
>>> import os
>>> os.path.join('/hello/','good/boy/','doiido')
'/hello/good/boy/doiido'
```

> 参考[博客网站](https://www.cnblogs.com/sui776265233/p/10755525.html)


## 8.4 ord() & chr()

ord()
将字符转化为ascii码

chr()
将ascii码转化为字母或实际数字

```python
ord('a')  # 返回ASCII码 97

chr(97)   # 返回 字母'a'
```