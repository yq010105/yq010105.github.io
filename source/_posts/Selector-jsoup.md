---
title: 厚墨书源制作所需技术
date: 2020-02-18 12:19:20
summary: 在学习制作厚墨书源过程中需要进一步学习的技术
categories: 学习力
tags:
  - Jsoup
---

**Jsoup 中 Selector 选择器用法**
暂时不学了先，事情太多了
<!--more-->

> [Jsoup Selector](https://blog.csdn.net/syt_boss/article/details/82863990)
> [官方文档](https://jsoup.org/apidocs/org/jsoup/select/Selector.html)

# 1. Selector 选择器概述

* tagname: 通过标签查找元素，比如：a
* ns|tag: 通过标签在命名空间查找元素，比如：可以用 fb|name 语法来查找 <fb:name> 元素
* #id: 通过 ID 查找元素，比如：#logo
* .class: 通过 class 名称查找元素，比如：.masthead
* [attribute]: 利用属性查找元素，比如：[href]
* [^attr]: 利用属性名前缀来查找元素，比如：可以用[^data-] 来查找带有 HTML5 Dataset 属性的元素
*  [attr=value]: 利用属性值来查找元素，比如：[width=500]
*  [attr^=value], [attr$=value], [attr*=value]: 利用匹配属性值开头、结尾或包含属性值来查找元素，比如：[href\*=/path/]
*  [attr\~=regex]: 利用属性值匹配正则表达式来查找元素，比如： img[src\~=(?i)\.(png|jpe?g)]
* \*: 这个符号将匹配所有元素

# 2. Selector选择器组合使用

* el#id: 元素+ID，比如： div#logo
* el.class: 元素+class，比如： div.masthead
* el[attr]: 元素+class，比如： a[href]
* 任意组合，比如：a[href].highlight
* ancestor child: 查找某个元素下子元素，比如：可以用.body p 查找在"body"元素下的所有 p元素
* parent > child: 查找某个父元素下的直接子元素，比如：可以用div.content > p 查找 p 元素，也可以用body > * 查找body标签下所有直接子元素
* siblingA + siblingB: 查找在A元素之前第一个同级元素B，比如：div.head + div
* siblingA ~ siblingX: 查找A元素之前的同级X元素，比如：h1 ~ p
* el, el, el:多个选择器组合，查找匹配任一选择器的唯一元素，例如：div.masthead, div.logo

# 3. 伪选择器selectors
* :lt(n): 查找哪些元素的同级索引值（它的位置在DOM树中是相对于它的父节点）小于n，比如：td:lt(3) 表示小于三列的元素
* :gt(n):查找哪些元素的同级索引值大于n，比如： div p:gt(2)表示哪些div中有包含2个以上的p元素
* :eq(n): 查找哪些元素的同级索引值与n相等，比如：form input:eq(1)表示包含一个input标签的Form元素
* :has(seletor): 查找匹配选择器包含元素的元素，比如：div:has(p)表示哪些div包含了p元素
* :not(selector): 查找与选择器不匹配的元素，比如： div:not(.logo) 表示不包含 class=logo 元素的所有 div 列表
* :contains(text): 查找包含给定文本的元素，搜索不区分大不写，比如： p:contains(jsoup)
* :containsOwn(text): 查找直接包含给定文本的元素
* :matches(regex): 查找哪些元素的文本匹配指定的正则表达式，比如：div:matches((?i)login)
* :matchesOwn(regex): 查找自身包含文本匹配指定正则表达式的元素
* 注意：上述伪选择器索引是从0开始的，也就是说第一个元素索引值为0，第二个元素index为1等

