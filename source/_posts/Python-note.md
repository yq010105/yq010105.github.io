---
title: Python_note
date: 2020-02-09 15:38:38
tags:
    - Python
---

# 文件管理（txt）
```
fd = open('file.txt','w',encoding='utf-8')      #utf-8 or GBK
fd.write(content)     
fd.close()
```
其中content可以是字符串，变量，\t ......
<hr/>

| r | w | a |
| :----: | :----: | :----: |
| 只读 | 覆盖写 | 添加写 |

# csv文件
<!-- more -->
## 列表序列数据
* headers :表头
* rows :内容
* f_csv = csv.writer(f)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*f为open('file.txt','w',encoding='utf-8')*
* f_csv.writerow(headers)
* f_csv.writerows(rows)
```
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
*注意：如果打开csv文件出现空行的情况，那么需要添加一个参数 newline=”*
`with open('test.csv','w',newline='')as f:`

| class | name | sex | height | year |
| :----: | :----: | :----: | :----: | :----: |				
|1|xiaoming|male|168|23|				
|1|xiaohong|female|162|22|				
|2|xiaozhang|female|163|21|
|2|xiaoli|male|158|21|

## 字典序列数据
* headers :表头
* rows :内容
* f_csv = DictWriter(f,headers)
* f_csv.writeheader()
* f_csv.writerows(rows)
```
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
| class | name | sex | height | year |
| :----: | :----: | :----: | :----: | :----: |				
|1|xiaoming|male|168|23|				
|1|xiaohong|female|162|22|				
|2|xiaozhang|female|163|21|
|2|xiaoli|male|158|21|

## csv文件的读
```
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
>参考[网站](https://blog.csdn.net/katyusha1/article/details/81606175 "CSDN")

# with open () as 读写文件
```
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

>参考[网站](https://blog.csdn.net/xrinosvip/article/details/82019844 "CSDN")


# python中陌生的函数
*自己还不太熟悉的*
## `split() #对字符串进行切片`--返回一个列表


语法`str.split(str="", num=string.count(str)).`
* str：分隔符，默认为所有的空字符，包括空格、换行、指标
* num：分割次数，默认为-1，即分割所有
```
#example
txt = "Google#Runoob#Taobao#Facebook"
 
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
 
print(x)         #['Google', 'Runoob#Taobao#Facebook']
```
>参考教程：[RUNOOB](https://www.runoob.com/python/att-string-split.html "runoob.com")
