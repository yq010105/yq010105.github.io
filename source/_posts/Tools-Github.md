---
title: Github的一些基本知识
date: 2020-02-09 11:15:23
toc: true
categories: 学习力
summary: Github的优雅操作/Git的基础操作，记录学习使用github这座宝库中的一些基础知识
tags:
  - Github
---

<!--more-->

## 1. Github

### 1.1 搜索技巧

#### ① in:name spring boot

名字里带 spring boot，在 name 中搜

#### ② in:readme spring boot

readme 中带 spring boot，在 readme 中搜

#### ③ in:description

在描述中搜

#### ④ stars:>3000

stars 多于 3000 的数据库

#### ⑤ forks:>3000

forks 多于 3000 的数据库

#### ⑥ language:java

java 语言的数据库

#### ⑦ push:>2019-02-01

在 2019.02.01 以后有过更新的数据库

> 在[大佬 b 站视频](https://www.bilibili.com/video/av75587104)中学习

## 2. Git

### 2.1 git 使用

>[大佬的b站帐号](https://space.bilibili.com/503792864)
>[大佬的视频](https://www.bilibili.com/video/av540325349)

![大佬做的图](https://raw.githubusercontent.com/yq010105/Blog_images/master/img/git.png)

基本操作：
- `git init 项目名` 创建一个新的本地代码库
- `git config --global user.name "your name"` 设置你的名字，将会被加到commit和tags中
- `git config --global user.email "youremail"` 设置邮箱地址，将会被加到commit和tags中

#### 2.1.1 本地操作

- `git add . `放到暂存区
- `git commit -m 'title'` 提交代码到本地仓库
- `git status` 查看当前状态，列出所有新修改、暂存区文件的修改情况
- `git log --n` 显示最近n次commit记录
- `git reset  --hard commit_id` 回滚版本 *commit_id: 就是用git reflog可以查看到的一串东西*
- `git diff [file]` 查看工作区和暂存区的区别 ：`git diff` `git diff --cached`
- `git rm [file]` 删除工作区和暂存区的文件
- `git reflog` 记录所有的操作记录
- `git checkout -- [file]` 把工作区修改撤销掉
- `git reset HEAD [file]` 把暂存区的修改撤销掉
- `git stash` 把工作区修改内容保存到贮藏区
- `git stash pop` 将贮藏区的内容恢复到工作区
- `git tag` 列出代码库中所有的tag
- `git tag -a<版本号>-m message` 新增一个版本号 

#### 2.1.2 分支操作

- `git branch -a` 列出当地所有分支
- `git switch -c [name]` 创建一个新的分支
- `git switch [name]` 切换分支
- `git merge [from name]` 将name分支与当前分支合并
- `git branch -d [name]` 删除name分支

#### 2.1.3 远程操作

- `git clone url` 从远程代码库下载整个代码库和历史记录
- `git remote add <remote name> <url>` 链接一个远程库
- `git fetch` 从远程代码库下载所有变动
- `git push` 将当前本地的代码库推送到远程remote库的branch分支
- `git pull` 从远程库拉去代码并将当前分支和他的`upstream merge`

### 2.2 .gitignore 文件

|     例子      |            解释            |
| :-----------: | :------------------------: |
|     /mtk      |       过滤整个文件夹       |
|    \*.zip     |     过滤所有.zip 文件      |
|   /mtk/do.c   |      过滤某个具体文件      |
| !/mtk/one.txt | 追踪（不过滤）某个具体文件 |

```
配置语法
以斜杠“/”开头表示目录；
以星号“*”通配多个字符；
以问号“?”通配单个字符
以方括号“[]”包含单个字符的匹配列表；
以叹号“!”表示不忽略(跟踪)匹配到的文件或目录。
注意： git 对于 .gitignore配置文件是按行从上到下进行规则匹配的
```

- _如果你创建.gitignore 文件之前就 push 了某一文件，那么即使你在.gitignore 文件中写入过滤该文件的规则，该规则也不会起作用，git 仍然会对该文件进行版本管理_
- **.gitignore 规则不生效**
  _.gitignore 只能忽略那些原来没有被 track 的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore 是无效的_
- **解决方法**
  **解决方法就是先把本地缓存删除（改变成未 track 状态），然后再提交**

```
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
```

- **Git 忽略文件提交的三种方法**
- **1、在 Git 项目中定义 .gitignore 文件**
  这种方式通过在项目的某个文件夹下定义 .gitignore 文件，在该文件中定义相应的忽略规则，来管理当前文件夹下的文件的 Git 提交行为
  在 .gitingore 文件中，遵循相应的语法，在每一行指定一个忽略规则
- **2、在 Git 项目的设置中指定排除文件**
  这种方式只是临时指定该项目的行为，需要编辑当前项目下的 .git/info/exclude 文件，然后将需要忽略提交的文件写入其中
  _这种方式指定的忽略文件的根目录是项目根目录_
- **3、定义 Git 全局的 .gitignore 文件**
  除了可以在项目中定义 .gitignore 文件外，还可以设置全局的 git .gitignore 文件来管理所有 Git 项目的行为。这种方式在不同的项目开发者之间是不共享的，是属于项目之上 Git 应用级别的行为

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

> 作者：王伟 desire
>链接：https://www.jianshu.com/p/74bd0ceb6182
>来源：简书
>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

### 2.3 cmder 命令操作文件和文件夹

常用命令

- 切换目录 cd：change directory 的简写，如：cd d:aa/nn 意思就是切换到 d 盘下的 aa 文件夹下的 nn 文件夹
- 回到上一目录 cd .. 这个结合我们写 js 或者 css 时，引用文件时写为../lib/aa.js 所以这个很好理解 需要注意的是在 cd 和..之间有个空格
- 创建文件 touch 如：touch aa.te 意思就是在当前目录下创建一个名为 aa.te 的文件
- 删除文件 rm 是 remove 的简写 如：rm aa.te 意思就为删除当前目录下的 aa.te 文件
- 创建文件夹 mkdir 为 make directory 的简写，如 mkdir aa 即为在当前目录下创建一个 aa 文件夹
- 删除文件夹 rm -r 其中的 r 表示递归（recusive）的意思，意思就是先删除文件夹里的文件在删除文件夹，如：rm -r aa 意思为删除 aa 文件夹下的文件和 aa 文件夹自己
- 打印当前目录路劲 pwd 为 print working directory 的简写，
- 显示当前目录下的所有文件列表 ls 为 list 的简写，当然也可以用 ll 命令，它比 ls 显示的内容更加详细，但是 ll 在 cmder 中不可用
- 清屏 cmder 中为 cls 和 clear 均可，reset 无效， 而在 bash 中 clear 和 reset 均可，cls 无效；

![cmder](https://raw.githubusercontent.com/yq010105/Blog_images/master/img/cmder.png)

> 版权声明：本文为 CSDN 博主「LeonWuV」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
> [原文链接](https://blog.csdn.net/wxl1555/article/details/79887591)

### 2.4 更加基础的 cmd 命令

- mkdir `mkdir 文件夹名` 新建文件夹
- touch `touch 文件名`新建文件
  - 另一种方法：`cd .>user.js` // 在当前目录下新建 user.js 文件
- rm/del `rm 文件名` `del 文件名`删除文件
- rmdir `rmdir 空文件夹名`删除空文件夹
  - `rmdir /s/q 文件夹名`删除文件夹及内的全部文件 /s -删除全部子目录及内容，/q - 不显示 Y/N 询问
  - `rmdir /s/q d:\multify\my-multify` 删除 D 盘 multify 文件夹下的 my-multify 文件夹以及子内容，并且不提示
- rename`rename 1.txt 1.bat` 文件重命名
- `echo 111>>1.txt` 将 111 写进 1.txt 中，cmd 文本编辑
  - `echo .>>1.txt` 换行写
  - `for /f %i in ('type 1.txt') do md %i`以一个 txt 文件中的内容为名称创建文件(夹)
  - `copy con 1.txt` 然后将内容写入 1.txt 文件中(好像只能覆盖)
- `type 文件名` 查看文本文件内容
- `move 路径/文件名 路径` 移动文件
  - `move 路径\*.* 路径\` 移动所有文件
