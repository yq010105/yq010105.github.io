---
title: CSS学习中跟着老师做的几个项目
top: false
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
  1. logo盒子
  2. nav导航栏
  3. search搜索框和搜索按钮
  4. user用户头像和用户名
* 写banner部分