---
title: Python_pip
top: false
cover: false
date: 2020-02-27 15:10:05
categories: 学习力
tags:
  - Python
summary: pip 的使用方法
---

> [参考博客](https://blog.csdn.net/qq_15260769/article/details/80731407)

# 1. pip 自身的安装，更新，卸载

## 1.1 pip 安装

[官网下载 pip](https://pypi.python.org/pypi/pip),下载 .tar.gz 压缩包

- 解压后再文件目录中有一个`setup.py`文件
- 使用`python setup.py install`安装 pip
- 环境变量设置，找一下 pip.exe 所在位置，将其添加到系统的环境变量 path 中

# 1.2 pip 更新

`python -m pip install --upgrade pip`

# 1.3 pip 卸载

`python -m pip uninstall pip`

# 2. pip 对 python 包的操作

## 2.1 pip 安装包

`pip install 包名`

## 2.2 pip 更新包

`pip install --upgrade 包名`

## 2.3 pip 卸载包

`pip uninstall 包名`

## 2.4 其他细节操作

### 2.4.1 查看安装的包

`pip list`

### 2.4.2 查看具体包的信息

`pip show 包名`

### 2.4.3 查看需要升级的包

`pip list --outdated`
