---
title: Markdown
date: 2020-02-08 12:00:45
tags:
  - Markdown
---

**关于我初次使用 Markdown 以来遇到的问题**
_Markdown 笔记本_

<!-- more -->

# 1. 空格

|          语法          |   example    |                                解释                                 |
| :--------------------: | :----------: | :-----------------------------------------------------------------: |
|   `ok&nbsp;ok`&nbsp;   |  ok&nbsp;ok  |   它是按下 space 键产生的空格,叫不换行空格，全称是 No-Break Space   |
|   `ok&ensp;ok`&ensp;   |  ok&ensp;ok  |          等同于字体度的一半,叫“半角空格”，全称是 En Space           |
|   `ok&emsp;ok`&emsp;   |  ok&emsp;ok  |   1 em 在 16px 的字体中就是 16px,它叫“全角空格”，全称是 Em Space    |
| `ok&thinsp;ok`&thinsp; | ok&thinsp;ok | “窄空格”，全称是 Thin Space。占据的宽度比较小。它是 em 之六分之一宽 |
|    `ok&zwj;ok`&zwj;    |  ok&zwj;ok   | 它叫零宽连字，全称是 Zero Width Joiner，简称“ZWJ”，是一个不打印字符 |

> 参考[网站](https://www.jianshu.com/p/31eade263e7a "简书")

# 2. 链接

## 2.1 行内式(方便简洁)

`[链接文字](链接网址 "标题")`
`This is an [example link](https://www.jianshu.com/p/31eade263e7a)`
会显示为:&nbsp;This is an [example link](https://www.jianshu.com/p/31eade263e7a)

## 2.2 锚点

- 第一种

```
- [测试](#测试)
### <a id="测试">测试</a>
```

- [测试](#测试)

* 第二种

```
### <a href="#测试2">测试2</a>
h
t
m
l
<a id="测试2">测试2</a>
```

- <a href="#测试2">测试 2</a>

> 参考[link](https://blog.csdn.net/wangzhibo666/article/details/88731227 "CSDN")

# 3. 图片

## 3.1 网络图片的添加

```
![alt 属性文本](图片地址)

![alt 属性文本](图片地址 "可选标题")
```

```
![四月是你的谎言](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=905665511,4125694826&fm=26&gp=0.jpg "四谎")
```

![四月是你的谎言](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=905665511,4125694826&fm=26&gp=0.jpg "四谎")

## 3.2 本地图片的添加

```
![avatar](/img/picture_exam.jpeg "example")
--or--
<img src="/img/picture_exam.jpeg " width = 10% height = 10% div align=right />
# 或者是
#<img src="url" width = "100" height = "100" div align=left />
```

![avatar](/img/picture_exam.jpeg "example")
<img src="/img/picture_exam.jpeg " width = 10% height = 10% div align=right />

# 4. 表格

```
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
```

| 左对齐 | 右对齐 | 居中对齐 |
| :----- | -----: | :------: |
| 单元格 | 单元格 |  单元格  |
| 单元格 | 单元格 |  单元格  |

> 参考教程:[markdown](https://www.runoob.com/markdown/md-tutorial.html)

# 5. 设置字体大小颜色

```
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=7 face="黑体">color=#0099ff size=72 face="黑体"</font>
<font color=#00ffff size=72>color=#00ffff</font>
<font color=gray size=72>color=gray</font>
```

<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=7 face="黑体">color=#0099ff size=72 face="黑体"</font>
<font color=#00ffff size=72>color=#00ffff</font>
<font color=gray size=72>color=gray</font>

- <a id="测试">锚点测试</a>
- <a id="测试2">锚点测试 2</a>
  > 参考网站:[CSDN](https://blog.csdn.net/weixin_37998647/article/details/79428290 "CSDN")
