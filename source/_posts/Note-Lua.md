---
title: Lua-Note
img: /img/pic/1.jpg
top: false
cover: false
date: 2020-03-04 20:09:03
categories: 学习力
tags:
  - Lua
  - Note
summary: 关于lua语言的学习，听说跟c差不多，Lua语言学习笔记本
password:
---

<!--more-->

# 1. 基础知识

## 1.1 注释

- 单行注释 `--单行注释`

- 多行注释

```lua
--[[
多行注释
下面两个--可有可无
--]]
```

### 1.2 标示符

变量，最好不要使用下划线夹大写字母的标示符
Lua 不允许使用特殊字符和@ \$ % 来定义标示符

### 1.3 关键字

不可以当作变量，function local nil repeat until 等等

### 1.4 全局变量

默认变量为全局变量
访问一个没有声明的全局变量返回 nil，无

```lua
print(aa)
-- nil
```

删除全局变量：`a = nil`

### 1.5 Lua 数据类型

lua 是动态类型语言，变量不需要类型定义，只需复制
lua 的数据基本类型：
**nil** , **boolean** , **number** , **string** , userdata(用户自定义) , **function(函数)** , thread(进程) ,**table(实现类与类的继承)**
nil：一个无效值（false）
boolean： true 、false/nil
number： 只有 double 双精度型
string：字符串，''/""都可以 `[[一串可换行字符串]]`
userdata：表示任意存储在变量中的 c 数据结构
thread：表示执行的独立线路，用于执行协同程序
table：lua 中的他变了是一个关联数组，数组的索引可以实数字、字符串或表类型，构造表达式：{}表示创建一个空表

#### 1.5.1 number & string

几个例子：

```lua
print(11+"11")
--22.0
print("11"+"11")
--22.0   自动将字符串转换为number

print("a" .. "b")
--ab
-- 用 .. 链接字符串，前后有空格
print(123 .. 456)
--123456

len = "123456"
print(#len)
-- 6
-- # 计算字符串长度
```

#### 1.5.2 table

table 表的操作

```lua
-- 创建空表
local tbl1 = {}

-- 键值对形式添加数据
tbl1 = {}
tbl1["red"] = 10
print(tbl1["red"])
--10
rrr = {red=10,blue=20,yellow=30}
print(rrr["red"])
--10

-- 列表中的yyy[1] 不是下标，而是key |123
yyy = {"red","blue","orange"}
print(yyy[1],yyy[2],yyy[3])
--red blue	orange
```

table 遍历

```lua
rrr = {red=10,blue=20,yellow=30}
for k,v in pairs(rrr) do
    print(k .. ":" .. v);
end
--[[好像是随机排的
red:10
blue:20
yellow:30
]]
```

#### 1.5.3 function

函数类型，定义函数

```lua
function kkk (v)
    print(v+v)
end
kkk(6)
-- 12

a = kkk
a(8)
--16
```

**难点:函数中函数**

```lua
function kkk(tab,func)
    for k,v in pairs(tab) do
        func(k,v)
    end
end

ttt = {red = 10 , blue = 20 }
kkk(ttt,function(k1,v1)
            print(k1 .. v1)
        end
)

-- blue20
-- red10
```

### 1.6 运算符

#### 1.6.1 算数运算符

+-\*/ 加减乘除
% 取余
^ 乘幂
\- 符号

#### 1.6.2 关系运算符

== / ~= / > / < / >= / <=

#### 1.6.3 逻辑运算符

and 与
or 或
not 非

#### 1.6.4 其他运算符

.. 连接两个字符串
\# 返回字符串长度或表的长度

#### 1.6.5 运算符优先级

从上到下，优先级减小 ^优先级最大
^
not - \* /
\+ -
..
\> < <= >= ~= ==
and
or

### 1.7 