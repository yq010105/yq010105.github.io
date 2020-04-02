---
title: 服务器学习
img:
top: false
cover: false
date: 2020-03-11 17:31:06
categories: 学习力
tags:
  - 服务器
summary: 从零开始的服务器学习(白嫖到阿里云服务器后开始了解一些服务器的基本知识)
password:
---

<!--more-->

# 1. 入门概述

一台云服务器（以下简称 ECS 实例）由实例规格、镜像、块存储、快照、安全组、弹性网卡等基础计算组件组成并协同提供服务。一般来说，阿里云服务器、云服务器、云服务器 ECS、ECS 实例等均指代云服务器 ECS。其中：

- 实例规格：定义了 ECS 实例的 vCPU 和内存的配置，是计算能力的体现。
- 镜像：提供启动 ECS 实例所需的所有信息，包括操作系统和预装软件。
- 块存储：提供存储能力，包括系统盘和数据盘。存储类型包括云盘和本地盘等多种不同类型的磁盘。就像硬盘一样，您可以对挂载到 ECS 实例上的云盘做分区、格式化、创建文件系统等操作，并对数据进行持久化存储。
- 网络：使用专有网络（简称 VPC），相当于您自己构建了一个数据中心网络，有自己的路由、交换机和访问策略。
- 安全组：用来允许或拒绝公网请求和内网请求，为实例提供防护能力。绝大多数情况下，当实例加入一个新创建的安全组时，在提供业务访问前您都必须添加必要的安全组规则。一般来说，安全组等同于服务器防火
  墙。

# 2. 操作

> [参考博客](https://www.cnblogs.com/minhren/p/12337260.html)

## 2.1 登录

`ssh root@ip地址`

然后输入密码，可以到实例中重置密码

## 2.2 更新系统

`apt-get update`

## 2.3 升级软件

`apt-get install upgrade`
或者
`apt-get upgrade`

## 2.4 接着安装桌面系统

`apt-get install ubuntu-desktop`

## 2.5 打开

等到图形界面安装完成输入 reboot 指令进行重启.接着我们用控制台里的远程连接管理:要选 VNC,如图

![图片链接](https://img2018.cnblogs.com/i-beta/828103/202002/828103-20200220203209860-193153872.png)

然后输入远程连接密码

# 3. 连接服务器的方法

## 3.1 用 cmder 的 ssh

`ssh root@ip`
然后输入密码，即可连接

## 3.2 使用网页端的 VNC 连接

在阿里云服务器实例中的远程连接中有一个 VNC 连接，网页版的连接占用小但是太卡了

## 3.3 使用 Xshell 连接服务器

- Xshell:跟 cmder 差不多都是 ssh 连接然后命令行操作

* Xftp:可以在本地与服务器之间传输文件
* Xmanager:可以左到与 VNC 一样显示服务器的图形界面

# 服务器的一些用法（菜鸟）

## 1. 搭建网站

### 1.1 第一步学习

- 前端:html+css+js/vue 框架
- 后端:Django
- 数据库:Mysql
- Linux 知识

### 1.2 使用框架

word press + 主题

### 1.3 另一种方式

> 将本地的 hexo 博客内容部署到阿里云服务器：主要参考[大佬的教程](https://www.zhihu.com/question/60329559)

安装 nginx 和 git，我的是 Ubuntu，所以

```
apt-get update
apt-get install nginx
apt-get install git
```

新建 git 用户，并设置密码

```
adduser git
passwd
```

切换到 git 用户`su git`

在用户目录下新建.git 目录

```
cd ~  # cd到用户目录
mkdir .git
cd .git
```

将本地的密匙文件`id_rsa.pub`内容保存到`.git`目录下的`authorized_keys`

```
vim authorized_keys
```

使用vim将密匙粘贴在该文件中，然后保存退出就可以使用git用户ssh到服务器了

`ssh git@ip地址`

成功后，建立git库

```
mkdir hexo.git
cd hexo.git
git init --bare
```

然后设置显示成网页

```
cd hooks 
vim post-receive
```

将一下内容写入到`post-receive`中

```
#!/bin/bash

rm -rf /home/git/hexo
git clone /home/git/hexo.git /home/git/hexo

rm -rf /usr/share/nginx/hexo/*
mv /home/git/hexo/* /usr/share/nginx/hexo
```

修改执行权限

`chmod a+x post-receive`

配置nginx

`cd /usr/share/nginx`

切换root用户
```
su

创建hexo网页目录
mkdir hexo 

将文件夹所有者设置为git
chown git hexo 
chgrp git hexo 
```

到nginx中修改配置

```
cd /etc/nginx
vim nginx.conf

修改配置文件，修改location的目录,即加一行
root /usr/share/nginx/hexo;
```

然后将本地的hexo文件夹中的配置文件`_config.yml`修改`deploy`

`git@ip地址:hexo.git`

如我的
```
deploy:
  type: git
  repo: git@服务器ip地址:hexo.git
```

## 2. 内网穿透

## 3. 搭建一个文件系统

类似云盘

### 3.1 搭建网盘owncloud

>主要参考[这位大佬的教程](https://luomuxiaoxiao.com/?p=722)
>要先看[这篇](https://luomuxiaoxiao.com/?p=707)

只要跟着做一遍基本就能安装上，但是也有几个坑

几个坑：最后的登录时的用户名要在`/etc/mysql`下的`debian.cnf`中查看
直接输入：
`sudo vim/vi /etc/mysql/debian.cnf`
查看数据库的用户名密码，然后就可以了

可能我的服务器宽带不够hhh，搭建网盘还是没速度hhh，算了，等毕业以后在弄这些东西，主要是那个备案太烦了，太难了。所以现在光有域名没有备案，就不行，hhh只能通过ip地址访问hhh，太low了


## 4. 爬虫

初步实现的爬虫程序：

- 哔哩哔哩脚本

- 图片爬取
