---
title: 前端开发的基础知识
top: false
toc: true
cover: false
date: 2020-03-25 12:04:47
categories: 学习力
tags:
  - 前端
  - Note
summary: 学习前端前的基础知识，对，没错，就是html、css和js
password:
---

<!--more-->

**参考资料**（大佬的笔记）

> [HTML](https://blog.csdn.net/wuyxinu/article/details/103515157)
> [CSS](https://blog.csdn.net/wuyxinu/article/details/103583618)
> [JS](https://blog.csdn.net/wuyxinu/article/details/103642800)
> [JS-下](https://blog.csdn.net/wuyxinu/article/details/103646041)
> 还有 [jQuery](https://blog.csdn.net/wuyxinu/article/details/103669718)
> [Node.js+Gulp](https://blog.csdn.net/wuyxinu/article/details/103774211)

**学习思路**
* [x] HTML 入门 
* [ ] CSS 入门 
* [ ] HTML 进阶 
* [ ] CSS 进阶 
* [ ] JavaScript 入门
* [ ] jQuery 入门 
* [ ] ASP.NET 入门（或 PHP 入门）
* [ ] Ajax
* [ ] ASP.NET 进阶（或 PHP 进阶）

# 1. html/html5 的基础

- **1、什么是 HTML?**
  HTML 是用来描述网页的一种语言
  HTML 指超文本标记语言( Hyper Text Markup Language)
  HTML 不是编程语言,是一种标记语言
- 2、**HTML5 的新特性**
  用于绘画的 canvas 标签
  用于媒介回放的 vdeo 和 audo 元素
  对本地离线储存的更好支持
  新的特殊内容元素,如: article、 footer、 header、nav、 section
  新的表单控件如: calendar、date、time、emai、url、 search

## 1.1 html 基础结构

```html
<!DOCTYPE html>
<html>  #html file
<head>
    <title></title>
    <meta></meta>

</head>
<body> #html main
<h1 align = "center">    <!--head first    居中center   h1~6-->
<p>	#paragraph
<a href = "http://wfaief.com">this is a link</a>
</p>
</h1>
</body>
</html>
```

## 1.2 页头 head

- title 定义网页的标题
- meta 定义网页的基本信息
- style 定义 css 样式
- link 定义链接外部 css 文件或脚本文件

* script 定义脚本语言
* base 定义页面所有链接的基本定位

## 1.3 页身 body

### 1.3.1 段落与文字

- 段落
  - h1~h6 多级标题
  - p 段落
  - br 换行`<br/>`
  - hr 水平线`<hr/>`
  - div 分割-块元素
  - span 区域-行内元素
- 文字
  - strong 加强-粗体
  - em 强调-斜体
  - cite 引用
  - sup 上标
  - sub 下标
- 网页特殊符号
  - `&nbsp;`空格

*div和span没有任何语义,正是因为没有语义，这两个标签一般都是配合CSS来定义元素 样式的*
* div是块元素，可以包含任何块元素和行内元素，不会与其他元素位于同一行；span 是行内元素，可以与其他行内元素位于同一行。

* div常用于页面中较大块的结构划分，然后配合CSS来操作；span 一般用来包含文字等, 它没有结构的意义，纯粹是应用样式。当其他行内元素都不适合的时候，可以用span来配合CSS 操作

### 1.3.2 列表

- ol 有序列表

```html
<ol>
  <li>有序列表项</li>
  <li>有序列表项</li>
  <li>有序列表项</li>
</ol>

type 属性： 数字 123--- 小写字母 abc--- 大写字母 ABC--- 小写罗马数字
i、ii、iii…… 大写罗马数字 I、II、III……
```

- ul 无序列表（重点）

```html
<ul type="列表项符号">
  <li>无序列表项</li>
  <li>无序列表项</li>
  <li>无序列表项</li>
</ul>

type 属性值 disc 默认值，实心圆“●” circle 空心圆“○” square 实心正方形“■”
```

- dl 定义列表

```html
<dl>
  <dt>定义名词</dt>
  <dd>定义描述</dd>
  ……
</dl>
```

### 1.3.3 表格

- 基本结构

  - table 表格
  - tr 表格行
  - td 单元格

- 完整结构
  - caption 标题
  - thead 表头
  - th 表头单元格
  - tbody 表身
  - tfoot 表脚
  - td rowspan 合并行
    `<td rowspan="跨度的行数">`
  - td colspan 合并列
    `<td colspan="跨度的列数">`

```html
<table
    <cation>表格标题</cation>
    <!--头-->
    <thead>
        <tr>
            <th>表头单元格1</th>
    <th>表头单元格2</th>
        </tr>
    </thead>
    <!--表身-->
    <tbody>
        <tr>
            <td>标准单元格1</td>
            <td>标准单元格2</td>
        </tr>
        <tr>
            <td>标准单元格1</td>
            <td>标准单元格2</td>
        </tr>
    </tbody>
    <!--表脚-->
    <tfoot>
        <tr>
            <td>标准单元格1</td>
            <td>标准单元格2</td>
        </tr>
    </tfoot>
</table>
```

### 1.3.4 图像

`<img src="图片地址" alt="图片描述（给搜索引擎看）" title="图片描述">`

- src 图像的文件地址
- alt 图片显示不出来时提示的文字
- title 鼠标移动到图片上的提示文字

### 1.3.5 链接

- href 链接

```html
<a href="链接地址" target="目标窗口的打开方式">
  target 属性值 \_self 默认方式，即在当前窗口打开链接 \_blank
  在一个全新的空白窗口中打开链接 \_top 在顶层框架中打开链接 \_parent
  在当前框架的上一层里打开链接</a
>
```

- 内部链接

- 锚点链接

```html
<a href="#music">推荐音乐</a><br />
<div id="music"></div>
```

- 内部页面链接

- 外部链接

### 1.3.6 表单

- input 的 type 中的属性
  `<input type="表单类型"/>`

```
- text单行文本框
- password密码文本框
- button按钮
- reset重置按钮
- image图像形式的提交按钮
- radio单选按钮
- checkbox复选框
- hidden隐藏字段
- file文件上传
```

- textarea
  `<textarea rows="行数" cols="列数">多行文本框内容</textarea>` 多行文本框

- select
- option

```html
<select multiple="mutiple" size="可见列表项的数目">
  <option value="选项值" selected="selected">选项显示的内容</option>
  ……
  <option value="选项值">选项显示的内容</option>
</select>
```

### 1.3.7 多媒体

- embed 音频视频
  `<embed src="多媒体文件地址" width="播放界面的宽度" height="播放界面的高度"></embed>`
  src 可以是绝对地址也可以是相对地址
  width 和 height 使用 px 作为单位

- bgsound 背景音乐-只适用 ie 浏览器
  `<bgsound src="背景音乐的地址"/>`

loop="2"表示重复 2 次，loop="infinite"表示无限次循环播放，也可以使用 loop="-1"表示无限次循环播放。

### 1.3.8 浮动框架

浮动框架是一种较为特殊的框架，它是在浏览器窗口中嵌套的子窗口，整个页面并不一定是框架页面，但要包含一个框架窗口

- iframe

```html
<iframe
  src="浮动框架的源文件"
  width="浮动框架的宽"
  height="浮动框架的高"
></iframe>
width、height宽高 scrolling滚动条

<iframe
  src="浮动框架的源文件"
  width="浮动框架的宽"
  height="浮动框架的高"
  scrolling="取值"
></iframe>
```

取值

- auto 默认整个表格左对齐
- yes 总是显示滚动条
- no 任何情况不显示滚动条

## 1.4 HTML XHTML HTML5 简介

### 1.4.1 XHTML

xhtml 比 html 更加严格

- 1、XHTML 标签必须闭合
- 2、XHTML 标签以及属性必须小写
- 3、XHTML 标签属性必须用引号
- 4、XHTML 标签用 jd 属性代替 name 属

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title></title>
  </head>
  <body>
    <p>
      “<span style="font-weight:bold;color:Red;">视觉化思考</span>”能以独特而有效的方式，让你的心有更大的空间来解决问题。
    </p>
  </body>
</html>
```

### 1.4.2 HTML5

HTML 5 除了新增部分标签之外，还增加了一组技术，包括 canvas、SVG、WebSocket.本地存储等。这些新增的技术都是使用 JavaScript 来操作。也就是说，HTML 5 使得 HTML 从一门“标记语言” 转变为一门 **“编程语言”**

* 声明更简洁 `<!DOCTYPE html>`
* 不再区分大小写 `<div>绿叶学习网</DIV>`
* 允许属性值不加引号 `<div id=wrapper style=co1or: red> 绿叶学习网 </div>`
* 允许部分属性的属性值省略
  * 
```html
<input type="ntext" readonly/>
<input type="checkbox" checked/>
```

| 省略形式 | 等价于                |
| -------- | --------------------- |
| checked  | checked="nchecked"    |
| readonly | readonly="readonly"   |
| defer    | defer="defer"         |
| ismap    | ismap="ismap"         |
| nohref   | nohref="nohref"       |
| noshade  | noshade="noshade"     |
| nowrap   | nowrap="nowrap"       |
| selected | selected="selected"   |
| disabled | ciisabled="disableci" |
| multiple | multiple="multiple"   |
| noresize | noresize="disabled"   |


## 1.5 知识点

### 1.5.1 class与id

class,顾名思义，就是“类”。它釆用的思想跟C、Java等编程语言中的“类”相似。 我们可以为同一个页面的相同元素或者不同元素设置相同的class,然后使得相同class的元 素具有相同的CSS样式

**可以用多类名**，**用空格隔开**
eg: `<h1 class="title tac">文章总标题</h1>`

id属性具有唯一性，也就是说在一个页面中相同的id只允许出现一次
W3C建议，对 于页面关键的结构或者大结构，我们才使用id。所谓的关键结构，指的是诸如LOGO、导航、 主体内容、底部信息栏等结构。对于一些小地方，还是建议使用class属性

### 1.5.2 浏览器标题栏小图标

放在head里面

`<link rel="shortcut icon" type="image/x-icon" href="favicon.icon"/>`

### 1.5.3 语义化
即尽可能地不使用div来编写，用自带的语句来编写

- 标题语义化
  - （1）一个页面只能有一个h1标签
  - （2）hl ~ h6之间不要断层
  - （3）不要用h1 ~ h6来定义样式
  - （4）不要用div来代替h1 ~ h6.

- 图片语义化
  - （1） alt属性和title属性
```html
<img src="" alt="图片描述(给搜索引擎看)" title="图片描述(给用户看)">
````
  - （2） figure 元素和 figcaption 元素
```html
<figure>
    <img src="" alt=""/>
    <figcaption>图注文字</figcaption>
</figure>
```
- 表格语义化（在实际开发中，我们不建议使用表格布局，应该使用浮动布局或者定位布局）
  - th表示“表头单元格”
  - caption表示“表格标题”
  - thead、tbody和tfoot这3个标签把表格从语义上分为三部分: 表头、表身和表脚
  ```html
  <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    
    <head>
        <style type="text/css">
            .body {
                font-family: "微软雅黑";
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class='content'>
            <table>
                
                <caption> 表格标题 </caption> 
                <!--表头-->
                <thead>
                <tr>
                <th>表头单元格l</th>
                <th>表头单元格2</th> </tr>
                </thead>
                <!--表身-->
                <tbody>
                <tr>
                <td>标准单元格l</td>
                <td>标准单元格2</td> </tr>
                <tr>
                <td>标准单元格l</td>
                <td>标准单元格2</td> </tr>
                </tbody>
                <!--表脚-->
                <tfoot>
                <tr>
                <td>标准单元格l</td>
                <td>标准单元格2</td> </tr>
                </tfoot>
                </table>
        </div>
    </body>
    </html>
  ```

- 表单语义化
  - （1）label 标签
  - （2）fieldset 标签和 legend 标签
  ```html
  <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    
    <head>
        <title></title>
    </head>
    
    <body>
        <form action="index.aspx" method="post">
            <fieldset>
                <legend>登录绿叶学习网</legend>
                <p>
                    <label for="name"> 账号：</label><input type="text" id="name" name="name" />
                </p>
                <label for="pwd"> 密码：</label><input type="password" id="pwd" name="pwd" />
                </p>
                <input type="checkbox" id="remember-me" name="remember-me" /> <label for="remember-me"> 记住我 </label>
                <input type="submit" value="登录" />
    
            </fieldset>
        </form>
    </body>
    </html>
  ```

- 其他语义化
  - 换行符 `<br/>`只适合用于p标签内 部的换行，不能用于其他标签
  - 在实际开发中，大多数情况下都是使用无序列表ul，极少情况下会使用有序列表
  - strong标签和em标签 <strong>加粗</strong>和<em>斜体</em>
  - del标签和ins标签   <del>删除线</del> 和 <ins>下划线</ins>
  - img标签

- 语义化验证：去掉css，要有好的可读性

- html5删除地标签

| 标签     | 说明                              |
| :------- | --------------------------------- |
| basefont | 定义页面文本默认字体，颜色，尺寸  |
| big      | 定义大字号文本                    |
| center   | 定义文本居中                      |
| font     | 定义文本的字体样式                |
| strike   | 定义删除线文本                    |
| s        | 定义删除线文本                    |
| u        | 定义下划线文本                    |
| dir      | 定义目录列表，应该用ul代替        |
| acronym  | 定义首字母缩写，应该用abbr代替    |
| isindex  | 定义与文档相关的可搜索索引        |
| applet   | 定义嵌入的applet,应该用object代替 |
| frame    | 定义frameset中的一个特定的框架    |
| frameset | 定义一个框架集                    |
| noframes | 为那些不支持框架的浏览器显示文本  |

## 1.6 HTML5

### 1.6.1 新的语义化标签

* header头部标签
* nav导航标签
* article内容标签
* section块级标签
* aside侧边栏标签
* footer尾部标签

### 1.6.2 多媒体音频标签

* audio音频
可以在不使用标签的情况下，也能够原生的支持音频格式文件的播放，但是：播放格式是有限的
  * autoplay自动播放
  * controls出现该属性，则向用户显示控件
  * loop每当音频结束时自动重新播放
  * src音频地url

```html
<audio controls>
    <source src="./media/snow.mp3" type="audio/mpeg" />
</audio>
```
* video视频
  * autoplay自动播放
  * controls出现该属性，则向用户显示控件
  * width px 宽
  * height px 高
  * loop每当音频结束时自动重新播放
  * src音频地url
  * preload 预先加载
  * poster 加载等待地画面图片imgurl
  * muted 静音播放

```html

<body>
  <!-- <video src="./media/video.mp4" controls="controls"></video> -->
​
  <!-- 谷歌浏览器禁用了自动播放功能，如果想自动播放，需要添加 muted 属性 -->
  <video controls="controls" autoplay muted loop poster="./media/pig.jpg">
    <source src="./media/video.mp4" type="video/mp4">
    <source src="./media/video.ogg" type="video/ogg">
  </video>
</body>
```
### 1.6.3 新增 input 标签

![input标签](https://img-blog.csdnimg.cn/20191229133014181.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1eXhpbnU=,size_16,color_FFFFFF,t_70)

### 1.6.4 新增表单属性

![表单属性](https://img-blog.csdnimg.cn/20191229133048182.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1eXhpbnU=,size_16,color_FFFFFF,t_70)


# 2. css 的基础

CSS是什么？CSS，即“Cascading Style Sheet（层叠样式表）”，是用来控制网页的外观的一门技术

## 2.1 css的引入

外部样式表、内部样式表、内联样式表

### 2.1.1 外部样式表

把CSS代码和HTML代码都单独放在不同文件中，然后在HTML文档中使用link标签来引用CSS样式表

外部样式表都是在head标签内使用link标签来引用的

```html
<head>
    <link href="css文件路径" rel="stylesheet" type="text/css" />
</head>
```

### 2.1.2 内部样式表

指的就是把CSS代码和HTML代码放在同一个文件中，其中CSS代码是放在**标签对内的**

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>  
    <title></title>    
    <!--这是内部样式表，CSS样式在style标签中定义-->    
    <style type="text/css">
          p{color:Red;}      
    </style>
</head>
<body>   
    <p>绿叶学习网</p>  
    <p>绿叶学习网</p>
</body>
```

### 2.1.3 内联样式表(行内式)

也是把CSS代码和HTML代码放在同一个文件中，但是跟内部样式表不同，CSS样式不是在<style></style>标签对中定义，而是**在标签的style属性中定义**

```html
<!DOCTYPE html> 
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title></title>
</head>
<body>
    <p style="color:Red; ">绿叶学习网</p>
    <p style="color:Red; ">绿叶学习网</p>
    <p style="color:Red; ">绿叶学习网</p>
</body>
</html>
```

## 2.2 元素的id和class

id属性是唯一的，class可以有多个
`<div id="first">绿叶学习网</div>`
```html
<div class="first">绿叶学习网</div>
<p class="first">绿叶学习网</p>
```

## 2.3 CSS选择器

将想要的标签选中，然后再操作标签

选择器
```css
选择器{
    样式属性1:取值1;
    样式属性2:取值2;
    ……
}
/*注释*/
```

### 2.3.1 基本选择器

#### 2.3.1.1 元素选择器

```css
div {width:100px; height:100px;}
元素符号 {属性:属性值}
```

#### 2.3.1.2 id选择器

```css
#box {width:100px}
#id属性值 {属性:属性值}
```

#### 2.3.1.3 class选择器

```css
.red {width:100px}
.class属性值 {属性:属性值}
```

#### 2.3.2.2 子元素选择器

```css
#father1 #p1 {color:red;}
#父元素选择 #子元素选择 {属性:属性值}

<div id="father1">
    <div id="p1">绿叶学习网</div>
    <div>绿叶学习网</div>
</div>
```

#### 2.3.2.5 相邻选择器

```css
#lv + div {color:red;}
#元素a + 元素a相邻的兄弟元素 {属性:属性值}

则是第三个div文本为红色red
<div>绿叶学习网</div>
<div id="lv">
    <p>绿叶学习网</p>
</div>
<div>绿叶学习网</div>
<div>绿叶学习网</div>
```

#### 2.3.2.6 群组选择器

```css
h3,div,p,span {color:red;}
```

### 2.3.2 复合选择器

#### 2.3.2.1 后代选择器

```css
.class h3 {
  color: red;
}
h3是div的后代，div的元素名为class

#father1 #p1 {color:red;}
#父元素选择 #子元素选择 {属性:属性值}

<div id="father1">
    <div id="p1">绿叶学习网</div>
    <div>绿叶学习网</div>
</div>
```

#### 2.3.2.2 子元素选择器

**只选择儿子**，**不会选择所有的后代**
```css
/* 子代选择器 */
.class>h3 {
  color: red;
}
```

#### 2.3.2.3 交集选择器

既是p标签 又是.red类 关系

```css
p.red {
  color:red;
}
```

#### 2.3.2.4 并集选择器(群组选择器)

样式相同时，用并集选择
```css
p,span,.red,#id {
  color:red;
}
```

#### 2.3.2.5 链接伪类选择器

##### 2.3.2.5.1 伪选择器

类选择器 `.demo`
伪类选择器 `:demo`
为链接添加一些特殊效果

##### 2.3.2.5.2 链接伪类选择器

* a:link 未访问链接
* a:visited 已访问链接
* a:hover 鼠标移动到链接上
* a:active 选定链接

顺序不能颠倒：lvha
也算是交集选择器的变种
实际开发，都是先用一个总的a风格，然后只是写a:hover

```css
a:link {
  color: #333;
}
a:visited {
  color: #9ca7a5;
}
a:hover {
  color: red;
}
a:active {
  color: green;
}

/* 子代选择，只是nav中的链接有hover样式 */
.nav a:hover {
  color: red;
}
```

## 2.4 CSS的font文本样式

* font-family 字体名：微软雅黑等等
`font-family:微软雅黑;` 还有 `宋体` `Times New Roman等等`

```css
h1 {
	color: deeppink;
	font-size: xx-large;
	font-family: JetBrains Mono,"幼圆","microsoft yahei","微软雅黑";
	/*多个字体用逗号隔开，从开始寻找字体：如果第一个没有，用第二个，如果都没有，用默认字体*/
	/*中文字体需要引号，英文字体无特殊字符，不需要引号*/
  font-family: "\5FAE\8F6F\96C5\9ED1"   /*= 微软雅黑*/
  /*Unicode字体，可以查表*/
}
```

* font-size 字体大小: px/百分比/em
`font-size:15px;` 一般都用px，像素

* font-weight 字体粗细
`font-weight:bold;` `normal` `100~900   400为normal，700为bold`
用数字更好

* font-style 字体斜体
`font-style:italic;`斜体 `oblique`特殊字体（无italic变量） `normal`默认

* color 颜色
`color:blue;` `color:#000000;`

**综合性font语法**
```css
.imporp {
	font: initial 700 20px "幼圆";
}

也就是:
.xuanze {
  font: font-style font-weight font-size font-family;
}
```

## 2.5 CSS的外观属性

### 2.5.1 color文本颜色

* 预定义颜色：red，green，blue，pink等等
* 十六进制：#FF0000，#000000黑色，#ffffff白色，#ff0000红色
  * 简写：#ccc   由 #cccccc简写，两两相同
* RGB颜色：`rgb(255,0,0)` `rgb(100%,0%,0%)`

### 2.5.2 文本水平对齐方式

`text-align:` 
left 左对齐（默认）
right 右对齐
center 居中对齐

### 2.5.3 行间距

`line-height:`
em 百分比 px
一般用像素px，作为单位，一般行距比字号大7、8像素

### 2.5.4 首行缩进

`text-indent:` ， em为常用单位
为字符单位的倍数，如1em为一个字的宽度

### 2.5.5 文本的装饰

`text-decoration:` 去掉连接下划线
none 默认，无装饰
blink 闪烁
underline 下划线
line-through 删除线
overline 上划线

## 2.6 标签的显示模式

**这节是重点**

### 2.6.1 标签的显示模式

div只能自己占一行，可以把多个span放到一行，a链接也可以一行放多个

块标签和行标签

### 2.6.2 块级元素
`block-level`

h1~h6、p、div、ul、ol、li等，div是典型

* 高度、宽度、外边距、内边距都可以控制（可以自己设置）
* 宽度默认为容器（父级宽度）的100%
* 里面可以放行内或者块级元素
* p、h1~h6、dt不能放块级元素，p不能放div

### 2.6.3 行内元素
`inline-level`

a、strong、b、em、i、del、s、ins、u、span等，span典型

* 相邻行内元素再一行上、一行可以显示多个
* 高宽不能直接设置
* 默认宽度就是它本身的宽度,与文本内容多少有关
* 行内元素只能容纳文本或者其他行内元素
* 链接里面不能再含有链接
* 特殊情况：a内可以放块级元素，但给a转换一下块级模式更加安全

### 2.6.4 行内块元素
`inline-block`

img、input表单类、td单元格等，可以对他们设置宽高和对齐属性

* 和相邻的行内元素在一行上、但会有空白缝隙，一行可以显示多个
* 默认宽度和高度是本身内容的宽度
* 高度、行高、外边距、内边距可以控制

### 2.6.5 显示模式转换display

* 块转换为行：`display:inline;`
* 行转换为块：`display:block;`
* 块、行转换为行内块：`display:inline-block`

## 2.7 行高line-height

可以间接让文字垂直居中

### 2.7.1 行高测量

行高测量：有英文的话基线与基线间的距离、中文可以直接量底线
![行高测量](/img/hcj/hgcl.png)

### 2.7.2 单行文本垂直居中

上距离+文字高度+下距离 = 块高

**行高**
**等于高度**，**文字垂直居中**
大于高度，文字偏下
小于高度，文字偏上

## 2.8 CSS背景background

### 2.8.1 背景颜色color

`-color:`
transparent透明色--默认透明

### 2.8.2 背景图片image

`background-image: url(images/1.jpg)`
默认url为none,url中的地址不用加引号

### 2.8.3 背景平铺repeat

`background-repeat:`
默认repeat 平铺
no-repeat 不平铺
repeat-x 横向平铺
repeat-y 纵向平铺

### 2.8.4 背景位置position（重点）

`background-position:`
length 百分数，浮点数子和单位标识符组成的长度值
position后面是完整的位置坐标，可以加方位名词或者数字
* 方位名词：`right top;` 右上角,,left,bottom,center
  * `left top` 与 `top left`效果相同，顺序无关
  * 只写一个的话，另一个默认居中

常用的超大背景图片`center top`

* 数字坐标： `x坐标 y坐标;`,如`10px 50px;`
  * 第一个为x坐标，第二个为y坐标，顺序有关
  * 只给一个值，则默认为x坐标，另一个默认居中
  * 如果精确和方位混合使用，则精确值第一个为x，第二个为y

### 2.8.5 背景附着

`background-attachment:`
`scroll` 滚动
`fixed` 固定

### 2.8.6 背景简写

`background: transparent url(image.jpg) repeat-y scroll center top;`
`background:`背景颜色 图片地址 背景平铺 背景滚动 背景位置;

### 2.8.7 背景透明（CSS3）

黑色半透明，rgba(red,green,blue,alpha)
alpha：透明度0~1

`background: rgba(0,0,0,0.3);`
* 简略显示`rgba(0,0,0,.3)`
* 半透明只是盒子半透明，内容不受影响

## 2.9 CSS三大特性

### 2.9.1 CSS层叠性

通俗：前面有一个div属性，后面再写一个一样的，则会使用后面的

* 就近原则，那个样式离着结构近，就执行那个样式
* 样式不冲突，不会层叠

### 2.9.2 CSS继承性

```html
<style>
div {
  color: red;
}
</style>
<div>
<p>内容<p>
</div>
```
p中的内容也是red红色

* 恰当的使用继承可以让代码更加简洁
* text-，font-，line-，只有这些元素可以继承

### 2.9.3 CSS优先级（重点）

同一元素上有不同的规则
* 选择器相同，执行就近原则（层叠性）
* 选择器不同，如一个`div`，一个`.class`，两个选择器，选择`.class`

#### 2.9.3.1 权重计算公式
| 选择器           | 计算权重公式 |
| ---------------- | ------------ |
| 继承或者*        | 0,0,0,0      |
| 每个元素标签选择器       | 0,0,0,1      |
| 每个元素类选择器.        | 0,0,1,0      |
| 每个元素id选择器#        | 0,1,0,0      |
| 每个元素行内选择器style  | 1,0,0,0      |
| 直接用!important | 权重最高     |

最高权重的用法
```css
div {
  color: red!important;
}
```

**只要是继承权重一定为0**

* 如果该标签被选中，则比较权重
* 如果标签没有被选中，则始终为0

#### 2.9.3.2 权重计算叠加

交集选择器、后代选择器会出现权重叠加
如：
* `div ul li`   0,0,0,3
* `.nav ul li`  0,0,1,2
* `a:hover`  0,0,1,1
* `.nav a`  0,0,1,1

## 2.10 盒子模型（CSS重点）

### 2.10.1 盒子模型介绍

网页布局本质

* 设置好各个盒子的大小，摆放好盒子的位置
* 然后放内容（图片，文字等等）

**盒子模型Box Model**
* 盒子组成四部分：Border厚度（边缘），content内容，Padding内边距，Margin盒子与盒子间的距离（外边距）

![盒子模型](/img/hcj/boxmodel.png)

### 2.10.2 盒子边框border

综合性写法：`border: 1px solid pink;`没有顺序 

`border-width:` 默认medium，边框宽度px 
`border-style:` 边框样式，none，hidden，dotted点线，dashed虚线，**solid实线**
`border-color:` 颜色

#### 2.10.2.1 边框分开写

`border-top:` 上边框综合写法，具体写`border-top-width`等等
`border-bottom:` 下边框
`border-right:` 右边框
`border-left:` 左边框

例子
```css
input {
  /* border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 1px dashed pink;
    */
  border: none;
  border-bottom: 1px dashed red;
}
```

```html
用户名: <input type="text">
密码： <input type="text">
```

#### 2.10.2.2 表格的细线边框

表格的两个单元格在重合时会发生重叠，从而使得边框变粗

合并单元格：`table {border-collapse:collapse;}`
相邻边框合并在一起，而不会变粗

### 2.10.3 盒子内边距padding

单位px
`padding-left:`
`padding-right:`
`padding-top:`
`padding-bottom:`

* 内容和边框有了距离
* 添加内边距，盒子会变大
* 简写：
`padding: 20px;` 解释：上下左右都是20px的内边距
`padding: 10px 20px;`  上下10px，左右20px
`padding: 10px 20px 30px;` 上10px，左右20px，下30px
`padding: 10px 20px 30px 40px;` 上10 ，右20，下30，左40，顺时针

---

![新浪导航](/img/hcj/xldh.png)

给盒子指定一个padding而不给宽度，实现不同内容，不同宽度

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>xl</title>
	<style>
		.nav {
			height: 41px;
			background-color: rgb(252, 252, 252);
			border-top: 4px solid #dd5600;
			border-bottom: 1px solid #edefec;
		}
		.nav a {
			display: inline-block;
			height: 41px;
			/* background-color: pink; */
			text-decoration: none;
			padding: 0px 20px;
			line-height: 41px;
			color: #4c4c4c;
			font-size: 12px;
		}
		.nav a:hover {
			background-color: #eaedea;
		}
	</style>
</head>
<body>
	<div class="nav">
		<a href="#">设为首页</a>
		<a href="#">手机新浪网</a>
		<a href="#">移动客户端</a>
		<a href="#">博客</a>
		<a href="#">微博</a>
		<a href="#">关注我</a>
	</div>
</body>
</html>
```

---

**盒子模型的计算**

![盒子模型](/img/hcj/boxmodel.png)

**盒子的实际大小 = 内容宽度 高度 + 内边距 + 边框**

* `padding: 10px`会把盒子的宽高各增加20px
* 解决方法： 要让盒子保持原大小，则要修改width，height，减去内边距即可

特殊情况：padding不会撑开的情况
如果这个盒子没有宽度，则padding不会撑开盒子，盒子内的盒子不会撑开盒子

### 2.10.4 盒子的外边距margin

`margin-left:`
`margin-right:`
`margin-top:`
`margin-bottom:`
简写，与padding一样
`margin: 10px` 上下左右

#### 2.10.4.1 块级盒子居中对齐

居中对齐：有宽度、左右外边距设为`auto`
* 第一种写法
`width: 600px;`
`margin-left: auto;`
`margin-right: auto;`

* 第二种写法
`margin: auto;`

* 第三种写法
`margin: 0 auto;`
上下为`0` ，左右`auto`

#### 2.10.4.2 文字居中，盒子居中

* 文字水平居中：`text-aligh: center;`
也可以让行内元素和行内块元素居中对齐

* 盒子水平居中：`margin: 10px auto;`

#### 2.10.4.3 插入图片和背景图片

通常用插入图片
* 插入图片`<img src="url" alt="">`
移动位置只能通过盒模型`padding`或`margin`值来移动

背景图片很少用，小图标或者超大背景
* 背景图片`background-image: url(url);`
移动位置只能用`background-position: x,y;`


#### 2.10.4.4 清除元素默认的内外边距（写css第一句代码，很重要）

```css
* {
  padding: 0;
  margin: 0;
}
```

* 一些元素有默认的内外边距，要美观就要删掉
* **行内标签，尽量只设置左右内外边距，不设置上下内外边距（不管用）**

#### 2.10.4.5 外边距合并
1. 
  * 相邻块元素垂直外边距合并，取两个值中的较大值（外边距塌陷）
  * 解决方法：尽量只给一个盒子添加margin值
2. 
  * 嵌套关系的垂直外边距合并，（塌陷）父子级关系，给儿子一个margin，父亲也会有margin
  * 解决方案
    * 为父元素指定外边框`border-top:`
    * 为父元素指定一个上`padding-top:`
    * 为父元素添加`overflow: hidden;`

#### 2.10.4.6 盒子模型的布局稳定性

优先级使用，先宽度width，然后内边距padding，最后外边距margin

### 2.10.5 盒子综合案例

![盒子综合案例](/img/hcj/boxlizi.png)

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>盒子综合案例</title>
	<style>
		* {
			padding: 0;
			margin: 0;
		}
		.box {
			width: 298px;
			height: 198px;
			border: 1px solid #ccc;
			margin: 100px auto; /* 水平居中 */
			background: url(../images/1.ico);
			padding: 15px;
		}
		.box ul li {
			/* 去掉列表样式 */
			list-style: none;
			height: 30px;
			border-bottom: 1px dashed #ccc;
			line-height: 30px;
			background: url(../images/1.ico) no-repeat 5px center;
			/* background-position: 5px center; */
			padding-left: 20px;
		}
		.box ul li a {
			text-decoration: none;
			font-size: 12px;
			color: #2a2a29;
			/* margin-left: 20px; */
			/* padding-left: 20px; */
		}
		.box ul li a:hover {
			text-decoration: underline;
		}
		.box h2 {
			font-size: 18px;
			padding: 5px 0;
			border-bottom: 1px solid #ccc;
			margin-bottom: 10px;
		}
	</style>
</head>
<body>
	<div class="box">
		<h2>最新文章/New Articles</h2>
		<ul>
			<li><a href="#">北京招聘</a></li>
			<li><a href="#">体验js</a></li>
			<li><a href="#">jquery</a></li>
			<li><a href="#">网页设计师</a></li>
			<li><a href="#">链式编程</a></li>
		</ul>
	</div>
</body>
</html>
```

**去掉列表默认的样式（前面的小点）**
无序列表和有序列表列表样式在不同浏览器显示样式不一样所以去掉
`li { list-style: none; }`

### 2.10.6 拓展CSS3

#### 2.10.6.1 边框圆角

`border-radius: length`
length可以为数值或百分比

横向矩形为高度一般设置为高度的一半

#### 2.10.6.2 盒子阴影

`box-shadow: 水平阴影 垂直阴影 模糊距离(虚实) 阴影尺寸(大小) 阴影颜色 内外阴影`
`h-shadow v-shadow`前两个必须写
`blur spread color inset`可以省略
内外阴影默认为outset，且不用写

`美观的` `box-shadow: 0 15px 30px rgba(0,0,0,.3);`

```css
width: 300px;
height: 300px;
background-color: pink;
margin-left: auto;
margin-right: auto;
text-align: center;
/* border-radius: 150px; */
border-radius: 20%;
box-shadow: 2px 2px 2px 2px #000 ;
```

![picture](/img/hcj/shadow.png)

## 2.11 CSS书写规范

**空格规范**

* `选择器`与`{}`之间有空格
* 属性的`冒号`跟`值`有空格

**选择器规范**

* 并集选择器竖着写
* 花括号对齐
* 选择器嵌套层数最好不超过3级

**属性规范**

* 属性必须另起一行
* 属性定义后必须有`;`结束

### 2.11.1 CSS属性书写顺序（重点）

按照顺序书写

1. 布局定位属性：`display / position / float / clear / visibility / overflow` （display第一个写）
2. 自身属性： `width / height / margin / padding / border / background /`
3. 文本属性： `color / font / text-decoration / text-align / vertical-align / white-space / break-word`
4. 其他属性（CSS3）： `content / cursor / border-radius / box-shadow / text-shadow / background:linear-gradient ...` 

## 2.12 浮动float

布局页面

### 2.12.1 CSS布局的三种机制

网页布局的核心就是用CSS来摆放盒子

三种方法：
* 普通流

块级元素会独占一行，从上向下顺序排序
`div、hr、p、h1~h6、ul、ol、dl、form、table`

行内元素会多个在一行内显示，从左到右，碰到父元素边缘自动换行
`span、a、i、em`

* 浮动流

让盒子从普通流中浮动起来，主要作用让多个块级盒子一行显示

* 定位流

将盒子定在浏览器中的某一个位置，CSS离不开定位，特别是后面的js特效

### 2.12.2 浮动

#### **1. 为什么用浮动？？？**

* 让多个盒子水平排列成一行

&emsp;行内块也可以让多个块水平排列在一行`display: inline-block`，**但中间会有一个空隙，而且很难去掉，也不能简单地调整空隙大小,但浮动可以实现**

* 实现盒子的左右对齐

#### **2. 什么是浮动？？？**

设置了浮动属性地元素：
* 脱离标准普通流地控制
* 移动到指定地位置

#### **3. 浮动的作用**：
* 让多个盒子div水平排列成一行
* 可以实现盒子地左右对齐
* 最早是用来控制图片，实现**文字环绕图片**的效果

#### **4. 浮动的语法**

float属性定义浮动
```css
选择器 {
  float: none
}

/* none 、 left 、 right  */
/* 不浮动 、 左浮 、 右浮 */
```

#### **5. 浮动的口诀**

**浮**
漂浮在普通流的上面，脱离标准流，*脱标*
float让盒子漂浮在标准流的上面，所以第二个标准流的盒子跑到浮动盒子的地下

![浮动](/img/hcj/float.png)

**漏**
浮动的盒子原来的位置留给下面标准流的盒子，不占有原来的位置

**特**
float特性，float会改变元素的display属性
任何元素都可以浮动，浮动的元素会生成一个块级框，而不论他本身是什么元素，生成的块级框跟行内块相似

两个块元素都给上float属性，会都转化为**行内块元素，而且中间没有空隙**

**浮动的盒子会相互靠在一起，如果父级宽度装不下这些浮动的盒子，多出的盒子会另起一行对齐**

#### **6. 浮动的应用(重点)**

浮动流和标准流的父盒子的搭配
先给定一个标准流的父级盒子，然后浮动流在标准流中浮动
**完整的网页 = 标准流 + 浮动 + 定位**

![浮动案例](/img/hcj/floatex1.png)

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Float</title>
	<style>
		* {
			padding: 0;
			margin: 0;
		}
		.box {
			width: 1226px;
			height: 615px;
			background-color: #CCCCCC;
			margin: auto;
			margin-top: 30px;
		}
		.left {
			width: 234px;
			height: 615px;
			background-color: #f7ebcd;
			float: left;
		}
		.left img {
			width: 234px;
		}
		.right {
			width: 992px;
			height: 615px;
			background-color: skyblue;
			float: right;
		}
		.right li {
			/* 清除列表样式 */
			list-style: none;	
			width: 234px;
			height: 300px;
			background-color: pink;
			float: left;
			margin-left: 14px;
			margin-bottom: 14px;
		}
	</style>
</head>
<body>
	<div class="box">
		<div class="left"><img src="../images/1.ico" alt=""></div>
		<ul class="right">
			<li>1</li>
			<li>2</li>
			<li>3</li>
			<li>4</li>
			<li>5</li>
			<li>6</li>
			<li>7</li>
			<li>8</li>
		</ul>
	</div>
</body>
</html>
```

![浮动导航栏案例](/img/hcj/floatex2.png)

**导航栏用li+a搭配更好**

```html
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>导航栏</title>
	<style>
		* {
			padding: 0;
			margin: 0;
		}
		li {
			list-style: none;
		}
		.banner {
			width: 760px;
			height: 150px;
			background-color: #CCCCCC;
			margin: auto;
		}
		.banner img {
			width: 760px;
		}
		.nav {
			width: 760px;
			height: 32px;
			background-color: pink;
			margin: 0 auto;
			background-image: url(../images/dhl.png) ;
			background-repeat: repeat-x;
		}
		.nav ul li {
			float: left;
		}
		/* 可以给a和li大小,但是a要求hover,所以要直接给a大小 */
		.nav ul li a {
			text-decoration: none;
			display: block;
			width: 80px;
			height: 32px;
			background: url(../images/banner0.png) no-repeat; 
			
			line-height: 32px;
			text-align: center;
			
			color: #3b4300;
			font-size: 12px;
		}
		.nav ul li a:hover {
			background: url(../images/banner1.png) no-repeat;
		}
	</style>
</head>
<body>
	<!-- banner广告条 -->
	<div class="banner"><img src="../images/banner.png" ></div>
	<div class="nav">
		<!-- 重要的导航栏用li+a的写法 -->
		<ul>
			<li><a href="#">网站首页</a></li>
			<li><a href="#">网站首页</a></li>
			<li><a href="#">网站首页</a></li>
			<li><a href="#">网站首页</a></li>
			<li><a href="#">网站首页</a></li>
			<li><a href="#">网站首页</a></li>
		</ul>
	</div>
</body>
</html>
```

#### **7. 浮动的扩展**

![浮动元素与父盒子的关系](/img/hcj/floatkz.png)

* 浮动元素与父盒子的关系
  * 子盒子的浮动参考父盒子对齐
  * 不会与父元素的边框重叠，也不会超过父盒子的内边距

![浮动元素与父盒子的关系](/img/hcj/floatkz1.png)
![浮动元素与父盒子的关系](/img/hcj/floatkz2.png)

两个都不浮动，则就两行显示，跟1不浮动、2浮动一样

* 浮动元素与兄弟盒子的关系，在一个父级盒子中，如果前一个兄弟盒子是
  * 浮动的，那么当前盒子会与钱一个盒子顶部对齐（1、2都浮动）
  * 普通流的，那么当前盒子会显示正在前一个兄弟盒子的下方（1不浮动、2浮动）

**一个父盒子中有很多盒子，如果其中一个盒子浮动，其他也应该浮动，防止出现问题**

### 2.12.3 清除浮动

#### 1. 为什么要清除浮动？？？

**父级盒子很多情况下，不方便给出高度**，但是子盒子如果浮动就不会占用位置，最后父级盒子的高度为0，就会影响下面的标准流盒子

正常的标准流盒子会把没有固定高度的父盒子撑开，而浮动的盒子不会撑开父亲
不方便给高度：固定的样式，内容不同的情况下

#### 2. 清除浮动

主要是解决浮动元素撑不开**未给高度的父盒子**的问题，清除浮动后，父级会根据浮动的子盒子自动检测高度

#### 3. 清除浮动的方法

`clear: 属性值;`
`left清除左侧浮动影响 right both`
一般直接用`clear: both`

##### ① 额外标签法（隔墙法）

在浮动元素末尾添加一个空的标签

`<div style="clear: both"></div>`或者其他如`<br>`标签等

* 缺点： 添加了许多无意义标签，结构性差

##### ② 父级添加overflow属性方法

给父级添加`overflow`为`hidden` `auto` `scroll` 都可以
`overflow: hidden;`
auto生成滚动条，scroll生成两个滚动条

代码简洁，但是内容增多时荣一造成不会自动换行而导致内容被隐藏掉，无法显示需要溢出的元素

##### ③ 使用after伪元素清除浮动

after方式为空元素添加额外标签的升级版，不用单独添加标签

相当于给这个标签后面添加了一个新的标签，但是结构里面不可见，虚拟，更好

```css
/* 声明清除浮动的样式 */
.clearfix:after {
  content: "";
  display: block;
  height: 0;
  visibility: hidden;
  clear: both;
}
/* 防止低版本浏览器不支持after */
/* ie6、7清除浮动的样式 */
.clearfix {
  *zoom: 1;
}

/* 然后给需要的标签添加一个类名：clearfix */
```

##### ④ 使用双伪元素清除浮动

代码更加简洁

```css
.clearfix:before,
.clearfix:after {
  content: "";
  display: table;
}
.clearfix:after {
  clear: both;
}
.clearfix {
  *zoom: 1;
}
```

#### 4. 清除浮动总结

当
* 父级没高度
* 子盒子浮动
* 影响下面的布局
就需要清除浮动，四种方法清除浮动

#### 5. PS切片

**PS切片常用切片工具**

大致步骤：切片后然后，导出-->存储为web常用-->然后用切片保存选中的切片
切片方法：
1. 切片工具直接切片
2. 图层-->新建基于图层的切片
3. 利用辅助线`ctrl+ R`调出辅助线

清除切片：视图-->清除切片

或者使用ps切片的插件（免费但是需要注册自己的帐号）
Cutterman切图神器

---

# ✳快捷键操作（常用）

**html编辑的快捷方法**

![快捷键操作](/img/hcj/kjj.png)

* `w200` 生成 `width: 200px;`
* `h200` 生成 `height: 200px;`

我的HB不行hhh草
* `bd+` 生成 `border: 1px solid #000;`
* `bd-` 生成 `border: none;`

---

# 3. js 的基础
