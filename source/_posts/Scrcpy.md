---
title: Scrcpy手机投屏到电脑
img: /img/pic/6.jpg
top: false
cover: false
date: 2020-03-02 19:07:08
categories: 技术力
tags:  
    - Source
    - Windows
summary: Scrcpy的使用教程
---

[Scrcpy](https://github.com/Genymobile/scrcpy)是一款可以将安卓手机投屏到电脑上的开源软件，在电脑上控制手机，无需root手机

**用前提示：**
安卓系统版本要求 5.0 以上

几个缺陷：（建议忽略）*版本 v1.12.1*

* 不能直接用电脑键盘输入中文，而且中文模式下，数字和符号无法输入
* 不能很好地与电脑触摸板习惯相联系（如双指放大缩小操作），但问题不大
* 手机内容无法复制到电脑，但电脑内容可以复制到手机

*也许以后会作者大佬修复*

**使用方法：**
### 1. 有线投屏
* 用usb数据线将手机和电脑相连接
* 打开手机地usb调试功能（开发者选项里）
* 如果提示是否允许usb调试，点击确定
* PC端，windows根据系统位数直接[下载压缩包](https://github.com/Genymobile/scrcpy/releases)
* 将解压后的安装包里面有一个**scrcpy.exe**文件，使用cmd运行
然后就好了

>更加详细的教程，参考[这篇文章](https://www.iplaysoft.com/scrcpy.html)


快捷键的使用
![快捷键使用](/img/scrcpy.png)


### 2. 无线投屏

注意要在同一局域网下

* 查询设备当前的 IP 地址 (设置 →关于手机→状态)
* 启用 adb TCP/IP 连接，执行命令：adb tcpip 5555，其中 5555 为端口号
* 拔掉你的数据线
* 通过 WiFi 进行连接，执行命令：adb connect 设备IP地址:5555
* 重新启动 scrcpy 即可
* 如果 WiFi 较慢，可以调整码率：scrcpy -b 3M -m 800，意思是限制 3 Mbps，画面分辨率限制 800，数值可以随意调整。
* 如需切换回 USB 模式，执行：adb usb