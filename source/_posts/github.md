---
title: Github
date: 2020-02-09 11:15:23
categories: 学习力
summary: Github的优雅操作/Git的基础操作
tags:
    - Github
---

## 1. Github

### 1.1 搜索技巧
#### ① in:name spring boot
名字里带spring boot，在name中搜

#### ② in:readme spring boot
readme中带spring boot，在readme中搜
#### ③ in:description
在描述中搜
#### ④ stars:>3000
stars 多于3000的数据库
#### ⑤ forks:>3000
forks 多于3000的数据库
#### ⑥ language:java
java 语言的数据库
#### ⑦ push:>2019-02-01
在2019.02.01以后有过更新的数据库
>在[大佬b站视频](https://www.bilibili.com/video/av75587104)中学习

## 2. Git
### 2.1 git使用
* git add .
* git commit -m 'title'
* git push 
* git pull
* git clone https://........

### 2.2 .gitignore文件

|例子|解释|
|:----:|:----:|
|/mtk |过滤整个文件夹|
|*.zip| 过滤所有.zip文件|
|/mtk/do.c| 过滤某个具体文件|
|!/mtk/one.txt| 追踪（不过滤）某个具体文件|

```
配置语法
以斜杠“/”开头表示目录；
以星号“*”通配多个字符；
以问号“?”通配单个字符
以方括号“[]”包含单个字符的匹配列表；
以叹号“!”表示不忽略(跟踪)匹配到的文件或目录。
注意： git 对于 .gitignore配置文件是按行从上到下进行规则匹配的
```

* *如果你创建.gitignore文件之前就push了某一文件，那么即使你在.gitignore文件中写入过滤该文件的规则，该规则也不会起作用，git仍然会对该文件进行版本管理*
* **.gitignore规则不生效**
*.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的*
* **解决方法**
**解决方法就是先把本地缓存删除（改变成未track状态），然后再提交**
```
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```

* **Git 忽略文件提交的三种方法**
* **1、在Git项目中定义 .gitignore 文件**
这种方式通过在项目的某个文件夹下定义 .gitignore 文件，在该文件中定义相应的忽略规则，来管理当前文件夹下的文件的Git提交行为
在 .gitingore 文件中，遵循相应的语法，在每一行指定一个忽略规则
* **2、在Git项目的设置中指定排除文件**
这种方式只是临时指定该项目的行为，需要编辑当前项目下的 .git/info/exclude 文件，然后将需要忽略提交的文件写入其中
 *这种方式指定的忽略文件的根目录是项目根目录*
* **3、定义Git全局的 .gitignore 文件**
除了可以在项目中定义 .gitignore 文件外，还可以设置全局的 git .gitignore 文件来管理所有Git项目的行为。这种方式在不同的项目开发者之间是不共享的，是属于项目之上Git应用级别的行为

```
Git 忽略规则匹配语法
在 .gitignore 文件中，每一行的忽略规则的语法如下：

空格不匹配任意文件，可作为分隔符，可用反斜杠转义
# 开头的模式标识注释，可以使用反斜杠进行转义
! 开头的模式标识否定，该文件将会再次被包含，如果排除了该文件的父级目录，则使用 ! 也不会再次被包含。可以使用反斜杠进行转义
/ 结束的模式只匹配文件夹以及在该文件夹路径下的内容，但是不匹配该文件
/ 开始的模式匹配项目跟目录
如果一个模式不包含斜杠，则它匹配相对于当前 .gitignore 文件路径的内容，如果该模式不在 .gitignore 文件中，则相对于项目根目录
**匹配多级目录，可在开始，中间，结束
?通用匹配单个字符
[]通用匹配单个字符列表
```


>作者：王伟desire
    链接：https://www.jianshu.com/p/74bd0ceb6182
    来源：简书
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


### 2.3 cmder 命令操作文件和文件夹
常用命令
* 切换目录 cd：change directory的简写，如：cd d:aa/nn 意思就是切换到d盘下的aa文件夹下的nn文件夹
* 回到上一目录 cd .. 这个结合我们写js或者css时，引用文件时写为../lib/aa.js 所以这个很好理解 需要注意的是在 cd 和..之间有个空格
* 创建文件 touch 如：touch aa.te 意思就是在当前目录下创建一个名为aa.te的文件
* 删除文件 rm 是remove的简写 如：rm aa.te 意思就为删除当前目录下的aa.te文件
* 创建文件夹 mkdir 为make directory 的简写，如 mkdir aa 即为在当前目录下创建一个aa文件夹
* 删除文件夹 rm -r 其中的r表示递归（recusive）的意思，意思就是先删除文件夹里的文件在删除文件夹，如：rm -r aa 意思为删除aa文件夹下的文件和aa文件夹自己
* 打印当前目录路劲 pwd 为print working directory的简写，
* 显示当前目录下的所有文件列表 ls 为list的简写，当然也可以用ll命令，它比ls显示的内容更加详细，但是ll在cmder中不可用
* 清屏 cmder中为 cls和clear均可，reset无效， 而在bash中clear和reset均可，cls无效；

![cmder](/img/cmder.png)
>版权声明：本文为CSDN博主「LeonWuV」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
>[原文链接](https://blog.csdn.net/wxl1555/article/details/79887591)


### 2.4 更加基础的cmd命令
* mkdir `mkdir 文件夹名`  新建文件夹
* touch `touch 文件名`新建文件
  * 另一种方法：`cd .>user.js` // 在当前目录下新建user.js文件
* rm/del `rm 文件名`    `del 文件名`删除文件
* rmdir `rmdir 空文件夹名`删除空文件夹
  * `rmdir /s/q 文件夹名`删除文件夹及内的全部文件     /s -删除全部子目录及内容，/q - 不显示 Y/N询问
  * `rmdir /s/q d:\multify\my-multify`    删除D盘multify文件夹下的my-multify文件夹以及子内容，并且不提示
* rename`rename 1.txt 1.bat`   文件重命名
* `echo 111>>1.txt` 将111 写进1.txt中，cmd文本编辑
  * `echo .>>1.txt` 换行写
  * `for /f %i in ('type 1.txt') do md %i`以一个txt文件中的内容为名称创建文件(夹)
  * `copy con 1.txt` 然后将内容写入1.txt文件中(好像只能覆盖)
* `type 文件名` 查看文本文件内容
