---
title: 前端开发的基础知识
top: false
cover: false
date: 2020-03-25 12:04:47
categories: 学习力
tags:
  - Vue
summary: 学习前端前的基础知识，对，没错，就是html、css和js
password:
---

<!--more-->

**参考资料**（大佬的笔记）

> HTML https://blog.csdn.net/wuyxinu/article/details/103515157
> CSS https://blog.csdn.net/wuyxinu/article/details/103583618
> JS https://blog.csdn.net/wuyxinu/article/details/103642800
> JS-下 https://blog.csdn.net/wuyxinu/article/details/103646041
> 还有 jQuery 的 https://blog.csdn.net/wuyxinu/article/details/103669718
> Node.js + Gulp 知识点汇总 https://blog.csdn.net/wuyxinu/article/details/103774211

**学习思路**
HTML 入门 →**CSS 入门** →HTML 进阶 →CSS 进阶 →JavaScript 入门
→jQuery 入门 →ASP.NET 入门（或 PHP 入门）→Ajax→ASP.NET 进阶（或 PHP 进阶）

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
    <link href="index.css" rel="stylesheet" type="text/css" />
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

### 2.1.3 内联样式表

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

## 2.3 css选择器

将想要的标签选中，然后再操作标签

选择器
```css
选择器{
    样式属性1:取值1;
    样式属性2:取值2;
    ……
}
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

#### 2.3.1.4 子元素选择器

```css
#father1 #p1 {color:red;}
#父元素选择 #子元素选择 {属性:属性值}

<div id="father1">
    <div id="p1">绿叶学习网</div>
    <div>绿叶学习网</div>
</div>
```

#### 2.3.1.5 相邻选择器

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

#### 2.3.1.6 群组选择器

```css
h3,div,p,span {color:red;}
```

## 2.4 文本样式

* font-family 字体名：微软雅黑等等
`font-family:微软雅黑;`
* font-size 字体大小: px/百分比/em
`font-size:15px;`
* 

# 3. js 的基础
