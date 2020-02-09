---
title: Spider_note
date: 2020-02-08 11:40:18
tags:
---
# 一、线程
### 线程Pool
```多线程计算每个数的平方
from multiprocessing.dummy import Pool   
def calc_power2(num):
return num*num
pool = Pool(5)
origin_num = [x for x in range(10)]
result = pool.map(calc_power2,origin_num)
print(f'0~9的平方分别为：{result}')
```
`Pool(5)` &emsp;五个线程
<hr/>

### 所用函数
`time.time()` &nbsp; 程序当前时间
eg：用来对比单线程和多线程访问baidu的速度

<!-- more -->
# 二、request库
## 基础用法
```
url = ''
headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like\ Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48"
}
response = request.get(url,headers=headers)
response.encoding = 'utf-8'  #或者GBK
html = response 
```
## 另一种用法
`html = requests.get('url').content.decode()`
# 三、re库
## 基础用法
```
re.findall(r'',html,re.S)   #这是一个列表所以可以取第一个数据
                            #re.findall(r'',html,re.S)[0]
```

# 四、Xpath--lxml库
* XPath是一种查询语言，能从XML\HTML的树状结构中寻找节点

## XPath语法
### XPath语法解析
``` example
example_html
<html>
    <head>
         <title>测试</title>
    </head>
    <body>
         <div class="useful">
 <ul>
                   <li class="info">我需要的信息1</li>
                   <li class="info">我需要的信息2</li>
                   <li class="info">我需要的信息3</li>
 </ul>
         </div>
         <div class="useless">
              <ul>
                   <li class="info">垃圾1</li>
                   <li class="info">垃圾2</li>
              </ul>
         </div>
     </body>
</html>
```
`info = selector.xpath('//div[@class="useful"]/ul/li/text()')`
就可以提取出class="userful"中的三句话，返回一个列表
##### 基本框架
``` 具体使用方法
import lxml.html
selector = lxml.html.fromstring('网页源代码')    #网页源代码可用requests来获取
info = selector.xpath('一段XPath语句')
```
###### example
``` example
import lxml.html

source = '''
<html>
    <head>
         <title>测试</title>
    </head>
    <body>
         <div class="useful">
 <ul>
                   <li class="info">我需要的信息1</li>
                   <li class="info">我需要的信息2</li>
                   <li class="info">我需要的信息3</li>
 </ul>
         </div>
         <div class="useless">
              <ul>
                   <li class="info">垃圾1</li>
                   <li class="info">垃圾2</li>
              </ul>
         </div>
     </body>
</html>
'''
selector = lxml.html.fromstring(source)
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
print(info)         #['我需要的信息1', '我需要的信息2', '我需要的信息3']
```
<hr/>

* a.**XPath语句格式**
`info = selector.xpath('一段XPath语句')`中'一段XPath语句'的格式
核心思想：XPath就是写地址
获取文本：`//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../text()`
获取属性值：`//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../@属性n`
其中的`[@属性="属性值"]`不是必需的，其作用是帮助过滤相同的标签，无相同标签可省略
* b.**标签1的选取**         
标签1可以直接从html这个最外层的标签开始，一层一层往下找，这个时候，XPath语句是这样的：
`/html/body/div[@class="useful"]/ul/li/text()`
但是由于前面的'/html/body'是所有HTML通用的，而且没有属性，所以可不写，即带属性标签前的标签都可以省略
* c.**可以省略的属性**
1、本身标签没有属性
2、这个标签所有的属性值相同
* d.**XPath的特殊情况**
1、以相同字符串开头`标签[starts-with(@属性,"开头字符串")]`
```
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
    content = selector.xpath('//div[starts-with(@id,"test")]/text()')
    print(content)      #['需要的内容1','需要的内容3','需要的内容2']
```
2、属性值包含相同字符串`标签[contains(@属性,"相同字符串")]`
3、对XPath返回的对象执行XPath
```
useful = selector.xpath('//div[@class="useful"]')   #这里返回一个列表
info_list = useful[0].xpath('ul/li/text()')         #useful[0]即为列表中第一个数据
print(info_list)
```
4、不同标签下的文字
```
import lxml.html

html = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div id="test3">
        我左青龙，
        <span id="tiger">
        右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
        老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''
#如果直接提取id="test3"
selector = lxml.html.fromstring(html)
content_1 = selector.xpath('//div[@id="test3"]/text()')
print(content_1)   #['\n        我左青龙，\n        ', '\n        龙头在胸口。\n    ']
#只会提取到div标签中的文字信息，而不会自动提取子标签中的信息

#这时就需要用string(.)关键字了
selector = lxml.html.fromstring(html)
data = selector.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
print(info)     #就可以提取出所有的文本信息了
```
### XPath通过chrome辅助构造
在一行源码单击右键，选择“Copy”→“Copy XPath”命令
把结果粘贴下来，可以看到如下的XPath语句：
`//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a`
*其中方括号中的数字，表示这是第几个该标签，但需要注意，这里的数字是从1开始*


# 五、Beautiful Soup4库(BS4)
*BS4在某些方面比XPath易懂，但是不如XPath简洁，而且由于它是使用Python开发的，因此速度比XPath慢。*
使用Beautiful Soup4提取HTML内容，一般要经过以下两步。
## bs4处理步骤
* 1)处理源代码生成BeautifulSoup对象。
解析源代码生成BeautifulSoup对象，使用以下代码：
`soup = BeautifulSoup(网页源代码, '解析器')`
解析器：       
这里的“解析器”，可以使用html.parser：
`soup = BeautifulSoup(source, 'html.parser')`
如果安装了lxml，还可以使用lxml：
`soup = BeautifulSoup(source, 'lxml')`
* 2)使用find_all()或者find()来查找内容。
`soup.find(class_='属性值')`
*由于HTML中的class属性与Python的class关键字相同，因此为了不产生冲突，BS4规定，如果遇到要查询class的情况，使用“class_”来代替*

###### [example](http://exercise.kingname.info/exercise_bs_1.html) 
```example_link
import request
from bs4 import BeautifulSoup

html = requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()
# 1、解析源代码
soup = BeautifulSoup(html,'lxml')
# 2、查找内容
info = soup.find(class_= 'test')
print(info.string)      #我需要的信息2

# 先抓大，再抓小
useful = soup.find(class_='useful')
all_content = useful.find_all('li')
for li in all_content:
    print(li.string)        #我需要的信息1
                            #我需要的信息2
                            #我需要的信息3
    print(li)               #<li class="info">我需要的信息1</li>
                            #<li class="test">我需要的信息2</li>
                            #<li class="iamstrange">我需要的信息3</li>    
    print(li['class'])      #['info']
                            #['test']
                            #['iamstrange']
```
* 其他查找方法
**以‘我需要’为开头的信息**
`content = soup.find_all(text = re.compile('我需要'))`
**对属性值搜素使用正则,即对iamstrang属性值搜索**
```
content = soup.find_all(class_=re.compile('iam'))[0]
print(content.string)       #我需要的信息3
```
