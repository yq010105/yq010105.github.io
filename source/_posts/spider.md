---
title: Spider_note(已置顶)
date: 2020-02-08 11:40:18
top: true
tags:
    - Python
    - Spider
---
>参考Github上的[教程](https://github.com/kingname/SourceCodeOfBook "Github")学习
一个连python都没有完全学会的菜鸡来学爬虫
<!-- more -->
# 1. 线程
## 1.1 线程Pool
```py
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


## 1.2 所用函数
`time.time()` &nbsp; 程序当前时间
eg：用来对比单线程和多线程访问baidu的速度


# 2. request库
## 2.1 基础用法
```py
url = ''
headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like\ Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48"
}
response = requests.get(url,headers=headers)
response.encoding = 'utf-8'  #或者GBK
html = response.text
```
## 2.2 进阶用法
* **使用requests模拟发送get请求**
```py
import requests 

url = 'http://exercise.kingname.info/ajax_1_backend'
html = requests.get(url).content.decode()
print(html)
# 如果你看到这一段文字，说明你已经成功访问了这个页面,并获取了GET方式的异步加载数据。
```
* **使用requests模拟发送post请求**
```py
import requests

url = 'http://exercise.kingname.info/ajax_1_postbackend'
html = requests.post(url,json={'name':'yunq','age':24}).content.decode()
print(html)
# 如果你看到这一段文字，说明你已经成功访问了这个页面，并获取了POST方式的异步加载数据。你向服务器提交的两个参数，分别为name： yunq, age：24
```

>参考[学习网站](http://exercise.kingname.info/exercise_ajax_1.html)，([异步GET与POST请求](#异步GET与POST请求))

# 3. re库
## 3.1 基础用法
```py
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
# 4. 正则表达式
`.*?`

# 5. Xpath--lxml库
* XPath是一种查询语言，能从XML\HTML的树状结构中寻找节点

## 5.1 XPath语法
### 5.1.1 XPath语法解析
```html
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
### 5.1.2 基本框架
```py
import lxml.html
selector = lxml.html.fromstring('网页源代码')    #网页源代码可用requests来获取
info = selector.xpath('一段XPath语句')
```
### 5.1.3 example
```py 
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
```py
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
    content = selector.xpath('//div[starts-with(@id,"test")]/text()')
    print(content)      #['需要的内容1','需要的内容3','需要的内容2']
```
2、属性值包含相同字符串`标签[contains(@属性,"相同字符串")]`
3、对XPath返回的对象执行XPath
```py
useful = selector.xpath('//div[@class="useful"]')   #这里返回一个列表
info_list = useful[0].xpath('ul/li/text()')         #useful[0]即为列表中第一个数据
print(info_list)
```
4、不同标签下的文字
```py
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
## 5.2 XPath通过chrome辅助构造
在一行源码单击右键，选择“Copy”→“Copy XPath”命令
把结果粘贴下来，可以看到如下的XPath语句：
`//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a`
*其中方括号中的数字，表示这是第几个该标签，但需要注意，这里的数字是从1开始*


# 6. Beautiful Soup4库(BS4)
*BS4在某些方面比XPath易懂，但是不如XPath简洁，而且由于它是使用Python开发的，因此速度比XPath慢。*
使用Beautiful Soup4提取HTML内容，一般要经过以下两步。
## 6.1 bs4处理步骤
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

## 6.2 [example](http://exercise.kingname.info/exercise_bs_1.html) 
```py
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
```py
content = soup.find_all(class_=re.compile('iam'))[0]
print(content.string)       #我需要的信息3
```

# 7. 异步加载与请求头
## 7.1 异步加载
*异步加载：一个页面，点击后网址不变，页面改变*
### 7.1.1 AJAX技术
* AJAX是Asynchronous JavaScript And XML的首字母缩写，意为异步JavaScript与XML
* 使用AJAX技术，可以在不刷新网页的情况下更新网页数据。使用AJAX技术的网页，一般会使用HTML编写网页的框架。
* 在打开网页的时候，首先加载的是这个框架。剩下的部分将会在框架加载完成以后再通过JavaScript从后台加载。
### 7.1.2 JSON
* JSON的全称是JavaScript Object Notation，是一种轻量级的数据交换格式。网络之间使用HTTP方式传递数据的时候，绝大多数情况下传递的都是字符串。
* 因此，当需要把Python里面的数据发送给网页或者其他编程语言的时候，可以先将Python的数据转化为JSON格式的字符串，然后将字符串传递给其他语言，其他语言再将JSON格式的字符串转换为它自己的数据格式
* **列表\字典与字符串相互转化**
* *python中字典or列表 与 json格式字符串的相互转化*
``` py
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

### 7.1.3 异步GET与POST请求
- 使用异步加载技术的网站，被加载的内容是不能在源代码中找到的。
- 为了解决这个问题，就需要使用Google Chrome浏览器的开发者模式。在网页上单击右键，选择“检查”命令，然后定位到“Network”选项卡
- 接下来需要刷新网页。在Windows下，按F5键或者单击地址栏左边的“刷新”按钮
- 单击“Network”选项卡下面出现的“ajax_1_backend”和“ajax_1_postbackend”，并定位到“Response”选项卡，可以看到这里出现了网页上面的内容
- 再选择“Headers”选项卡，可以看到这个请求使用GET方式，发送到http://exercise.kingname.info/ajax_1_backend
- 对于网页中的第2条内容，查看“Headers”选项卡，可以看到，这是使用POST方式向http://exercise.kingname.info/ajax_1_postbackend 发送请求，并以JSON格式提交数据
>具体代码实现看*request*&nbsp;&nbsp;的**[进阶用法](#进阶用法)**

### 7.1.4 特殊的异步加载
* **[练习页面](http://exercise.kingname.info/exercise_ajax_2.html)**
- 伪装成异步加载的后端渲染,数据就在源代码里，但却不直接显示出来
- 源代码最下面的JavaScript代码，其中有一段：
`{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}`
- 使用Python去解析，发现可以得到网页上面的内容
```py
import json

html_json = '{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}'
html_dic = json.loads(html_json)
print(html_dic)      #{'code': '行动代号：天王盖地虎'}
```
- **这种假的异步加载页面，其处理思路一般是使用正则表达式从页面中把数据提取出来，然后直接解析**
```py
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

### 7.1.5 多次请求的异步加载
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
```py
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
```html
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
```js
{code: "kingname is genius.", success: true}
code: "kingname is genius."
success: true
```
- 这一条请求就是一个不带任何参数的GET请求
- *对于这种多次请求才能得到数据的情况，解决办法就是逐一请求，得到返回结果以后再发起下一个请求。具体到这个例子中，那就是先从源代码里面获得secret2，再通过GET请求得到secret1，最后使用secret1和secret2来获取页面上显示的内容*
* **[爬取网站]http://exercise.kingname.info/exercise_ajax_3.html)**
```py
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

### 7.1.6 基于异步加载的简单登录
* **[练习页面](http://exercise.kingname.info/exercise_ajax_4.html)**
- 网站的登录方式有很多种，其中有一种比较简单的方式，就是使用AJAX发送请求来进行登录
- 在[练习页面](http://exercise.kingname.info/exercise_ajax_4.html)中根据输入框中的提示，使用用户名“kingname”和密码“genius”进行登录,登录成功以后弹出提示框
- **对于这种简单的登录功能，可以使用抓取异步加载网页的方式来进行处理**
- 在Chrome开发者工具中可以发现，当单击“登录”按钮时，网页向后台发送了一条请求
**`{"code": "kingname is genius", "success": true}`**
```py
import requests
import json

url = 'http://exercise.kingname.info/ajax_4_backend'
code_json = requests.post(url,json={
    'username':'kingname','password':'genius'}).content.decode()
code__dict = json.loads(code_json)
print(code__dict['code'])
# kingname is genius
```
- 这就是使用POST方式的最简单的AJAX请求。使用获取POST方式的AJAX请求的代码，就能成功获取到登录以后返回的内容

## 7.2 请求头
### 7.2.1 请求头的作用
- 使用计算机网页版外卖网站的读者应该会发现这样一个现象：第一次登录外卖网页的时候会让你选择当前所在的商业圈，一旦选定好之后关闭浏览器再打开，网页就会自动定位到先前选择的商业圈
- 又比如，例如携程的网站，使用计算机浏览器打开的时候，页面看起来非常复杂多样
- 同一个网址，使用手机浏览器打开时，网址会自动发生改变，而且得到的页面竟然完全不同
**同一个网址，PC端和手机端页面不同**
* Headers称为请求头，浏览器可以将一些信息通过Headers传递给服务器，服务器也可以将一些信息通过Headers传递给浏览器，电商网站常常应用的Cookies就是Headers里面的一个部分

### 7.2.2 伪造请求头
- 打开[练习页](http://exercise.kingname.info/exercise_headers.html)，使用Chrome的开发者工具监控这个页面的网页请求
- 页面看起来像是发起了一个普通的GET方式的异步请求给http://exercise.kingname.info/exercise_headers_backend
- 使用requests尝试获取这个网址的返回信息,结果发现失败
- 使用浏览器访问网站的时候，网站可以看到一个名称为Headers（请求头）的东西
```js
headers = {
            Accept: */*
            Accept-Encoding: gzip, deflate
            Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
            anhao: kingname
            Content-Type: application/json; charset=utf-8
            Cookie: __cfduid=d513aff6c34f63c4c2971cdf1e19780051581303763
            Host: exercise.kingname.info
            Proxy-Connection: keep-alive
            Referer: http://exercise.kingname.info/exercise_headers.html
            User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36
            X-Requested-With: XMLHttpRequest
            }
```
- 为了解决这个问题，就需要给爬虫“换头”。把浏览器的头安装到爬虫的身上，这样网站就不知道谁是谁了
- 要换头，首先就需要知道浏览器的头是什么样的。因此需要在Chrome浏览器开发者工具的“Network”选项卡的Request Headers里面观察这一次请求的请求头
- 在requests里面，设置请求头的参数名称为“headers”，它的值是一个字典
**带有请求头的请求，使用requests的发送格式为：**
```py
html = requests.get(url, headers=字典).content.decode()
html = requests.post(url, json=xxx, headers=字典).content.decode()
```
- 代码中的字典就对应了浏览器中的请求头
- 在爬虫里面创建一个字典，将Chrome的请求头的内容复制进去，并调整好格式，发起一个带有Chrome请求头的爬虫请求，可以发现请求获得成功
- 虽然对于某些网站，在请求头里面只需要设置User-Agent就可以正常访问了，但是为了保险起见，还是建议把所有项目都带上，这样可以让爬虫更“像”浏览器

## 7.3 模拟浏览器
- **[练习页面](http://exercise.kingname.info/exercise_advanced_ajax.html)**
- *问题：*
- 有一些网站在发起AJAX请求的时候，会带上特殊的字符串用于身份验证。这种字符串称为Token
- 打开练习页面，这个页面在发起AJAX请求的时候会在Headers中带上一个参数ReqTime；在POST发送的数据中会有一个参数sum
- 多次刷新页面，可以发现ReqTime和sum一直在变化
- 不难看出ReqTime是精确到毫秒的时间戳，即使使用Python生成了一个时间戳，也不能得到网页上面的内容
### 7.3.1 Selenium介绍
- 虽然在网页的源代码中无法看到被异步加载的内容，但是在Chrome的开发者工具的“Elements”选项卡下却可以看到网页上的内容
### 7.3.2 selenium安装
- 安装selenium `pip install selenium`
- 下载ChromeDriver
### 7.3.3 selenium的使用
#### 7.3.3.1 获取源代码
* **将chromedriver与代码放在同一个文件夹中以方便代码直接调用**
```  py
# 初始化selenium
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')     
```
* 指定了Selenium使用ChromeDriver来操作Chrome解析网页，括号里的参数就是ChromeDriver可执行文件的地址
- 如果要使用PhantomJS，只需要修改第3行代码即可：driver = webdriver.PhantomJS('./phantomjs')，需要将PhantomJS的可执行文件与代码放在一起
- 需要特别提醒的是，如果chromedriver与代码不在一起，可以通过绝对路径来指定，例如：driver = webdriver.Chrome('/usr/bin/chromedriver')
- 使用Windows的读者可在路径字符串左引号的左边加一个“r”符号，将代码写为：driver = webdriver.Chrome(r'C:\server\chromedriver.exe')
- 初始化完成以后，就可以使用Selenium打开网页了。要打开一个网页只需要一行代码：
`driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')`
- 代码运行以后会自动打开一个Chrome窗口，并在窗口里面自动进入这个网址对应的页面。一旦被异步加载的内容已经出现在了这个自动打开的Chrome窗口中，那么此时使用下列代码：
`html = driver.page_source`
- 就能得到在Chrome开发者工具中出现的HTML代码
**综合：**
```py
from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
time.sleep(5)
html = driver.page_source
print(html)
input('按任意键结束：')
```
**运行程序会出现以下界面**
![selenium](/img/selenium.png "selenium")
#### 7.3.3.2 等待信息出现
- 设置了一个5s的延迟，这是由于Selenium并不会等待网页加载完成再执行后面的代码。它只是向ChromeDriver发送了一个命令，让ChromeDriver打开某个网页
- 至于网页要开多久，Selenium并不关心。由于被异步加载的内容会延迟出现，因此需要等待它出现以后再开始抓取

#### 7.3.3.3 在网页中获取元素
*在网页中寻找需要的内容，可以使用类似于Beautiful Soup4 的语法：*
```py
element = driver.find_element_by_id("passwd-id") #如果有多个符合条件的，返回第1个
element = driver.find_element_by_name("passwd") #如果有多个符合条件的，返回第1个
element_list = driver.find_elements_by_id("passwd-id") #以列表形式返回所有的符合条件的element
element_list = driver.find_elements_by_name("passwd") #以列表形式返回所有的符合条件的element
```
**也可以使用XPath**
```py
element = driver.find_element_by_xpath("//input[@id='passwd-id']") 
#如果有多个符合条件的，返回第1个
element = driver.find_elements_by_xpath("//div[@id='passwd-id']") 
#以列表形式返回所有的符合条件的element
```
[练习网站](http://exercise.kingname.info/exercise_advanced_ajax.html)
```py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')

time.sleep(5)
try :
    WebDriverWait(driver,30).until(EC.text_to_be_present_in_element(By.CLASS_NAME,"content"),'通关')
except Exception as _:
    print('网页加载太慢，爬')
# 但是也可能会爬，不知到原因
element = driver.find_element_by_xpath('//div[@class="content"]')
print(f'异步加载的内容是：{element.text}')

# 异步加载的内容是：通关成功，通关口令：这是最终数据。

driver.quit()
```
## 7.4 实例：[乐视](http://www.le.com)爬取视频评论
* *1>分析网站的异步加载请求*
* *2>使用requests发送请求*<hr/>
* 通过使用Chrome的开发者工具分析页面的异步加载请求，可以发现评论所在的请求
* 可以使用Python来模拟这个请求，从而获取视频的评论信息
* 在请求的URL里面有两个参数：vid和pid,这两个参数在网页的源代码里面都可以找到
<hr/>

* 爬虫首先访问视频页面，通过正则表达式获取vid和pid，并将结果保存到“necessary_info”这个类属性对应的字典中
```py
# 核心代码
def get_necessary_id(self):
  source = self.get_source(self.url, self.HEADERS)
  vid = re.search('vid: (\d+)', source).group(1)
  pid = re.search('pid: (\d+)', source).group(1)
  self.necessary_info['xid'] = vid
  self.necessary_info['pid'] = pid
```
* 访问评论的接口，用Python发起请求，获得评论数据
```py
def get_comment(self):
    url = self.COMMENT_URL.format(xid=self.necessary_info['xid'],
                             pid=self.necessary_info['pid'])
    source = self.get_source(url, self.HEADERS)
    source_json = source[source.find('{"'): -1]
    comment_dict = json.loads(source_json)
    comments = comment_dict['data']
    for comment in comments:
        print(f'发帖人： {comment["user"]["username"]}, 评论内容：{comment["content"]}')
```
* 代码中，提前定义的self.COMMENT_URL和self.HEADERS
```py
# 综合
import re
import json
import requests

class LetvSpider(object):

    COMMENT_URL = 'http://api-my.le.com/vcm/api/list?jsonp=jQuery19100358 \
    8935956887496_1581419682085&type=video&rows=20&page=1&sort=&cid=2&sourc\
    e=1&xid=27576461&pid=10022394&ctype=cmt%2Cimg%2Cvote&listType=1&_=1581419682087'

    HEADERS = {'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'tj_lc=d551d3996ae75055e97c1f22ac9aa002; tj_uuid=-_15814196222976075472; tj_env=1; ssoCookieSynced=1; language=zh-cn; sso_curr_country=CN; vjuids=-75eba524.17033f49d1f.0.d645e0a5d3aa1; vjlast=1581419634.1581419634.30; tj_v2c=-27576461_2',
            'Host': 'api-my.le.com',
            'Proxy-Connection': 'keep-alive',
            'Referer':'http://www.le.com/ptv/vplay/27576461.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
             }

    def __init__(self,url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()
        self.get_comment()

    # 得到request返回的html--str
    def get_source(self,url,headers):
        return requests.get(url,headers).content.decode()
    
    def get_necessary_id(self):
        source = self.get_source(self.url,self.HEADERS) # 得到html
        vid = re.search('vid: (\d+)',source).group(1)   #re到vid、pid
        pid = re.search('pid: (\d+)',source).group(1)
        self.necessary_info['xid'] = vid        #传入vid、pid到字典
        self.necessary_info['pid'] = pid
    
    def get_comment(self):
        url = self.COMMENT_URL.format(xid=self.necessary_info['xid'],
        pid=self.necessary_info['pid'])     # format格式化  url 评论list的request_url
        source = self.get_source(url,self.HEADERS)  # 调用get_source()
        source_json = source[source.find('{"'): -1] # str切片
        comment_dict = json.loads(source_json)  #一个字典
        comments = comment_dict['data']
        for comment in comments:
            print(f'发帖人：{comment["user"]["username"]},评论内容:{comment["content"]}')

if __name__ == '__main__':
    spider = LetvSpider('http://www.le.com/ptv/vplay/27576461.html')


'''
发帖人：福建乐迷,评论内容:好喜欢东华帝君
发帖人：河北乐迷,评论内容:十
发帖人：河北乐迷,评论内容:瑶光上神好漂亮。
发帖人：河北乐迷,评论内容:太好看了。
发帖人：河北乐迷,评论内容:真水无香。
发帖人：河北乐迷,评论内容:喜欢白浅
发帖人：天莫邪,评论内容:杨幂真不好看
发帖人：呆萌小甜心,评论内容:爱幂幂
发帖人：G_,评论内容:有谁是看了枕上书又来看十里桃花我浅浅的
发帖人：黑名单,评论内容:我来啦
发帖人：凉辰梦瑾空人心_702_210,评论内容:为啥只能隔乐视看了 好伤心�😭
发帖人：上海乐迷,评论内容:产科医生
发帖人：红_,评论内容:这个很好看
发帖人：子璇,评论内容:墨渊霸气，白浅跟她在一起才不会受伤害
发帖人：聂芳英,评论内容:为什么其他的APP上看不到
发帖人：月色不错,评论内容:这个是玉帝还是王母
发帖人：Myth橙子,评论内容:每个平台看一遍我是有多闲
发帖人：上海乐迷,评论内容:怎么这么难找〈产科医生）的电视剧
发帖人：上海乐迷,评论内容:我想看产科医生的电视剧
发帖人：上海乐迷,评论内容:产科医生
'''
```

```py
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 网站名：菜鸟教程, 地址 www.runoob.com
```

```py
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
# value 为: 6
```

# 8. 模拟登录与验证码
- 对于一个需要登录才能访问的网站，它的页面在登录前和登录后可能是不一样的
- 如果直接使用requests去获取源代码，只能得到登录以前的页面源代码
## 8.1 模拟登录
* 1.使用Selenium操作浏览器登录和使用Cookies登录虽然简单粗暴，但是有效
* 2.使用模拟提交表单登录虽然较为麻烦，但可以实现自动化

### 8.1.1 使用Selenium模拟登录
```
     使用Selenium来进行模拟登录，整个过程非常简单。流程如下。
（1）初始化ChromeDriver。
（2）打开知乎登录页面。
（3）找到用户名的输入框，输入用户名。
（4）找到密码输入框，输入用户名。
（5）手动单击验证码。
（6）按下Enter键。

```
- 程序首先打开知乎的登录页面，然后使用“find_element_by_ name”分别找到输入账号和密码的两个输入框
- 这两个输入框的name属性值分别为“account”(我的是username)和“password”
- 在Selenium中可以使用send_keys()方法往输入框中输入字符串
- 在输入了密码以后，验证码框就会弹出来。知乎使用的验证码为点击倒立的文字，这种验证码不容易自动化处理，因此在这个地方让爬虫先暂停，手动点击倒立文字
- 爬虫中的input()语句会阻塞程序，直到在控制台按下Enter键，爬虫才会继续运行

### 8.1.2 使用Cookies登录
- *Cookie是用户使用浏览器访问网站的时候网站存放在浏览器中的一小段数据*
- Cookie的复数形式Cookies用来表示各种各样的Cookie。它们有些用来记录用户的状态信息；有些用来记录用户的操作行为；还有一些，具有现代网络最重要的功能：记录授权信息——用户是否登录以及用户登录哪个账号
- 为了不让用户每次访问网站都进行登录操作，浏览器会在用户第一次登录成功以后放一段加密的信息在Cookies中。下次用户访问，网站先检查Cookies有没有这个加密信息，如果有并且合法，那么就跳过登录操作，直接进入登录后的页面
- 通过已经登录的Cookies，可以让爬虫绕过登录过程，直接进入登录以后的页面
- 在已经登录知乎的情况下，打开Chrome的开发者工具，定位到“Network”选项卡，然后刷新网页，在加载的内容中随便选择一项，然后看右侧的数据，从Request Headers中可以找到Cookie
```
cookie: _zap=56180d87-245a-4b79-83e2-711f4629644e; d_c0="AMAY69ZKzRCPTh5KJj9edoIQ4_BiQS3iqwM=|1581434842"; _xsrf=jzLzeCfZignAw6qDdNqO85UOdCrRcB3C; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581485103,1581492629,1581492650,1581494278; capsion_ticket="2|1:0|10:1581494284|14:capsion_ticket|44:ZjQyY2FjMmZkZTJmNDJkNGI5NmYxMDNkMzc3MTVlNGI=|e2f4eb7e3652b2f1f3e439d7ff4275e4e15bdfbfbed8ce423dceded2da4235cf"; z_c0="2|1:0|10:1581494646|4:z_c0|92:Mi4xY2R0cUJRQUFBQUFBd0JqcjFrck5FQ1lBQUFCZ0FsVk5kdjh3WHdBMEczY0dBVm5MNUFmV1V4cmtja0p1Rm1kMGtn|560b73b3b5f052f6151d4a02e62f1f645f01ad7826d8c183d7152fb2fcf8456d"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581494647; tst=r; KLBRSID=81978cf28cf03c58e07f705c156aa833|1581494650|1581494278
```
* **请注意这里一定是“Request Headers”，不要选成了“Response Headers”** 
- 只要把这个Request Headers的内容通过requests提交，就能直接进入登录以后的知乎页面了
- 可以看到，使用Cookie来登录网页，不仅可以绕过登录步骤，还可以绕过网站的验证码
- Session，是指一段会话。网站会把每一个会话的ID（Session ID）保存在浏览器的Cookies中用来标识用户的身份
- requests的Session模块可以自动保存网站返回的一些信息
- 其实在前面章节中使用的requests.get()，在底层还是会先创建一个Session，然后用Session去访问
- 对于HTTPS的网站，在requests发送请求的时候需要带上verify=False这个参数，否则爬虫会报错
- 带上这个参数以后，爬虫依然会报一个警告，这是因为没有HTTPS的证书
- 不过这个警告不会影响爬虫的运行结果。对于有强迫症的读者，可以参考相关内容为requests设置证书，从而解除这个警告

### 8.1.3 模拟表单登录
**[练习页面](http://exercise.kingname.info/exercise_login?next=%2Fexercise_login_success)**
- 这个登录页面多了一个“自动登录”复选框输入用户名kingname，密码genius，勾选“自动登录”复选框并单击“登录”按钮，可以看到登录成功后的页面
- 打开Chrome的开发者工具并监控登录过程
- 然而，仔细观察会发现登录请求的那个网址只会在“Network”选项卡中存在1s，然后就消失了
- Network”选项卡下面只剩下登录成功后的页面所发起的各种网络请求
- 这是因为表单登录成功以后会进行页面跳转，相当于开了一个新的网页，于是新的请求就会直接把旧的请求覆盖。为了避免这种情况，需要在Chrome的开发者工具的“Network”选项卡中勾选“Preserve log”复选框，再一次登录就可以看到登录过程
- 此时可以看到Status Code是302，说明这里有一个网页跳转，也就证明了之前为什么登录以后看不到登录的请求
- **使用requests的Session模块来模拟这个登录**
```py
import requests

login_url = 'http://exercise.kingname.info/exercise_login'
login_sucess_url = 'http://exercise.kingname.info/exercise_login_success'

data = {
    'username':'kingname',
    'password':'genius',
    'remember':'Yes'
}

session = requests.Session()
before_login = session.get(login_sucess_url).text
print(before_login)
print('============开始登陆==============')
session.post(login_url,data=data).text
after_login = session.get(login_sucess_url).text
print(after_login)
```
**结果**
```html
<html>
    <head>
        <title>exercise login</title>
        <style>
            label { display: block;
                    width: 100px;
                    margin-left: auto;
                    margin-right: auto}
            body { text-align: center}
            .content {MARGIN-RIGHT: auto;
                      MARGIN-LEFT: auto;
                      height:200px;}
            .login {display: block;
                    margin-right: auto;
                    margin-left: auto;
                    margin-top: 5px;}
        </style>
    </head>
    <body>
        <div class="content">
            <form action="/exercise_login" method="POST">
                <div class="row">
                        <div class="form-group">
                            <label>用户名:</label>
                            <input name="username" type="text" class="form-control" placeholder="请输入:kingname" value="">
                        </div>
                </div>
                <div class="row">
                        <div class="form-group">
                            <label>密  码  :</label>
                            <input name="password" type="password" class="form-control" placeholder="请输入:genius" value="">
                        </div>
                </div>
                <div class="row">
                    <label class="checkbox pull-right" >自动登录
                        <input type="checkbox" name="rememberme" value="Yes" data-toggle="checkbox" />
                    </label>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <button type="submit" class="login">登录</button>
                    </div>
                </div>
            </form>
        </div>
    </body>
    <script src="static/js/jquery-3.2.1.min.js"></script>

</html>
============开始登陆==============
<html>
    <head>
        <title>Login Success</title>
    </head>
    <body>
        <div class="content">
            如果你看到这一行内容，说明你已经登录成功。<a href="/exercise_logout">退出登录</a>
        </div>
    </body>
</html>
```

## 8.2 验证码
### 8.2.1 肉眼打码
- 对于一次登录就可以长时间使用的情况，只需要识别一次验证码即可
- 这种情况下，与其花时间开发一个自动识别验证码的程序，不如直接肉眼识别
- **肉眼识别验证码有两种情况，借助浏览器与不借助浏览器**

- 1、借助浏览器
在模拟登录中讲到过Cookies，通过Cookies能实现绕过登录，从而直接访问需要登录的网站。因此，对于需要输入验证码才能进行登录的网站，可以手动在浏览器登录网站，并通过Chrome获取Cookies，然后使用Cookies来访问网站
这样就可以实现人工输入一次验证码，然后很长时间不再登录。
- 2、不借助浏览器
对于仅仅需要识别图片的验证码，可以使用这种方式——先把验证码下载到本地，然后肉眼去识别并手动输入给爬虫
```
手动输入验证码的一般流程如下:
（1）爬虫访问登录页面
（2）分析网页源代码，获取验证码地址
（3）下载验证码到本地
（4）打开验证码，人眼读取内容
（5）构造POST的数据，填入验证码
（6）POST提交
```
* *需要注意的是，其中的（2）、（3）、（4）、（5）、（6）步是一气呵成的，是在爬虫运行的时候做的。绝对不能先把爬虫程序关闭，肉眼识别验证码以后再重新运行*

**[练习页面](http://exercise.kingname.info/exercise_captcha.html)**
```py
import requests
import lxml.html

url = 'http://exercise.kingname.info/exercise_captcha.html'
url_check = 'http://exercise.kingname.info/exercise_captcha_check'

session = requests.session()
html = session.get(url).content
selector = lxml.html.fromstring(html)
captcha_url = selector.xpath('//img/@src')[0]

image = requests.get('http://exercise.kingname.info/'+captcha_url).content
with open('captcha.png','wb') as f:
    f.write(image)

captcha = input('请查看图片，然后输入在这里：')
after_check = session.post(url_check,data={'captcha':captcha})

print(f'请输入验证码后，网站返回：{after_check.content.decode()}')
```
**结果**
```
请查看图片，然后输入在这里：1595
请输入验证码后，网站返回：看到这个页面，说明你的验证码输入正确
```
![验证码](/img/captcha.png)

### 8.2.2 自动打码
1、Python图像识别
- 对于验证码识别，Python也有现成的库来使用
- 开源的OCR库pytesseract配合图像识别引擎tesseract，可以用来将图片中的文字转换为文本
- 这种方式在爬虫中的应用并不多见。因为现在大部分的验证码都加上了干扰的纹理，已经很少能用单机版的图片识别方式来识别了。所以如果使用这种方式，只有两种情况：网站的验证码极其简单工整，使用大量的验证码来训练tesseract
*安装tesseract*
打开网页下载安装包：https://github.com/tesseract-ocr/tesseract/wiki/Downloads ,在“3rd party Windows exe's/ installer”下面可以找到.exe安装包
*安装Python库*
pip install Pillow
pip install pytesseract
其中，Pillow是Python中专门用来处理图像的第三方库，pytesseract是专门用来操作tesseract的第三方库
*tesseract的使用*
```
          tesseract的使用非常简单。
① 导入pytesseract和Pillow。
② 打开图片。
③ 识别。
```
```py
# 通过以下代码来实现最简单的图片识别：
import pytesseract
from PIL import Image
image = Image.open('验证码.png')
code = pytesseract.image_to_string(image)
print(code)     
```

2、打码网站
在线验证码识别的网站，简称打码网站。这些网站有一些是使用深度学习技术识别验证码，有一些是雇佣了很多人来人肉识别验证码
网站提供了接口来实现验证码识别服务。使用打码网站理论上可以识别任何使用输入方式来验证的验证码
```
这种打码网站的流程一般是这样的。
① 将验证码上传到网站服务器。
② 网站服务器将验证码分发给打码工人。
③ 打码工人肉眼识别验证码并上传结果。
④ 网站将结果返回。
```
*使用在线打码*
在百度或者谷歌上面搜索“验证码在线识别”，就可以找到很多提供在线打码的网站。但是由于一般这种打码网站是需要交费才能使用的，所以要注意财产安全

## 8.3 案例-自动登录果壳网
[目标网站](https://www.guokr.com)
使用模拟登录与验证码识别的技术实现自动登录果壳网。 果壳网的登录界面有验证码，请使用人工或者在线打码的方式识别验证码，并让爬虫登录。登录以后可以正确显示“个人资料设置”界面的源代码
- 涉及的知识点：
- （1）爬虫识别验证码。
- （2）爬虫模拟登录。
>来自[第八章](https://github.com/kingname/SourceCodeOfBook/tree/master/%E7%AC%AC8%E7%AB%A0/program)，需要使用再来深度学习

