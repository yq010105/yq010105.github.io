---
title: CSS学习中跟着老师做的几个项目
top: false
toc: true
cover: false
date: 2020-04-26 16:47:29
categories: 学习力
tags:
    - 前端
summary: CSS学习过程中做的几个项目，主要是笔记本中字数太多了，看的不舒服hhh
password:
---

<!--more-->

# 1. 学成在线网站

跟学老师：[pink老师](https://space.bilibili.com/415434293)的css课，[B站上的教程](https://www.bilibili.com/video/BV14J4114768?p=195)
时间线：跟学第七天，浮动切片学完后的案例，学成在线网页项目的制作

>[黑马pink老师的资源链接](https://gitee.com/xiaoqiang001/html_css_material.git)
**pink老师yyds**

**开始学习**

---

## 1.1 布局流程

为了提高网页制作的效率布局时通常有一下的流程
* 必须确定页面的版心（可视区），测量可得
* 分析页面中的行模块，以及每个行模块中的列模块，页面布局（一行行的罗列而成）
* 制作HTML的结构，**先结构，后样式**
* 运用盒子模型的原理，通过div+css布局来控制网页的各个模块

## 1.2 页面制作

### 1.2.0 样式初始化
```css
/* css初始化代码,css reset */
/* 清除元素默认的内外边距 */
* {
	padding: 0;
	margin: 0;
}
/* 清除列表样式 */
li {
	list-style: none;
}
/* 去掉button中默认自带的边框 */
button {
	border: none;
}
```

### 1.2.1 版心定义

```css
.w {
	width: 1200px;
	margin: auto;
}
```

定义好了以后，直接后面用多类名方式应用版心样式

### 1.2.2 头部制作

* 先写主要的大盒子
* 然后写大盒子内的**小盒子**

`class="headr"`中

1. `logo`盒子
2. `nav`导航栏
3. `search`搜索框和搜索按钮
4. `user`用户头像和用户名

### 1.2.3 Banner部分

`class="banner"`部分

1. 左侧的`subnav start`
2. 右侧的`course start`

### 1.2.3 精品推荐小模块goods

（banner下面一行）

1. `h3` 
2. `goods-item`几个推荐
3. `mod` 修改兴趣

### 1.2.4 精品推荐大模块box
1. `box-hd`写标题
2. `box-bd`写内容小盒子