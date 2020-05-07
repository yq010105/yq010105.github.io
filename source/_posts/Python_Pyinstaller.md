---
title: Python中Pyinstaller库的学习
date: 2020-02-13 17:36:51
categories: 学习力
toc: true
summary: Pyinstaller 可以将 python 文件打包成 exe 可执行文件
tags:
  - Python
---

<!--more-->

**安装**
**`pip3 install pyinstaller`**

<!--more-->

# 1. Pyinstaller 的使用

## 1.1 打开 PowerShell 窗口

- 在你的 Python 程序文件夹上（不点进去）按住 shift 并且右键，在弹出的选项中点击"在此处打开命令行窗口"
- 或者先进入命令行窗口，然后使用 cd 指令进入程序文件夹，示例：
  `cd G:\工程储存\Python工程\love`

## 1.2 输入以下指令，开始打包

`pyinstaller -F -w (-i icofile) filename`

- filename 表示你的 Python 程序文件名
- -w 表示隐藏程序运行时的命令行窗口(不加-w 会有黑色窗口)
- 括号内的为可选参数，-i icofile 表示给程序加上图标，图标必须为.ico 格式
  _icofile 表示图标的位置，建议直接放在程序文件夹里面，这样子打包的时候直接写文件名就好_
- 输入示例：
  `pyinstaller -F -w -i favicon love.py`
- 然后我们进入到程序目录里面会再看到一个名称为 dist 目录，打包好的 exe 程序就在里面

## 1.3 pyinstaller 相关参数

- -F, –onefile 打包一个单个文件，如果你的代码都写在一个.py 文件的话，可以用这个，如果是多个.py 文件就别用
- -D, –onedir 打包多个文件，在 dist 中生成很多依赖文件，适合以框架形式编写工具代码，我个人比较推荐这样，代码易于维护
- -K, –tk 在部署时包含 TCL/TK
- -a, –ascii 不包含编码.在支持 Unicode 的 python 版本上默认包含所有的编码.
- -d, –debug 产生 debug 版本的可执行文件
- -w,–windowed,–noconsole 使用 Windows 子系统执行.当程序启动的时候不会打开命令行(只对 Windows 有效)
- -c,–nowindowed,–console 使用控制台子系统执行(默认)(只对 Windows 有效)
- -s,–strip 可执行文件和共享库将 run through strip.注意 Cygwin 的 strip 往往使普通的 win32 Dll 无法使用.
- -X, –upx 如果有 UPX 安装(执行 Configure.py 时检测),会压缩执行文件(Windows 系统中的 DLL 也会)(参见 note)
- -o DIR, –out=DIR 指定 spec 文件的生成目录,如果没有指定,而且当前目录是 PyInstaller 的根目录,会自动创建一个用于输出(spec 和生成的可执行文件)的目录.如果没有指定,而当前目录不是 PyInstaller 的根目录,则会输出到当前的目录下.
- -p DIR, –path=DIR 设置导入路径(和使用 PYTHONPATH 效果相似).可以用路径分割符(Windows 使用分号,Linux 使用冒号)分割,指定多个目录.也可以使用多个-p 参数来设置多个导入路径，让 pyinstaller 自己去找程序需要的资源
- –icon=<FILE.ICO>  
  将 file.ico 添加为可执行文件的资源(只对 Windows 系统有效)，改变程序的图标 pyinstaller -i ico 路径 xxxxx.py

- –icon=<FILE.EXE,N> 将 file.exe 的第 n 个图标添加为可执行文件的资源(只对 Windows 系统有效)
- -v FILE, –version=FILE 将 verfile 作为可执行文件的版本资源(只对 Windows 系统有效)
- -n NAME, –name=NAME 可选的项目(产生的 spec 的)名字.如果省略,第一个脚本的主文件名将作为 spec 的名字

> [参考 CSDN](https://blog.csdn.net/qq_33462307/article/details/90479045)

# 2. Pyinstaller 的问题

## 2.1 Fail to execute scrip XXX

**使用了`pyinstaller -F -w code.py`打包以后，发现打不开**

_解决不了啊啊啊啊_
