---
title: Markdown
date: 2020-02-08 12:00:45
tags:
---

# 1、空格
`ok&nbsp;ok`&nbsp;它是按下space键产生的空格,叫不换行空格，全称是 No-Break Space
ok&nbsp;ok<hr/>
`ok&ensp;ok`&ensp;等同于字体度的一半,叫“半角空格”，全称是 En Space
ok&ensp;ok<hr/>
`ok&emsp;ok`&emsp;1 em在16px的字体中就是16px,它叫“全角空格”，全称是 Em Space
ok&emsp;ok<hr/>
`ok&thinsp;ok`&thinsp;“窄空格”，全称是 Thin Space。占据的宽度比较小。它是em之六分之一宽。
ok&thinsp;ok<hr/>
`ok&zwj;ok`&zwj;它叫零宽连字，全称是 Zero Width Joiner，简称“ZWJ”，是一个不打印字符
ok&zwj;ok
>参考[网站](https://www.jianshu.com/p/31eade263e7a "简书")
<!-- more -->
# 2、链接
### 行内式(方便简洁)
`[链接文字](链接网址 "标题")`
`This is an [example link](https://www.jianshu.com/p/31eade263e7a)`
会显示为:&nbsp;This is an [example link](https://www.jianshu.com/p/31eade263e7a)