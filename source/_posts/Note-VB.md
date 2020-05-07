---
title: VB-Note
date: 2020-02-16 13:32:49
top: true
toc: true
img: /img/cover/vb.jpg
summary: VB语言学习过程，这个学期开始学习VB，提前作预习，VB笔记本
categories: 学习力
tags:
  - VB
  - Note
---

# 5. **正式学习**

## 5.1 基础知识（零碎）

对象：数据和数据操作方式的综合体，如窗体、控件

对象三要素：属性、事件、方法

- 属性：
  `对象.属性= 属性值`

- 事件：

```vb
Private Sub 对象名_事件过程名[参数列表]
' click load ----
End Sub
```

- 方法：

```
对象.方法[参数名表]
Form1.Print "avb"
Text1.SetFocus
```

暂停程序 Stop
结束程序 End

命令按钮改变背景必须变两个属性-bg 和 style
其他的只需改变 bg 就行了

### If 判断结构

```vb
if 表达式 then
  语句1
else
  语句2
end if
```

**example：密码输入，限制输入 3 次**

```vb
Dim i As Integer ' 定义一个整型变量
Private Sub Command2_Click()
    If Text1 = "buct" Then
        Text2.Visible = True
        Label2.Visible = True
        Command1.Visible = True
        Text1.Visible = False
        Label1.Visible = False
        Command2.Visible = False
        Label3.Visible = False
        Text2.SetFocus
    Else
       ' Text1 = ""
       ' Label3.Visible = True
       ' Label3 = "密码错误，请重新输入"
       ' Text1.SetFocus
        i = i +1
        If i >= 3 Then End
        Text1 = ""
        Text1.SetFocus
        MsgBox "密码输入错误，请重新输入" ' 弹出一个框
    End If
End Sub

Private Sub Form_Load()
    Text2.Visible = False
    Label2.Visible = False
    Command1.Visible = False
    Label3.Visible = False
End Sub
```

## 5.2 VB 的语言成分

编码规则：

- 不区分字母大小写
- 语句书写自由:同一行可以写多条语句用`:`分开、一条语句多行写用`_`连接
- 代码注释： `'`或者`Rem`引导注释内容、快注释-视窗-工具栏-编辑-快注释
- VB 的命名约定：字母或汉字开头，长度不超过 255 个字符，控件不超过 40 个字符
  - 不用 VB 关键字:`if loop`
  - 不能包含空格，小数点，其他声明字符`$ % &`

### 5.2.1 基本数据类型

![VB数据类型](/img/VB/sjlx.png)

### 5.2.2 直接常量

![VB直接常量](/img/VB/zjcl.png)

### 5.2.3 变量

1. 变量隐式声明：使用的变量未作声明，所有变量均为 Variant 类型
2. 变量显式声明：

- 使用类型标示符直接声明变量 `MyName$ ="David"`--字符串型
- 使用 Dim 语句
  - 格式 1：Dim 变量名 As 数据类型[,变量名 As 数据类型，.....0]
  - 格式 2：Dim 变量名 + 类型标识符

```vb
Dim A As Integer, B As Double
Dim A%,B#
Dim MyName1 As String , Myname2 As String*5 '字符串只能是五个字符
Dim Vp1, Vp2 As Single
```

3. 变量的强制声明：在每个模块开始处自动加一条"Option Explicit"语句，所有变量需要指定数据类型

工具菜单- 选项命令 - 选中编辑器中的要求变量声明

### 5.2.4 模块

VB 代码存储在模块中
三种模块：窗体模块、标准模块、类模块
![VB模块](/img/VB/mk.png)

### 5.2.5 变量的作用域

- 全局变量：在窗体或标准模块中声明 Public
  - `Public 变量名 As 数据类型`
- 模块级变量：在模块的声明部分使用 Dim 或 Private 声明
  - `Dim 变量名 As 数据类型`
- 局部变量：在过程中由 Dim 或 Static 关键字声明
  - `Static 变量名 As 数据类型`

变量的作用域
![变量的作用域及使用规则](/img/VB/zyy.png)

- 内部常量：控件常量、语言常量、对象常量、用户界面常量
- 用户定义常量：用 Const 语句和赋值

```vb
Const PI As Double = 3.14159265...
Private Const Msg As String = "hello world"
Public Const Msg As String = "天安门"
```

- 静态变量：每次调用一个过程时保留上次的调用值

`Static 变量名 As 数据类型,变量名 As 数据类型....`

### 5.2.6 变量类型检查

![变量的类型检查](/img/VB/bllxjc.png)

![数据类型分类判断](/img/VB/sjlxflpd.png)

### 5.2.7 运算符

![运算符](/img/VB/ysf.png)

### 5.2.8 常用内部函数

![常用内部函数、数学函数](/img/VB/cyhs.png)
![常用转换函数](/img/VB/cyzhhs.png)
![字符串函数](/img/VB/zfchs.png)

![字符串函数例子](/img/VB/sszfclz.png)

### 5.2.9 日期函数

```vb
'Time Date Now DateDiff DateAdd
Private Sub Command1_Click()
    Dim d1 As Date, d2 As Date
    Print Now, Date, Time
    Print Time, Hour(Time), Minute(Time), Second(Time)
    Print Date, Year(Date), Month(Date), Day(Date)
    Print "=---------------------="
    Print DateDiff("d", Now, #10/1/2009#); #10/1/2009# - Date
    Print Date + Time; "***"; DateAdd("h", 5, Now); "***";
    Print DateAdd("s", 5, Time), vbCrLf
    d1 = "2004-07-16 05:00:00"
    d2 = "2004-08-20 23:00:00"
    Print #8/20/2004# - #7/16/2004#, d2 - d1, (d2 - d1) * 24
End Sub
```

![日期函数例子](/img/VB/rqlz.png)

**格式输出函数**
`Format$(表达式[,格式字符串])`

> 关于日期的格式详情，参考[Format 函数](https://blog.csdn.net/bigheadsheep/article/details/12013267)这篇文章

**Shell 函数**
![shell函数](/img/VB/shellhs.png)

### 5.2.10 基本语句

#### 5.2.10.1 赋值语句

```vb
Let 变量名 = 表达式  '普通变量
Set 变量名 = 表达式  ' 对象型变量

Let A = 5
Set Obj1 = Command1

Text1.text = "ok"
```

#### 5.2.10.2 快速输入输出函数

![InputBox函数](/img/VB/kssrschs.png)

![MsgBox函数](/img/VB/msgbox.png)

![MsgBox例子](/img/VB/msgboxlz.png)

## 5.3 控制结构与算法

### 5.3.1 顺序结构

语句 1→→→ 语句 2→→→ 语句 3

### 5.3.2 选择结构

#### 5.3.2.1 if

**1**`if 表达式 then 语句`

```vb
2
if 表达式 then
    语句块
end if

3
if 表达式 then
    语句块1
else
    语句块2
end if

4
if 表达式 then
    语句块
else : 语句
end if

5
if 表达式 then 语句1 else 语句2

6
if 表达式1 then
    语句块1
elseif 表达式2 then
    语句块2
else
    语句块
end if
```

**例子：**
![摄氏度与华氏度提示](/img/VB/cfex.png)

#### 5.3.2.2 select

```vb
select case 变量或表达式
    case 表达式列表1    'is 关系运算表达式
        语句块1
    case 表达式列表2
        语句块2
    case else
        语句块
end select
```

**例子：**

![求函数Y的值](/img/VB/yex.png)

### 5.3.3 循环结构

```vb
for 循环变量=初值 to 终值 [step步长]
    语句块
    [exit for]
    语句块
next 循环变量
```

```vb
for each 元素变量 in 数组或集合
    语句块
next 元素变量
```

```vb
先判断后执行
do while 条件
    语句块
loop

do until 条件
    语句块
loop

先执行后判断
do
    语句块
loop while 条件

do
    语句块
loop until 条件


exit do 退出循环体
```

#### 5.3.3.1 for next 循环

- 循环变量是数之变量
- 初值、终值、步长可以是数之表达式
- 步长可正可负，但不能为 0 、为 1 是省略
- exit for 退出循环，经常放到条件语句中
- next 后的循环变量应与 for 语句中的循环变量一致，可以省略

```vb
for 循环变量=初值 to 终值 [step步长]
    语句块
    [exit for]
    语句块
next 循环变量
```

```vb
'--求1+2+3+4+...+n--
private sub command1_click()
    dim n as integer , i as integer , s as integer
    n = val(text1.text)
    s = 0
    for i = 1 to n
        s = s + i
    next i
    label3.caption = s
end sub
```

`for each ... in ... next 循环`

For Each...In...Next 循环结构中元素变量是 变体型变量

```vb
for each 元素变量 in 数组或集合
    语句块
next 元素变量
```

![控件颜色](/img/VB/foreach.png)

#### 5.3.3.2 do...loop 循环结构

```vb
do while 条件
    语句组1
    exit do
    语句组2
loop

细节------------------
先判断后执行---当
do while 条件
    语句块
loop

do until 条件
    语句块
loop

先执行后判断---直到
do
    语句块
loop while 条件

do
    语句块
loop until 条件
```

while true 则循环
until false 则循环

```vb
' 1^2+2^2+....小于n的最大值
private sub command1_click()
    dim n as long , s as long, i as integer
    n = val(text1.text)
    i = 0
    s = 0
    do while s < n
        i = i + 1
        s = s + i * i
    loop
    text2.text = s - i * i
end sub
```

#### 5.3.3.3 循环嵌套

```vb
'----------eg:
for i = 1 to 3
    for j = 5 to 7
        print i , j
    next j
next i

or
next j,i
```

### 5.3.4 goto 语句

`goto{标号|行号}`

![goto例子](/img/VB/gotoex.png)

## 5.4 数组

### 5.4.1 数组

![数组概念](/img/VB/szgn.png)

如：`A(8)`,`B(I)`,`A(A(5))`
`a(1,3)`-二维数组

### 5.4.2 数组定义

`Public|Private|Dim 数组名 维数定义 AS 类型`
`Dim A(-4 TO 10) As Integer`
`Dim A(0 TO 8,0 to 3) As Integer` = `Dim a(8,3) as integer`

#### 5.4.2.1 定义形式

`dim 数组名 ([下界 to]上界) as 数据类型`
下界默认为 0，也可以在 `option base n` 来修改默认下界

#### 5.4.2.2 动态数组的建立与使用

`dim 数组名() [as 数据类型]`先不给大小
`redim 数组名 (8,8,)`具体使用时在给出大小
`redim preserve 数组名(8,newvalue)`改变数组大小，可用 preserve 保留原来的数据

#### 5.4.2.3 控件数组

在窗体上画出控件，进行属性设置

- 复制粘贴，建立控件数组
- 编程时哟个 load 方法

![动态数组的使用](/img/VB/dtszdsy.png)

![输入10个单词，反序输出](/img/VB/fxsc.png)
![输出10个单词，反序输出2](/img/VB/fxsc1.png)
![输出10个单词，反序输出3](/img/VB/fxsc2.png)

```vb
array 数组输入
数组下界到数组上界
ubound(A) to lbound(A)
```

#### 5.4.2.4 数组元素的复制

```vb
option base 1
    dim a(15),b(3,5)
    for i = 1 to 3
        for j = 1 to 5
        b(i,j) = a((i-1) * 5 +j)
        next j
    next i
```

#### 5.4.2.5 for each ... next

```vb
打印一堆数组x中所有元素
dim x(15)
for each a in x
    print a;
next a
```

```vb
求二维数组y的所有元素之和
dim y(10,10)
for each a in y
    sum = sum + a
next a
print sum
```

![保留动态数组的内容](/img/VB/blsznr.png)

### 5.4.3 数组应用举例

#### 5.4.3.1 例子 1

例:生成 20 个 10 到 100 之间的随机整数,存于一维整型数组 A 中,同时显示于第一个文本框中,单击窗体将这 20 个数以相反的次序显示于另一个文本框中
![数组应用](/img/VB/szlz.png)

#### 5.4.3.2 例子 2

![控件数组](/img/VB/szlz1.png)

## 5.5 过程

- 过程的引入:使同类的操作不重复(操作方法相同、参数不同)
- 过程:完成一段独立功能,可供其他过程使用(调用)。过程又称为子程序
- 调用过程:调用其他过程的过程

过程：

- sub 子过程
- function 函数过程
- property 属性过程
- event 事件过程

### 5.5.1 子过程和函数过程

![子过程和函数过程](/img/VB/zgchsgc.png)

调用：

- 子过程名[参数列表]
- Call 子过程名 (参数列表)
- 变量名 = 函数过程名([参数列表])

- public 所有模块的所有其他过程
- private 只有本模块的其他过程
- static 过程中所有的局部变量都为静态变量
- 函数过程名：function 过程的名称
- 形参表：调用时要传递给 function 的参数变量列表

![过程例子](/img/VB/gclz.png)

```vb
定义求阶乘的函数Fact
Function Fact(n As Integer) As Double
    Dim F As Double, i As Integer
    F=1
    For i=1 To n
        F=F * i
    Next i
    Fact =F
End function

Private Sub Command1_Click()
    Dim m As Integer, n As Integer, c As Double
    m= Val(TextI.Text)
    n= Val(Text2.Text)
    c=Fact(m)/(Fact(n)*(Fact(m-n)))'调用Fact
    Text3.Text= Trim(Str(c))
End sub
```

- ◆Sub 过程的建立方法与 Function 过程的建立方法相同。
- ◆<过程名>不具有值的意义,在 Sub 过程中不能给<过程名>赋
  值,也不能给<过程名>定义类型。
- ◆Sub 过程通过<形参表>中的参数返回值。

![sub过程](/img/VB/subgclz.png)

### 5.5.2 参数的传递

![参数传递](/img/VB/cscd.png)

### 5.5.3 代码模块

![代码模块](/img/VB/dmmk.png)

#### 5.5.3.1 窗体模块

事件过程、通用过程、通用声明

#### 5.5.3.2 标准模块

![标准模块](/img/VB/bzmk.png)

#### 5.5.3.3 类模块

在类模块中编写代码建立新对象

### 5.5.4 过程的作用域

![过程作用域](/img/VB/gczyy.png)

![过程作用域例子](/img/VB/gczyylz.png)
![过程作用域例子](/img/VB/gczyylz1.png)

![过程作用域及使用规则](/img/VB/gczyysygz.png)

## 5.6 用户界面设计

### 5.6.1 单选按钮和复选框

单选框只能选一个（Option）
复选框可以选多个（Check）
`click动作`
`check.value = true` 则为被选中

![例子](/img/VB/checklz.png)

### 5.6.2 框架 Frame

框架之间可以隔开单选按钮
`fontname` `fontsize` `forecolor`
属性

### 5.6.3 滚动条

HScroll Bar 、 VScroll Bar
水平、竖直滚动条

- 属性
  MIN 默认 0
  MAX 默认 32767

Value ：设置滚动块在滚动条中的位置值
Smallchange ：最小变动值属性
Largechange ：最大------

- 事件
  Scroll ：当鼠标拖动滚动块时，触发
  Change ： 当改变 value 值时出发

eg：在 text 中显示最大最小值

```vb
text1 = HScroll1.Min
text2 = HScroll2.Max
text3 = HScroll3.Value

HScroll ' 横向
VScroll ' 纵向
```

RGB 函数：
颜色值的取间是 0~255

随机数 Rnd() 返回小于 1 大于或等于 0 的值
Rnd[()]

```vb
private sub form_click()
    text1.forecolor = RGB(255 * Rnd , 255 * Rnd , 255 * Rnd)
    form1.backcolor = RGB(255 * Rnd , 255 * Rnd , 255 * Rnd)
end sub
```

返回小于 1 但大于或等于 0 的值。 Number 的值决定了 Rnd 生成随机数的方式。
在调用 Rnd 之前,先使用无参数的 Randomize 语句初始化随机函数生成器,该
生成器具有根据系统计时器得到的种子。
如果 number 的值是 Randomize 生成。
小于 0,每次都使用 number 作为随机数种子得到相同结果
大于 0,以上一个随机数为种子产生下一个随机数;
等于 0,产生与最近生成的随机数相同的随机数。
省略,以上一个随机数为种子产生下一个随机数
例,Int((上限下限+1)\*Rnd+下限),生成上限与下限之间的随机整数。

### 5.6.4 列表框

只能在程序中设置的属性：
Listindex 执行时选中的列表项的序号
Listcount 项目数量 从 0 开始
Selected True 表示选中相应的项
Text 表示选中列表项文本内容

Additem ： 增加项
Removeitem ： 删除项
Clear ： 清除

属性 style : 1 时为多选框
属性 columns: 几列

```vb
List1.AddItem "1"
List1.AddItem "2"
province = Array("a","b") ' 一维数组

Province(List1.ListIndex) '数组中数据
List1.List(List.ListIndex) = text1

' 判断是否选中
if list1.selected(i) Then
```

### 5.6.5 组合框

style 属性：
0 下拉式
1 简单组合框
2 下拉式列表框

### 5.6.6 驱动器列表框、目录列表框、文件列表框

DriveListBox
DirectoryListBox
FileListBox

```vb
select case index
    case 0
        语句1
    case 1
        语句2
end select

' 打开程序
Retval = shell(dir1.path + "\" + file1.filename,1)
Retval = shell("C:\user\..",1)
```

### 5.6.7 通用对话框

打开、另存为、颜色、字体、打印机、帮助
工程--部件--Microsoft Comm Dialog Control 6.0 选择通用对话框

`对象.Action = 1` 打开文件对话框
`对象.ShowOpen` 打开文件对话框

![通用对话框例子](/img/VB/tongyong.png)

### 5.6.8 菜单设计

普通的菜单设计
工具--菜单编辑器--逐一填写

弹出菜单
对象.PopupMenu 菜单名，标值，x，y
`PopupMenu Cal2,2`

### 5.6.9 多重窗体

工程--添加窗体--打开
load 窗体名称 将窗体装入内存，但不显示
unload 窗体名称

窗体名称.show 显示窗体
窗体名称.hide 隐藏窗体
`form2.show`显示 form1 窗体

### 5.6.10 鼠标/键盘事件

![鼠标事件](/img/VB/sbsj.png)

键盘事件：KeyPress ， KeyUp ， KeyDown

### 5.6.11 对象拖放与 OLE 拖放

对象拖放：用鼠标将对象从一个地方拖动到另一个地方

拖放方式属性：DragMode 为 1 自动 0 手动
拖放图标属性可以在设计时设置，也可在程序中设置
`控件名.DragIcon = 图像控件.picture`
`控件名.DragIcon = LoadPicture("C:\Icons\mail.ico")`

拖放事件

```vb
sub form_dragdrop(source as control , x as single , y as single)
    source.move x,y
end sub
```

OLE 拖放 ：将数据从一个控件或应用程序中移动到另一个控件或应用程序。
**OLEDragMode**属性—决定是自动还是手动实现“拖”操作
**OLEDropMode**属性—决定是自动还是手动实现“放”操作
注:并不是所有的控件都有此二属性,有的只有其一。

- OLEDragDrop 事件—在目标控件上进行“放”操作时发生的事件。
- OLEStartDrag 事件一源控件 OLEDrag 方法被执行或用户做“拖”，操作时发生的事件
- OLEDragOver 事件—在拖动时,经某控件时在该控件上发生的事件

## 5.7 Active X 控件

### 5.7.1 SSTab 选项卡控件

工程--部件--选中 Microsoft Tabbed Dialog Control 6.0

style 属性：选项卡样式--0/1：office 风格/windows 风格
Tabs 属性：控制控件上选项卡的数目
Tab 属性 ：决定控件上当前被选定的项

### 5.7.2 ProgressBar 进度条控件

工程--部件--选中 Microsoft Windows Common Control 6.0

Max 属性：进度条上限
Min 属性：进度条下限
Value ：进度值
Scrolling ： 卷动方向形式
Orientation ： 纵横滚动定位
MousePoint ：鼠标指针

### 5.7.3 Slide 滑动条控件

工程--部件--选中 Microsoft Windows Common Control 6.0

TickStyle ： 决定控件上滑块及刻度的显示样式
TickFrequency ： 决定控件上刻度点的疏密
ToolTipText：指针停在该控件上时显示提示信息
Orientation ：决定控件在窗体上水平或垂直放置

### 5.7.4 MS Chart 控件

工程--部件--选中 Microsoft Chart Control 6.0(OLEDB)

BorderStyle ： 决定图表是否有外框线
ColumnCount ： 每一格的列数
RowCount ： 每一行的列数
ChartType ： 选择图表类型
TitleText ： 图题
ChartData 返回一个数组，该数组包含将要被该图表显示的值

`MSChart1.ChartData = 数组`

![图表控件](/img/VB/tubiao.png)

### 5.7.5 UpDown 控件

工程--部件--选中 Microsoft Windows Common Control-2 6.0

一对箭头按钮控件，单击按钮，增减数值
UpDown 通常与 Textbox 绑定

Max/Min 最大值最小值
Increment 指定每次单击上箭头或下箭头时 Value 的变化量

```vb
private sub updown1_downclick()
    text1.updown1.value
end sub
private sub updow n1_upclick()
    text1.updown1.value
end sub
```

### 5.7.6 ActiveX 控件的创建

ActiveX 是 Microsoft 对于一系列策略性面向对象程序技术和工具称呼,其中主要的技术是组件对象模型(COM)。

![ActiveX的三种表现形式](/img/VB/activex.png)

ActiveX 部件：可执行代码：exe、dll、ocx 文件

ActiveX 控件标准和非标准文件：以 ocx 后缀保存在 Windows\System 目录下
ActiveX 控件分为：控件和插入对象 、可插入对象就是一个应用程序，如 MIcrosoft Word

创造自己的 ActiveX 控件

- 启动 VB，打开 ActiveX 控件
- UserControl 对象，为 AX 控件名称，在此进行控件制作
- 在代码窗口利用工具中的添加过程，为新的 ActiveX 控件添加共有的属性、时间等
- 界面与代码设计好后，在指定目录生成指定的 ocx，完成自制 AX 控件的工作
- 另打开 VB，通过增加部件找到所自制的 AX 控件，放在工具箱上即可使用

## 5.8 文件

![基本概念](/img/VB/file.png)

### 5.8.1 顺序文件

ASCII 文件，由任何字处理文件建立，在 VB 中建立，只能按顺序存取记录

打开文件--读或写文件--关闭文件

#### 5.8.1.1 顺序文件打开

格式 Open <文件名> for 方式 as [#]<文件号>

Input 只读 / Output 写 / Append 添加方式

文件号 1 到 511 之间的整数

`opnn "C:\Data\Stud.dat" For Output As #1`

#### 5.8.1.2 顺序文件关闭

Close 文件号列表

`Close #1`
`Close #1,2,#8`
`Close` 关闭所有

#### 5.8.1.3 顺序文件的读写

**① 写**

1. Write #文件号,[输出列表]

`Write #1,A1,A2,A3`

说明

- <输出列表>中各项之间要用逗号分开
- <输出列表>每一项可以是常量、变量或表达式
- 写到文件中的各数据间自动插入逗号,字符串自动加上双引号
- 所有数据写完后,在最后加入一个回车换行符
- 不含<输出列表>时,将在文件中写入一空行

**学号、姓名、成绩 1、2**保存到文件中

```vb
Option Explicit
Dim no, na, g1, g2 As Variant
Private Sub Command1_Click()
    no = Text1.Text: na = Text2.Text
    g1 = Val(Text3.Text): g2 = Val(Text4.Text)
    Write #2, no, na, g1, g2
    Text1.Text = "": Text2.Text = "": Text3.Text = "": Text4.Text = ""
End Sub

Private Sub Command2_Click()
    Close #2
    End
End Sub

Private Sub Form_Load()
    CommonDialog1.ShowSave
    Open CommonDialog1.FileName For Append As #2
End Sub
```

2. print #文件号，输出列表

`print #2, no ,na, g1, g2`
`print #2, no; na; g1; g2`

将输出列表中的内容写入指定文件
说明

- 当<输出列表>用逗号分隔时,采用分区格式输出
- 当<输出列表>用分号分隔时,采用紧凑格式输出
- 所有项将在一行内输出,输出后将自动换行
- 可以使用 Spc()函数和 Tab()函数

![两者区别](/img/VB/writeprint.png)

**② 读**

1. input #文件号,变量列表
2. Line input #文件号，变量名
3. eof(文件号) 函数

**读取文件中的程序，计算平均成绩**

```vb
Option Explicit
Dim num, nam, s1, s2, ave

Private Sub Command1_Click()
    CommonDialog1.ShowOpen
    Open CommonDialog1.FileName For Input As #3
    Text1.Text = ""
    Do While Not EOF(3)
   ' 装入用Wite# 语句生成的文件
        Input #3, num, nam, s1, s2
        ave = (s1 + s2) / 2
        Text1.Text = Text1.Text & num & "   " & nam _
                        & "   " & Str(s1) & "    " & Str(s2) & _
                        "  " & Str(ave) & Chr(13) & Chr(10)
    Loop
    Close #3
End Sub
```

**计算每个同学的平均成绩，并同时将结果与原数据保存到另一个文件**

```vb
Option Explicit
Dim num(100) As String, nam(100) As String
Dim g(100, 2) As Integer, n As Integer, ave, sum1, sum2, i

Private Sub Command1_Click()
    CommonDialog1.ShowOpen
    Open CommonDialog1.FileName For Input As #3
        n = 0
        Do While Not EOF(3)
            n = n + 1
            Input #3, num(n), nam(n), g(n, 1), g(n, 2)
        Text1.Text = Text1.Text & "   " & num(n) & _
        "   " & nam(n) & "    " & Str(g(n, 1)) & _
        "   " & Str(g(n, 2)) & "    " & Chr(13) & Chr(10)
        Loop
End Sub

Private Sub Command2_Click()
    CommonDialog1.ShowSave
    Open CommonDialog1.FileName For Output As #4
    sum1 = 0
    sum2 = 0
    Text2.Text = ""
    For i = 1 To n
        ave = (g(i, 1) + g(i, 2)) / 2
        Write #4, num(i), nam(i), g(i, 1), g(i, 2), ave
        Text2.Text = Text2.Text & "   " & num(i) & _
        "   " & nam(i) & "   " & Str(g(i, 1)) & "   " & _
        Str(g(i, 2)) & "   " & Str(ave) & vbCrLf
        sum1 = sum1 + g(i, 1): sum2 = sum2 + g(i, 2)
    Next i
    Text2.Text = Text2.Text & "average" & " " & _
    Str(sum1 / n) & "   " & Str(sum2 / n)
    Write #4, "总平均", sum1 / n, sum2 / n
End Sub

Private Sub Command3_Click()
    Close #3, #4
    End
End Sub
```

### 5.8.2 随机文件

读写次序任意，记录长度相等，随机文件中的记录常定义为用户自定义类型

**自定义数据类型操作**

```vb
private/public type 自定义类型名
    元素名 下标 as 类型
end type
```

![](/img/VB/sjwjsm1.png)
![说明](/img/VB/sjwjsm2.png)

![例子](/img/VB/sjwjex.png)
![例子](/img/VB/sjwjex1.png)

#### 5.8.2.1 随机文件打开

`open 文件名 [for random] as 文件号 len= 记录长度`
for random 可以省略
记录长度：就是自定义类型的大小，可以用 len 获得
若文件不存在，则建立新的文件

#### 5.8.2.2 随机文件关闭

`close #2`

#### 5.8.2.3 随机文件写

`put 文件号，记录号，变量名`

![写文件](/img/VB/sjwjxie.png)

#### 5.8.2.4 随机文件读

`get #文件号， 记录号， 变量名`
功能： 将一个一打开的随机文件读入一个变量之中

![例子](/img/VB/sjwjdxex0.png)

![例子](/img/VB/sjwjdxex.png)
![例子](/img/VB/sjwjdxex1.png)

### 5.8.3 总结

![文件操作总结](/img/VB/filezongjie.png)

开闭 写读

- open 语句
- close 语句
- write\print 语句
- input\line input 语句 ， input 函数

---

- open 语句
- close 语句
- put 语句
- get 语句

## 5.9 绘图

### 5.9.1 图形设计基础

#### 5.9.1.1 坐标系统

左上角（0，0）横向 x，纵向 y

1. 刻度单位

![刻度单位](/img/VB/kddw.png)

2. 改变坐标系

**自定义坐标体系**

![自定义坐标体系](/img/VB/zdyzbx.png)

`ScaleLeft` `ScaleTop`属性 ， 窗体左边的坐标，上边的坐标

`ScaleWidth` `ScaleHeight`属性 ，容器对象内部的宽度和高度，将

![例子](/img/VB/zbxex1.png)

![例子](/img/VB/zbxex2.png)

![例子](/img/VB/zbxex3.png)

Scale 方法：
`对象名.Scale[(x1,y1)-(x2,y2)]`

```vb
Private Sub picture1_click()
    dim a(5,5) as integer, i as integer , j as integer
    picture1.scale (0,0)-(6,6)
    for i=1 to 5
        picture1.currenty = i
        for j=1 to 5
            if i = j then a(i,j) = 1 else a(i,j) = 0
            picture1.currentx = j
            picture1.print a(i,j);
    next j,i
end sub
```

![例子](/img/VB/scale.png)

3. 当前坐标

`currentx` `currenty`

4. 位置大小相关属性

![例子](/img/VB/wzdxxg.png)

#### 5.9.1.2 颜色

颜色值：四字节，长整型
RGB    每个字节取值：00-FF （或0-255）

1. 设计阶段设置
2. 运行阶段设置

RGB函数：`RGB(red,green,blue)`
eg:`form1.backcolor = RGB(255,0,0)`

或者

QBColor函数： `QbColor(value)`
value ： 0-7颜色加亮、 8-15
0黑1蓝2绿3青4红5紫红6黄7浅灰色

或者

使用颜色常量
`vbblack` `vbred` `vbgreen` `vbyellow` `vbwhite`
`vbblue`  `vbmagenta洋红` `vbcyan青色` 

或者

使用颜色的十六进制 `&H00BBGGRR&`

使用系统颜色 `vbscrollbars &H80000000`滚动条颜色

### 5.9.2 图形控件

#### 5.9.2.1 Picture控件

可以显示图片，可以作为其他控件的容器

* 设计阶段
* 程序运行中：`LoadPicture()`

`Autosize`为True时 自动调整大小与显示的图片匹配

#### 5.9.2.2 Image控件

可以显示图像，内存占用小
Stretch属性 拉伸位图和图标，适应图像框的大小

#### 5.9.2.3 Shape控件

属性：Shape、FillStyle、BackColor、FillColor等属性

方法：`object.Move left[,top[,width[,height]]]`

![例子](/img/VB/shapeex.png)

#### 5.9.2.4 Line控件

设计时再窗体上绘制直线

`BorderStyle` 、 `BorderWidth`

### 5.9.3 绘图方法

![绘图方法](/img/VB/htff.png)

#### 5.9.3.1 画点方法Pset

`对象名.Pset[step](x,y)[,颜色]`
在对象指定位置，用给定的颜色画点
* Step 可选，指定相对于又currentx和y 属性提供的坐标
* x，y 点的水平和垂直坐标
* 颜色 绘制该店的RGB颜色

![例子1](/img/VB/psetex.png)

![例子2](/img/VB/psetex1.png)
![例子2](/img/VB/psetex2.png)

#### 5.9.3.2 画线、画矩形Line

`对象名.Line[step][(x1,y1)]-[step]\(x2,y2)[,color[,B[F]]]`

![Line](/img/VB/line.png)

![例子1](/img/VB/lineex1.png)

![例子2](/img/VB/lineex2.png)

![例子3](/img/VB/lineex3.png)
![例子3](/img/VB/lineex4.png)

#### 5.9.3.3 画圆 Circle

![画圆](/img/VB/circle.png)

![画圆例子](/img/VB/circleex.png)

![画圆例子1](/img/VB/circleex1.png)
![画圆例子1](/img/VB/circleex2.png)

#### 5.9.3.4 使用point方法返回指定点的颜色

![Point例子](/img/VB/pointex.png)

## 5.10 高级界面设计

### 5.10.1 多文档界面MDI

![MDI](/img/VB/mdi.png)


## 5.11 开发多媒体应用程序

概述：MMControl控件
**播放动作的5个步骤**
* 选择播放设备 DeviceType
* 选择播放文件名 FileName
* 打开文件 Open
* 播放文件 Play
* 关闭 Close

![MCI控件](/img/VB/mci.png)

**MM控件的主要属性和事件**

![MMControl](/img/VB/mmcontrol.png)

![MMCommand](/img/VB/mmccommand.png)

![其他属性](/img/VB/mmcothers.png)

![制作播放器1](/img/VB/mmcmake.png)

![制作播放器2](/img/VB/mmcmake2.png)

![使用API多媒体函数实现播放](/img/VB/api.png)

![使用API多媒体函数实现播放](/img/VB/apiuse.png)

![使用API多媒体函数实现播放](/img/VB/apiuse2.png)

![使用API多媒体函数实现播放](/img/VB/apiuse3.png)

*直接搜API浏览器，打开文件，然后选择需要的函数，拷贝*

**拷贝内容**

```vb
Private Declare Function sndPlaySound Lib "winmm.dll" Alias "sndPlaySoundA" (ByVal lpszSoundName As String, ByVal uFlags As Long) As Long
Private Const SND_ASYNC = &H1         '  play asynchronously
Private Const SND_LOOP = &H8         '  loop the sound until next sndPlaySound
Private Const SND_SYNC = &H0         '  play synchronously (default)
```

![使用API多媒体函数实现播放例子](/img/VB/apiex.png)

![使用API多媒体函数实现播放例子](/img/VB/apiex1.png)

![使用API多媒体函数实现播放例子](/img/VB/apiex2.png)

## 5.12 数据库访问技术

![数据库概念](/img/VB/sjk.png)

**数据库管理系统**
有：Access Interbase SQLServer DB2 MySql 等等

### 5.12.1 关系型数据库
表、记录与字段、关键字、表间关系、外部键、索引

![关系型数据库概念](/img/VB/gxxsjk.png)

![关系型数据库字段、记录、关键字](/img/VB/gxxsjk1.png)

![关系型数据库表间关系](/img/VB/gxxsjk2.png)

![关系型数据库外部键、索引](/img/VB/gxxsjk3.png)

### 5.12.2 用可视化数据管理器建立和维护数据库

![可视化数据管理器](/img/VB/kshsjglq.png)

![可视化数据管理器](/img/VB/kshsjglq1.png)

![可视化数据管理器](/img/VB/kshsjglq2.png)

![可视化数据管理器](/img/VB/kshsjglq3.png)

![可视化数据管理器](/img/VB/kshsjglq4.png)

![可视化数据管理器](/img/VB/kshsjglq5.png)

![可视化数据管理器](/img/VB/kshsjglq6.png)

![可视化数据管理器](/img/VB/kshsjglq7.png)

![可视化数据管理器](/img/VB/kshsjglq8.png)

![可视化数据管理器](/img/VB/kshsjglq9.png)

## 5.13 总复习

### 5.13.1 同心圆
![案例1](/img/VB/txy.png)
![案例1](/img/VB/txy2.png)

### 5.13.2 两圆转动
![案例2](/img/VB/yzyd.png)
![案例2](/img/VB/yzyd2.png)

### 5.13.3 密码输入，文本框飘动
![案例3](/img/VB/mimayd.png)

### 5.13.4 网络连接计时

![案例4](/img/VB/wlljjs.png)
![案例4](/img/VB/wlljjs2.png)

# 6. 课程学习过程中练习

第几次课.第几道练习

## 2.1 勾选要求变量声明（初学）

然后每次使用必须先定义变量

```vb
Option Explicit

Private Sub Command1_Click()
    Dim B As Integer, A As Integer
    B = 10
    A = A + B
    Print B, A
End Sub
'10 10
'10 10
```

```vb
Option Explicit

Private Sub Command1_Click()
    Static B As Integer, A As Integer     '静态变量
    B = 10
    A = A + B
    Print B, A
End Sub
'10 10
'10 20
'10 30
```

Dim 和 Static 都是局部变量可以将其拉到窗体级全局变量

```vb
Option Explicit
    Dim B As Integer, A As Integer
Private Sub Command1_Click()

    B = 10
    A = A + B
    Print B, A
End Sub

Private Sub Command2_Click()
    Print B, A
End Sub
```

## 2.2 字符判断

```vb
Private Sub Text1_Change()
    If Not IsNumeric(Text1) Then
        MsgBox "Text1 输入非法数字，请重新输入"
        Text1.Text = ""
    End If
End Sub
```

## 2.3 inputbox & keypress

```vb
Option Explicit

Private Sub Label2_Click()
    Text3 = Val(Text1) + Val(Text2)
End Sub

Private Sub Text1_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then Text2 = InputBox("请输入")
End Sub

Private Sub Text3_GotFocus()
    Text1 = ""
    Text2 = ""
    Text3 = ""
    Text1.SetFocus
End Sub
```

## 3.1 DIY

**换行 text 的 multline 属性要为 true**
`chr(13) + chr(10)`
`vbcrlf`

```vb
Option Explicit
Dim ID As Boolean

Private Sub Command1_Click()
    ID = True
    Timer1.Interval = 600
    Text1 = "DIY" + Chr(13) + Chr(10) + "程序设计"  '回车换行
End Sub

Private Sub Command2_Click()
    ID = False
    Text1.Alignment = 0 '居左
    Text1.FontSize = 50
    Text1 = "1111" & vbCrLf _
    & "fads" + vbCrLf _
    & "7777" + Chr(13) + Chr(10)  '回车加换行
End Sub

Private Sub Timer1_Timer()
    Dim A As Integer
    Randomize
    A = Rnd * 4      'rnd 0-1
    Text1.ForeColor = RGB(Rnd * 250, Rnd * 250, Rnd * 250)
    If ID Then
        Text1.FontSize = Rnd * 260
        Text1.FontBold = True   '粗体字
        Select Case A
        Case 0
            Text1.FontName = "隶书"
            Text1.Alignment = 0
        Case 1
            Text1.FontName = "黑体"
            Text1.Alignment = 1
        Case 2
            Text1.FontName = "楷体"
            Text1.Alignment = 2
        End Select
    End If
End Sub
```

## 3.2 for

`cls`清屏

```vb
Option Explicit

Private Sub Command1_Click()
    Dim i As Integer, j As Integer
    For i = 1 To 3
        For j = 5 To 7
            Print i, j
        Next j
        Print "---------"
    Next i
End Sub

Private Sub Command2_Click()
    Dim a       '必须用变体
    For Each a In Form1.Controls
        a.BackColor = vbRed
    Next a
End Sub

Private Sub Command3_Click()
    Cls
End Sub
```

## 3.3 for 与 if 可以互换

`goto 111`

```vb
Option Explicit

Private Sub Command1_Click()
    'Dim i As Integer, s As Integer
    Dim i, a, j, b
    For i = 0 To 100
        a = a + i
    Next i
111 If j <= 100 Then
        b = b + j
        j = j + 1
        GoTo 111
    E
    Print a
    Print b
End Sub
```

## 4.1 求积

![例子](/img/VB/kclx4_1.png)

```vb
Private Sub Form DblClick
    Dim a (1 To 5) As integer, b (3 To 8)As Integer
    Dim i As Integer
    For i=1 to 5
        a(i) = i
        picture3.Print a(i)
    For i=3 to 8
        b(i) = i
        Picture4.Print b(i)
    Next i
    MsgBox"开始计算"
    Text1= tim(a())
    Text2= tim(b())
End sub
Function tim(x() As Integer)
    Dim t As double, i As Integer
    t=1
    For i= LBound (x) To UBound(x)
        t= t*x(i)
    Next i
    tim = t
End function
```

## 4.2 控件数组--将五个 shape 从上到下移动

设置好属性---复制，粘贴，名称一样的控件数组

shape1 重命名为 S1

```vb
Option Explicit
    Dim i As Integer

Private Sub Command1_Click()
    Timer1.Interval = 50
End Sub

Private Sub Timer1_Timer()
    For i = 0 To 4
        ' 改变颜色  ---不同颜色
        ' S1(i).BackColor = RGB(Rnd * 250, Rnd * 250, Rnd * 250)
        ' S1(i).BorderColor = RGB(Rnd * 250, Rnd * 250, Rnd * 250)
        If S1(i).Top + S1(i).Height > Form1.ScaleHeight Then
            S1(i).Top = 0
        Else
            S1(i).Top = S1(i).Top + 100
        End If
    Next i
End Sub

Option Explicit
    Dim i As Integer

Private Sub Command1_Click()
    Timer1.Interval = 50
End Sub

Private Sub Timer1_Timer()
    Dim A
    A = RGB(Rnd * 250, Rnd * 250, Rnd * 250)  ' 相同颜色
    For i = 0 To 4
        S1(i).BackColor = A
        S1(i).BorderColor = A
        ' S1(i).BackColor = RGB(Rnd * 250, Rnd * 250, Rnd * 250)
        ' S1(i).BorderColor = RGB(Rnd * 250, Rnd * 250, Rnd * 250)
        If S1(i).Top + S1(i).Height > Form1.ScaleHeight Then
            S1(i).Top = 0
        Else
            S1(i).Top = S1(i).Top + 100
        End If
    Next i
End Sub
```

## 4.3 所有控件的移动

```vb
Option Explicit
    Dim i As Variant  ' 变体型变量

Private Sub Command1_Click()
    For Each i In Form1.Controls
        If i.Top + i.Height > Form1.ScaleHeight Then
            i.Top = 0
        Else
            i.Top = i.Top + 500
        End If
    Next i
End Sub
```

## 4.4 模块、多窗口

`form2.show`打开 form2
新建 module，然后将子过程放入 module，可以在 form1 中调用

```vb
' module1:
Option Explicit

Sub fact(n As Integer, f As Long)
    Dim i As Integer
    f = 1
    For i = 1 To n
        f = f * i
    Next i
End Sub

' form1
Option Explicit

Private Sub Command1_Click()
    Dim s As Long
        Call fact(Val(Text1), s)
        Print Val(Text1); s
        Text1.SetFocus
        Text1 = ""
End Sub

Private Sub Command2_Click()
    Form2.Show
End Sub

' form2
Option Explicit

Private Sub Command1_Click()
    Dim s As Long
    Call fact(8, s)
    Print 8; s
End Sub
```