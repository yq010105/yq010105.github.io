---
title: Spider_note
date: 2020-02-08 11:40:18
tags:
    - Python
    - Spider
---
>参考Github上的[教程](https://github.com/kingname/SourceCodeOfBook "Github")学习
# 线程
## 线程Pool
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
<!-- more -->

## 所用函数
`time.time()` &nbsp; 程序当前时间
eg：用来对比单线程和多线程访问baidu的速度


# request库
## 基础用法
```
url = ''
headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like\ Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48"
}
response = requests.get(url,headers=headers)
response.encoding = 'utf-8'  #或者GBK
html = response.text
```
## 进阶用法
* **使用requests模拟发送get请求**
```
import requests 

url = 'http://exercise.kingname.info/ajax_1_backend'
html = requests.get(url).content.decode()
print(html)
# 如果你看到这一段文字，说明你已经成功访问了这个页面,并获取了GET方式的异步加载数据。
```
* **使用requests模拟发送post请求**
```
import requests

url = 'http://exercise.kingname.info/ajax_1_postbackend'
html = requests.post(url,json={'name':'yunq','age':24}).content.decode()
print(html)
# 如果你看到这一段文字，说明你已经成功访问了这个页面，并获取了POST方式的异步加载数据。你向服务器提交的两个参数，分别为name： yunq, age：24
```

>参考[学习网站](http://exercise.kingname.info/exercise_ajax_1.html)，([异步GET与POST请求](#异步GET与POST请求))

# re库
## 基础用法
```
re.findall(r'',html,re.S)   #返回一个列表，这是一个列表所以可以取第一个数据
                            #re.findall(r'',html,re.S)[0]

re.search(r'',html,re.S)    #返回一个re.Match类型数据
                            #<re.Match object; span=(214, 297), match='secret = \'{"code": "\\u884c\\u52a8\\u4ee3\\u53f7>

re.search(r'href="sf">(.*?)<').group()        
                            #返回一个字符串             #.*?是匹配到的内容
                            #group()返回的是''内的字符串内容:href="sf">(.*?)<
                            #group(1)返回的是()中的字符串内容:.*?
                            #如果(.*?)有多个，则使用group(1),group(2)........
```

# Xpath--lxml库
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
### 基本框架
``` 具体使用方法
import lxml.html
selector = lxml.html.fromstring('网页源代码')    #网页源代码可用requests来获取
info = selector.xpath('一段XPath语句')
```
### example
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
## XPath通过chrome辅助构造
在一行源码单击右键，选择“Copy”→“Copy XPath”命令
把结果粘贴下来，可以看到如下的XPath语句：
`//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a`
*其中方括号中的数字，表示这是第几个该标签，但需要注意，这里的数字是从1开始*


# Beautiful Soup4库(BS4)
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

## [example](http://exercise.kingname.info/exercise_bs_1.html) 
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

# 异步加载与请求头
## 异步加载
*异步加载：一个页面，点击后网址不变，页面改变*
### AJAX技术
* AJAX是Asynchronous JavaScript And XML的首字母缩写，意为异步JavaScript与XML
* 使用AJAX技术，可以在不刷新网页的情况下更新网页数据。使用AJAX技术的网页，一般会使用HTML编写网页的框架。
* 在打开网页的时候，首先加载的是这个框架。剩下的部分将会在框架加载完成以后再通过JavaScript从后台加载。
### JSON
* JSON的全称是JavaScript Object Notation，是一种轻量级的数据交换格式。网络之间使用HTTP方式传递数据的时候，绝大多数情况下传递的都是字符串。
* 因此，当需要把Python里面的数据发送给网页或者其他编程语言的时候，可以先将Python的数据转化为JSON格式的字符串，然后将字符串传递给其他语言，其他语言再将JSON格式的字符串转换为它自己的数据格式
* **列表\字典与字符串相互转化**
* *python中字典or列表 与 json格式字符串的相互转化*
``` 
import json

data = {
    'name' : 'Connor',
    'sex' : 'boy',
    'age' : 26
}
print(data)     #dict   #{'name': 'Connor', 'sex': 'boy', 'age': 26}
data1=json.dumps(data)  
print(data1)    #str    #{"name": "Connor", "sex": "boy", "age": 26}
data2=json.loads(data1)
print(data2)    #dict   #{'name': 'Connor', 'sex': 'boy', 'age': 26}
# 如果加上indent=4参数
data3 = json.dumps(data,indent=4)
print(data3)    #str
#结果更加的美观易读
'''
{
    "name": "Connor",
    "sex": "boy",
    "age": 26
}
'''
```
* **str=json.dumps(dict)**
* **dict=json.loads(str)**

### 异步GET与POST请求
- 使用异步加载技术的网站，被加载的内容是不能在源代码中找到的。
- 为了解决这个问题，就需要使用Google Chrome浏览器的开发者模式。在网页上单击右键，选择“检查”命令，然后定位到“Network”选项卡
- 接下来需要刷新网页。在Windows下，按F5键或者单击地址栏左边的“刷新”按钮
- 单击“Network”选项卡下面出现的“ajax_1_backend”和“ajax_1_postbackend”，并定位到“Response”选项卡，可以看到这里出现了网页上面的内容
- 再选择“Headers”选项卡，可以看到这个请求使用GET方式，发送到http://exercise.kingname.info/ajax_1_backend
- 对于网页中的第2条内容，查看“Headers”选项卡，可以看到，这是使用POST方式向http://exercise.kingname.info/ajax_1_postbackend 发送请求，并以JSON格式提交数据
>具体代码实现看*request*&nbsp;&nbsp;的**[进阶用法](#进阶用法)**

### 特殊的异步加载
* **[练习页面](http://exercise.kingname.info/exercise_ajax_2.html)**
- 伪装成异步加载的后端渲染,数据就在源代码里，但却不直接显示出来
- 源代码最下面的JavaScript代码，其中有一段：
`{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}`
- 使用Python去解析，发现可以得到网页上面的内容
```
import json

html_json = '{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}'
html_dic = json.loads(html_json)
print(html_dic)      #{'code': '行动代号：天王盖地虎'}
```
- **这种假的异步加载页面，其处理思路一般是使用正则表达式从页面中把数据提取出来，然后直接解析**
```
import json
import requests
import re

url = 'http://exercise.kingname.info/exercise_ajax_2.html'
html = requests.get(url).content.decode()
code_json = re.search("secret = '(.*?)'", html, re.S).group(1)
code_dict = json.loads(code_json)
print(code_dict['code'])
#行动代号：天王盖地虎
```

### 多次请求的异步加载
* **[练习页面](http://exercise.kingname.info/exercise_ajax_3.html)**
- 还有一些网页，显示在页面上的内容要经过多次异步请求才能得到。
- 第1个AJAX请求返回的是第2个请求的参数，第2个请求的返回内容又是第3个请求的参数，只有得到了上一个请求里面的有用信息，才能发起下一个请求
- 在“Headers”选项卡查看这个POST请求的具体参数，在body里面发现两个奇怪的参数secret1和secret2
- 尝试修改secret1和secret2，发现POST请求无法得到想要的结果
**奇怪的参数**
```
name: "xx"
age: 24
secret1: "kingname is genius."
secret2: "kingname"
```
**如果修改这两个参数**
```
import json
import requests

url = 'http://exercise.kingname.info/ajax_3_postbackend'
return_json_1 = requests.post(url,json={"name":"xx",
"age":"24","secret1":"123","secret2":"456"})
return_json_2 = requests.post(url,json={"name" :"xx","age":23
})
print(json.loads(return_json_1.content.decode()))   #{'success': False, 'reason': '参数错误'}
print(json.loads(return_json_2.content.decode()))   #{'success': False, 'reason': '参数不全'}
```
- 打开这个练习页的源代码，在源代码中可以找到secret_2
```
<html>
    <head>
        <title>exercise ajax load</title>
        <script> var secret_2 = 'kingname';</script>
    </head>
    <body>
        <div class="content"></div>
    </body>
    <script src="static/js/jquery-3.2.1.min.js"></script>
    <script src="static/js/loaddata_3.js"></script>
</html>
```
- 虽然在POST参数中，名字是secret2，而源代码中的名字是secret_2，不过从值可以看出这就是同一个参数
- 源代码里面没有secret1，因此就要考虑这个参数是不是来自于另一个异步请求
- 继续在开发者工具中查看其他请求，可以成功找到secret1,注意，它的名字变为了“code”，但是从值可以看出这就是secret1
* **不少网站也会使用这种改名字的方式来迷惑爬虫开发者**
```
{code: "kingname is genius.", success: true}
code: "kingname is genius."
success: true
```
- 这一条请求就是一个不带任何参数的GET请求
- *对于这种多次请求才能得到数据的情况，解决办法就是逐一请求，得到返回结果以后再发起下一个请求。具体到这个例子中，那就是先从源代码里面获得secret2，再通过GET请求得到secret1，最后使用secret1和secret2来获取页面上显示的内容*
* **[爬取网站]http://exercise.kingname.info/exercise_ajax_3.html)**
```example
import json
import requests
import re

url = 'http://exercise.kingname.info/exercise_ajax_3.html'
first_ajax_url = 'http://exercise.kingname.info/ajax_3_backend'
second_ajax_url = 'http://exercise.kingname.info/ajax_3_postbackend'

page_html = requests.get(url).content.decode()
secret_2 = re.search("secret_2 = '(.*?)';",page_html,re.S).group(1)
print(secret_2)           #kingname

ajax_1_json = requests.get(first_ajax_url).content.decode()
print(ajax_1_json)        #{"code": "kingname is genius.", "success": true}
ajax_1_dict = json.loads(ajax_1_json)
secret_1 = ajax_1_dict['code']
print(secret_1)           #kingname is genius.

# 获取了secret_1和secret_2后post请求second_ajax_url

ajax_2_json = requests.post(second_ajax_url,json={
    'name':'yq','age':24,'secret1':secret_1,'secret2':secret_2
}).content.decode()
print(ajax_2_json)          #{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u54ce\u54df\u4e0d\u9519\u54e6", "success": true}

ajax_2_dict = json.loads(ajax_2_json)
print(ajax_2_dict)          #{'code': '行动代号：哎哟不错哦', 'success': True}

code = ajax_2_dict['code']
print(code)                 #行动代号：哎哟不错哦
```

### 基于异步加载的简单登录
* **[练习页面](http://exercise. kingname.info/exercise_ajax_4.html)**
- 网站的登录方式有很多种，其中有一种比较简单的方式，就是使用AJAX发送请求来进行登录
- 在[练习页面](http://exercise. kingname.info/exercise_ajax_4.html)中根据输入框中的提示，使用用户名“kingname”和密码“genius”进行登录,登录成功以后弹出提示框
- **对于这种简单的登录功能，可以使用抓取异步加载网页的方式来进行处理**
- 在Chrome开发者工具中可以发现，当单击“登录”按钮时，网页向后台发送了一条请求