---
title: Python-Note
date: 2020-02-09 15:38:38
toc: true
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

# 9. python中类的相关知识 

## 9.1 类的定义和创建

```python
# 定义类，类名为Cname
class Cname(object):
    pass

# 创建cname1实例
cname1 = Cname()
```

## 9.2 类中的实例属性与类属性

* 实例属性：用于区分不同的实例，不同的类有不同的实例属性
* 类属性：是每个实例共有的属性，每个实例共有的属性

### 9.2.1 实例属性

`cname1.name = y` `cname2.name = q`
每个实例有了name属性后就可以访问
`print(cname1.name)` `print(cname2.name)`

但是这样会比较麻烦，所以可以在每个实例中统一加上name属性
```python
class Cname(object):
    def __init__(self,name):  # 初始化一个属性r
        self.name = name
```

**\_\_init\_\_() 方法的第一个参数必须是 self** 
*self 代表类的实例，是通过类创建的实例*

然后创建实例，就可以直接带上参数 `cname1 = Cname(y)` 
然后访问实例属性 `print(cname1.name)`

### 9.2.2 类属性

类的属性绑定后，所有实例都可以访问，而且**实例访问的类属性都相同**
**实例属性每个实例各自拥有，互相独立，而类属性有且只有一份**

```python
class Cname(object):
    zhongz = 'people'

    def __init__(self,name):
        self.name = name

cname1 = Cname('y')
cname2 = Cname('q')

print('--------')
print(cname1.zhongz)    # people
print(cname2.zhongz)    # people

# 通过类名修改了类属性后
Cname.zhongz = 'tenshi'
print('--------')
print(cname1.zhongz)    # tenshi
print(cname2.zhongz)    # tenshi

# 通过实例名修改了类属性
cname1.zhongz = 'mea'
print('--------')
print(cname1.zhongz)    # mea
print(cname2.zhongz)    # tenshi

# 删除了cname1的类属性zhongz后
print('--------')
print(cname1.zhongz)    # mea
del cname1.zhongz
print(cname1.zhongz)    # tenshi
```

**要修改类属性，不要再实例上修改，而是在类名上修改**

## 9.3 类的实例方法

**method** is the **function** in **class** ~~英语四级差点没过的渣渣~~
**方法是表明这个类用是来做什么,方法就是类中的函数**

*最简单的一个方法：打印属性*

```python
class Cname(object):
    zhongz = 'people'

    def __init__(self,name):
        self.name = name

    def printname(self):
        print(self.name) # 打印名字

cname1 = Cname('y')
cname2 = Cname('q')
cname1.printname()  # y
cname2.printname()  # q
```

`printname(self)`就是一个最简单的方法


## 9.4 类中的访问限制

### 9.4.1 属性的访问限制

python的类中的属性，如果有些属性不希望被外部访问，我们可以属性命名时以双下划线开头 `__`，如 `__age`

>但，如果一个属性以"\_\_xxx\_\_"的形式定义，那么它可以被外部访问。以"\_\_xxx\_\_"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性是以“\_\_xxx\_\_”定义，所以我们不要把普通属性用"\_\_xxx\_\_"定义。

>**加双下划线\_\_xx 的属性，可以通过“ \_类名\_\_xx ”可以访问到属性的值 如`Cname._Cname__age`**

### 9.4.2 方法的访问限制

在方法名前加双下划线，如`def __printage():`
此时，该方法只能在类的内部使用，而无法被外部调用

## 9.5 类中的装饰方法

* `@classmethod`    用来修饰类方法。使用在与类进行交互，但不和其实例进行交互的函数方法上
* `@staticmethod`   用来修饰静态方法。使用在有些与类相关函数，但不使用该类或该类的实例。如更改环境变量、修改其他类的属性等

*classmethod必须使用类的对象作为第一个参数，而staticmethod则可以不传递任何参数*

### 9.5.1 @classmethod 修饰方法——类方法

类方法，我们不用通过实例化类就能访问的方法。而且@classmethod 装饰的方法不能使用实例属性，只能是类属性。它主要使用在和类进行交互，但不和其实例进行交互的函数方法上。

```python
class Cname(object):
    zhongz = 'people'

    def __init__(self,name):
        self.name = name

    def printname(self):
        print(self.name)
    
    @classmethod
    def printwe(cls):
        print(cls.zhongz)

# Cname.printname()   # 没有实例化 ，会发生错误
Cname.printwe()     # 没有实例化也可以访问
```

>printwe(cls)中cls表示的是类，它和self类实例有一定的差别。类方法中都是使用cls，实例方法中使用self

### 9.5.2 @staticmethod 修饰方法——静态方法

`@staticmethod` 不强制要求传递参数（它做的事与类方法或实例方法一样）
`@staticmethod` 使用在有些和类相关函数，但不使用该类或者该类的实例。如更改环境变量、修改其他类的属性等
`@staticmethod` 修饰的方法是放在类外的函数，我们为了方便将他移动到了类里面，它对类的运行无影响

```python
class Date(object):
   day = 0
   month = 0
   year = 0

   def __init__(self, year=0, month=0, day=0):
       self.day = day
       self.month = month
       self.year = year

   @classmethod
   def from_string(cls, date_as_string):
       year, month, day = date_as_string.split('-')
       date = cls(year, month, day)
       return date
    # 返回的是类的实例

   @staticmethod
   def is_date_valid(date_as_string):
       """
      用来校验日期的格式是否正确
       """
       year, month, day = date_as_string.split('-')
       return int(year) <= 3999 and int(month) <= 12 and int(day) <= 31

date1 = Date.from_string('2012-05-10')
print(date1.year, date1.month, date1.day)
is_date = Date.is_date_valid('2012-09-18') # 格式正确 返回True
```

is_date_valid(date_as_string) 只有一个参数，它的运行不会影响类的属性

>@staticmethod修饰方法 is_date_valid(date_as_string)中无实例化参数self或者cls；而@classmethod修饰的方法中有from_string(cls, date_as_string) 类参数cls

## 9.6 python中的property的使用

property的作用
* 作为装饰器 @property将类方法转换为类属性（只读）
* property重新实现一个属性的setter和getter方法

### 9.6.1 @property将类方法转换为只读属性

经常使用，将类的属性设置为不可修改

将一个类方法转变成一个类属性

```python
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   @property
   def pi(self):
       return self.__pi

circle1 = Circle(2)
print(circle1.pi)
circle1.pi=3.14159  # 出现AttributeError异常
```

创建实例后我们可以使用circle1.pi 自己获取方法的返回值，而且他只能读不能修改

### 9.6.2 property重新实现setter和getter方法

我也不太懂hhh

```python
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   def get_pi(self):
       return self.__pi

   def set_pi(self, pi):
       Circle.__pi = pi

   pi = property(get_pi, set_pi)

circle1 = Circle(2)
circle1.pi = 3.14  # 设置 pi的值
print(circle1.pi)  # 访问 pi的值
```

当我们以这种方式使用属性函数时，它允许pi属性设置并获取值本身而不破坏原有代码

```python
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   @property
   def pi(self):
       return self.__pi

   @pi.setter
   def pi(self, pi):
       Circle.__pi = pi

circle1 = Circle(2)
circle1.pi = 3.14  # 设置 pi的值
print(circle1.pi)  # 访问 pi的值
```

把一个getter方法变成属性，只需要加上@property就可以了，如上此时pi(self)方法，@property本身又创建了另一个装饰器@pi.setter，负责把一个setter方法变成属性赋值，于是，将@pi.setter加到pi(self, pi)上，我们就拥有一个可控的属性操作


>参考[知乎大佬](https://www.zhihu.com/people/lyzf)的[教程](https://zhuanlan.zhihu.com/p/30223570)
>感谢大佬让我搞懂了python的类，虽然最后的不太懂，但是基础是懂了

接着学aaaaaaa

## 9.7 类的继承  --- 大师，我悟了

### 9.7.1 类的继承

```python
class Animal(object):  #  python3中所有类都可以继承于object基类
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def call(self):
       print(self.name, '会叫')
# 现在我们需要定义一个Cat猫类继承于Animal，猫类比动物类多一个sex属性。
class Cat(Animal):
   def __init__(self,name,age,sex):
       super(Cat, self).__init__(name,age)  # 不要忘记从Animal类引入属性
       self.sex=sex

if __name__ == '__main__':  # 单模块被引用时下面代码不会受影响，用于调试
   c = Cat('喵喵', 2, '男')  #  Cat继承了父类Animal的属性
c.call()  # 输出 喵喵 会叫 ，Cat继承了父类Animal的方法 
```

我悟了：类的继承一般都是object，然后如果想要继承自己的类，则可以把object继承对象改一下，原来类名后括号里的东西是继承对象

一定要用 `super(Cat, self).__init__(name,age)` 去初始化父类，否则，继承自 Animal的 Cat子类将没有 `name` 和 `age` 两个属性

函数`super(Cat, self)`将返回当前类继承的父类，即 Animal，然后调用`__init__()`方法，注意self参数已在`super()`中传入，在`__init__()`中将隐式传递，不能再写出self

### 9.7.2 Python对子类方法的重构

子类中的方法要求跟父类中的方法不同时，可以在子类中重构方法

```python
class Cat(Animal):
   def __init__(self, name, age, sex):
       super(Cat, self).__init__(name,age)
       self.sex = sex

   def call(self):
       print(self.name,'会“喵喵”叫')

if __name__ == '__main__':
   c = Cat('喵喵', 2, '男')
   c.call()  # 输出：喵喵 会“喵喵”叫
```

当我们在子类中重构父类的方法后，Cat子类的实例先会在自己的类Cat中查找该方法，当找不到该方法时才会去父类Animal中查找对应的方法

### 9.7.3 Python中子类与父类的关系

```python
class Animal(object):
   pass

class Cat(Animal):
   pass

A= Animal()
C = Cat()
```

* “A”是Animal类的实例，但，“A”不是Cat类的实例。
* “C”是Animal类的实例，“C”也是Cat类的实例。

函数 `isinstance(变量,类型)`
判断变量的类型，判断对象之间的关系

```python
print('"A" IS Animal?', isinstance(A, Animal))
print('"A" IS Cat?', isinstance(A, Cat))
print('"C" IS Animal?', isinstance(C, Animal))
print('"C" IS Cat?', isinstance(C, Cat))

# 输出
"A" IS Animal? True
"A" IS Cat? False
"C" IS Animal? True
"C" IS Cat? True
```

### 9.7.4 python中多态

类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Animal派生出 Cat和Dog，并都写了一个 call() 方法

```python
class Animal(object):  
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def call(self):
       print(self.name, '会叫')

class Cat(Animal):
   def __init__(self, name, age, sex):
       super(Cat, self).__init__(name, age)
       self.sex = sex

   def call(self):
       print(self.name, '会“喵喵”叫')

class Dog(Animal):
   def __init__(self, name, age, sex):
       super(Dog, self).__init__(name, age)
       self.sex = sex
   def call(self):
       print(self.name, '会“汪汪”叫')
```

我们定义一个do函数，接收一个变量 ‘all’,如下：

```python
def do(all):
   all.call()

A = Animal('小黑',4)
C = Cat('喵喵', 2, '男')
D = Dog('旺财', 5, '女')

for x in (A,C,D):
   do(x)

# 输出结果
# 小黑 会叫
# 喵喵 会“喵喵”叫
# 旺财 会“汪汪”叫
```

这种行为称为多态。也就是说，方法调用将作用在 all 的实际类型上。C 是 Cat 类型，它实际上拥有自己的 call() 方法以及从 Animal 继承的 call 方法
而调用 C .call() 总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止

>注意事项
> * 在继承中基类的构造方法（`__init__()方法`）不会被自动调用，它需要在其派生类的构造方法中亲自专门调用。
> * 在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。而在类中调用普通函数时并不需要带上self参数
> * Python总是首先查找对应类的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）

# 10. 几个python编写技巧

## 10.1 变量的交换

`a,b = b,a`

## 10.2 字符串格式化

`print("Hi, I'm %s . I'm from %s . And I'm %d" % (name,country,age))`
`print("Hi, I'm {} . I'm from {} . And I'm {}".format(name,country,age))`
`print(f"Hi, I'm {name} . I'm from {country} . And I'm {age+1}"`

## 10.3 Yield语法

yield不需要整个列表生成完毕后再输出，可以一个一个输出

每当一个数据生成时，可以直接输出

```python
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b
    return nums
for i in fibonacci(10):
    print(i)
```

## 10.4 列表解析式