---
title: WindowsTerminal
top: false
cover: false
date: 2020-03-18 22:48:23
categories: 资源力
tags:
	- Windows
summary: 一款美观的可以代替power shell的软件——WindowsTerminal
password:
---



# 发现

偶然间看到了[这篇文章](https://sspai.com/post/59380)，然后发现Windows terminal(wt)真的香，以下内容都是这篇文章的具体概况（自己的垃圾理解，太过于概括，建议看原文）

# 介绍

想要自定义一个美观的Windows terminal窗口，只需要打开Windows terminal的配置文件，即settings中设置`profiles.json`文件就可以配置了。

# 配置介绍

配置文件`profiles.json`中分为几个部分

* **全局属性**：位于 JSON 最外侧，包含有设置亮暗主题、默认 Profile 等项目的配置
* **环境入口 `profiles`**：一个列表，其中包含有 Windows Terminal 下拉菜单中唤起的各种环境（比如打开 PowerShell 环境、WSL 环境或 SSH 至远程服务器的环境……）与各种环境里 Windows Terminal 的显示方案（比如字体、背景、色彩方案等）
* **配色主题 `schemes`**：一个配色方案列表，其中包含有 Windows Terminal 在上一项「环境入口」中可以调用的「色彩主题」
* **快捷键绑定 `keybindings`**：自定义快捷键

![profiles.json的文件格式](https://cdn.sspai.com/editor/u_spencerwoo/15836861908691.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

## 全局属性

* `"defaultProfile"`即打开wt默认打开的环境,相对应得就是底下得`"guid"`后面的唯一标识码

- Terminal 亮暗主题设置 `"requestedTheme"`：可以为 `"system"`（跟随系统）、`"light"` 或 `"dark"`

- Terminal 初始大小：`"initialCols"` 和 `"initialRows"`

## profiles

可以看到刚下载下来的已经配置好的窗口有三个：PowerShell、cmd以及Azure Cloud Shell

在每一个窗口的配置中有着几个属性：

* `"guid"`唯一标识码 、`"name"`窗口名称、`"commandline"`打开的命令行
* 接下来就是自定义的属性（基础）
  * `"background"`背景颜色：`"#000000"`
  * `"acrylicOpacity"`亚克力效果透明度：`0.6`
  * `"useAcrylic"`亚克力效果：`true`
  * `"colorScheme"`底下的schemes中配置的颜色名字：`"name"`
  * `"backgroundImage"`背景图片，放在`C:\Users\{用户名}\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe`目录的`RoamingState`文件夹中假如命名为`back.png`,然后配置：`"ms-appdata:///roaming/back.png"`
  * `"backgroundImageStretchMode"`*按比例放大*:`"uniformToFill"`
  * `"backgroundImageOpacity"`图片的透明度:`0.6`
  * `"foreground"`字体颜色 : `"#e03c8a"`，`fontFace` 字体样式:`Consolas`, `fontSize` 字体大小:`16`
  * `"icon"` 添加小图标: `"ms-appdata:///roaming/sshicon.ico"`也是放在`RoamingState`中
  * 进一步的美化
    * `"cursorColor" `光标颜色: `"#7EA2B4"`
    * `"cursorShape" `光标形状: `"bar"`
    * 更进一步具体配置看[百度上的大佬](https://www.baidu.com/)_,或者参考[schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)中的配置可以在[官网](https://iterm2colorschemes.com/)预览

**详情可以参考我的配置文件**

```json
{
    "$schema": "https://aka.ms/terminal-profiles-schema",

    "defaultProfile": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",

    "requestedTheme": "light",

    "profiles":
    {
    
        "defaults":
        {
            // Put settings here that you want to apply to all profiles
        },
        "list":
        [
            {
                // Make changes here to the powershell.exe profile
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "name": "PowerShell",
                "commandline": "powershell.exe",
                "hidden": false,
            // "profiles": [ ... ] 项目中 PowerShell 环境的配置
            
                // "background": "#013456",
                // "acrylicOpacity": 0.8,  // 亚克力效果透明度
                // "useAcrylic": true  // 亚克力效果
                // "colorScheme": "name",//schemes中配置的主题颜色
                "backgroundImage": "ms-appdata:///roaming/back.png",
                "backgroundImageStretchMode": "uniformToFill", // 按比例放大
                "backgroundImageOpacity": 0.6 //图片透明的
            },
            {
                // Make changes here to the cmd.exe profile
                "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
                "name": "cmd",
                "commandline": "cmd.exe",
                "hidden": false,
                "backgroundImage": "ms-appdata:///roaming/cmd.jpg",
                "backgroundImageStretchMode": "uniformToFill",
                "backgroundImageOpacity": 0.6
            },
            {
                "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
                "hidden": false,
                "name": "Azure Cloud Shell",
                "source": "Windows.Terminal.Azure",
                "backgroundImage": "ms-appdata:///roaming/azu.jpg",
                "backgroundImageStretchMode": "uniformToFill",
                "backgroundImageOpacity": 0.6,
                "foreground": "#e03c8a"  //字体颜色 fontFace 字体样式, fontSize 字体大小
            },
            {
                "guid": "{a060905f-d089-43d9-9422-cd748e7f0230}",
                "name": "SSH-aliyun",
                "commandline": "powershell.exe ssh yq@123.56.22.122",
                "icon": "ms-appdata:///roaming/sshicon.ico",  // 添加小图标
                "backgroundImage": "ms-appdata:///roaming/ssh.jpg",
                "backgroundImageStretchMode": "uniformToFill",
                "backgroundImageOpacity": 0.6
            },
            {
                "acrylicOpacity" : 0.75,               //毛玻璃透明效果透明度
                "closeOnExit" : true,
                "commandline" : "bash.exe",
                "cursorColor" : "#7EA2B4",           //光标颜色
                "cursorShape" : "bar",               //光标形状
                "fontFace" : "Consolas",
                "fontSize" : 16,                      //字体大小
                "guid" : "{019f913c-595c-4498-a934-e01e71cd4cbf}",
                "historySize" : 9001,
                "icon" : "ms-appdata:///roaming/bashicon.ico", //图标地址
                "name" : "Git-bash",
                "padding" : "0, 0, 0, 0",
                "snapOnInput" : true,
                "startingDirectory" : "%USERPROFILE%",
                "useAcrylic" : true,
                "backgroundImage": "ms-appdata:///roaming/bash.jpg",
                "backgroundImageStretchMode": "uniformToFill",
                "backgroundImageOpacity": 0.6
            }
        ]
    },

    // Add custom color schemes to this array
    "schemes": [],

    // Add any keybinding overrides to this array.
    // To unbind a default keybinding, set the command to "unbound"
    "keybindings": [
        { "command": "closePane", "keys": ["ctrl+w"] },
        { "command": "closeWindow", "keys": ["alt+f4"] },
        { "command": "copy", "keys": ["ctrl+c"] },
        { "command": "paste", "keys": ["ctrl+v"] },
        { "command": "newTab", "keys": ["ctrl+t"] }
    ]
}

```

## schemes

[scheme官网](https://iterm2colorschemes.com/)有着最丰富的颜色配置

参照着schemes的配置学习如何自定义配置

也可以[参考大佬学习](https://www.cnblogs.com/KiraYoshikage/p/11443741.html)

## `keybindings`快捷键

![快捷键配置](/img/sys/key.png)

> 参考文档：[少数派](https://sspai.com/post/59380)