---
title: C#-Note
img:
top: false
cover: false
date: 2020-04-08 09:23:49
categories: 学习力
tags:
  - C#
  - Note
summary: 学习C#的笔记
password:
---

<!--more-->

> 参考[b 站的视频学习](https://www.bilibili.com/video/BV1wx411K7rb)

![编程](/img/cs/program.png)

# 0. C#学习前的 bb

C# 窗体应用，我的初步感受就是 VB+Java（狗头）
VB 现在正在学，但是 Java 是没学过 hhh

C# 是面向对象的语言，然而 C# 进一步提供了对面向组件 (component-oriented) 编程的支持。现代软件设计日益依赖于自包含和自描述功能包形式的软件组件。这种组件的关键在于，它们通过属性、方法和事件来提供编程模型；它们具有提供了关于组件的声明性信息的特性；同时，它们还编入了自己的文档。C# 提供的语言构造直接支持这些概念，这使得 C# 语言自然而然成为创建和使用软件组件之选。（copy from _csharp language specification 5.0 中文_）

# 1. 语言标准的——hello world!!!

## 1.1 Console

控制台.NET Framework

`Console.WriteLine("Hello World!!!");`

## 1.2 WPF

新的 windows forms（大概）,感觉就是更高级的 VB，更自由更美观的界面开发
跟 windows forms 一样

`textBoxShowHello.Text = "Hello World!";`

## 1.3 Windows Forms App(old)

窗体程序，学过一点 VB，无所畏惧

button
`textBoxShowHello.Text = "Hello World!";`

## 1.4 ASP.NET Web Forms(old)

网络应用程序，网页
Controller 中
`<h1>Hello World!<h1>`

## 1.5 ASP.NET MVC

程序开发架构，可以将不同语言的代码放在不同的目录中
Controller 中
`<h1>Hello World!<h1>`

## 1.6 WCF

纯网络服务，读取数据库、向数据库输入数据

```csharp
public string SayHello()
{
  return "hello world!!!";
}
```

## 1.7 Windows Store Application

平板电脑,也是窗体设计
`textBoxShowHello.Text = "Hello World!!!";`

## 1.8 Windows Phone Application(已经凉透了？？？)

`textBoxShowHello.Text = "Hello World!!!";`

## 1.9 Cloud

云计算 Azure
`<h1>Hello World!<h1>`

## 1.10 WF

窗体设计
直接在 writeline 控件里写
`"hello world!!!"`

# 2. 类与名称空间

**class & namespace**

## 2.1 剖析 Hello World 程序

- 类是构成程序的主体
- 名称空间是以树型结构组织类（和其他类型），如 Button 类和 Path 类

Console App : `Console.WriteLine("Hello World~");`

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApphello
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World");
        }
    }
}
```

类 class `Program`(自己写的)和`Console`(调用 C#的类)
`WriteLine`方法

名称空间 namespace `HelloWorld`，默认跟创建 project 时名称一样

**核心理解：**

**又如`System`名称空间中的`Console`类，类中的`WriteLine`方法**

**`using System`** 跟 python 中的`import`差不多

就是：
有`using System;` 直接用`Console.WriteLine`
没有`using System;`则必须用`System.Console.WriteLine`