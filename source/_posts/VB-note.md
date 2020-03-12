---
title: VB-Note
date: 2020-02-16 13:32:49
top: true
img: /img/cover/vb.jpg
summary: VB语言学习过程，这个学期开始学习VB，提前作预习
categories: 学习力
tags:
  - VB
  - Note
---

**VB 语言学习笔记**

> [参考教程](https://www.vbtutor.net/chinese/vbtutor_Chinese.html) _ Visual Basic 是一种相当容易学习的高阶程序语言，它可使你编写几乎任何的程序_

<!--more-->

# 1. 第一个 VB 程序`Hello World`

```vb
Private Sub Form_Load ( )

Form1.show

Print "Hello World"

End Sub
```

## 1.1 几个小例子

```vb
Private Sub Form_Activate ( )

Print 20 + 10
Print 20 - 10
Print 20 * 10
Print 20 / 10

End Sub

# or

Private Sub Form_Activate ( )

Print 20 + 10, 20 ?10, 20 * 10, 20 / 10

End Sub

# or

Private Sub Form_Activate ( )

x = 20
y = 10
Print x + y
Print x - y
Print x * y
Print x / y

End Sub
```

## 1.2 让程序窗口固定不变

|  属性窗口   |    设置为    |
| :---------: | :----------: |
| BorderStyle | Fixed Single |
|  MaxButton  |    False     |
|  minButton  |     True     |

# 2. 控件&控件的属性

## 2.1 控件的属性

- 可以在属性窗口里修改
  ![属性窗口](/img/VB/VB2_1.jpg)
- 也可以在代码中实现修改

```VB
Private Sub Form_Load()
Form1.Show
Form1.BackColor = &H000000FF&
End Sub
## 窗口背景颜色
```

```vb
Private Sub Form_Load()
Shape1.Shape = 3
End Sub
## shape控件形状
```

## 2.2 常见控件

![控件介绍](/img/VB/VB2_2.jpg)

### 2.2.1 文本框(TextBox)

文本框是是用来接收用户输入的控件，以及作为显示器输出。它可以处理字符串（纯文字）和数字数据，但不能处理图象或图片。一个文本框中的文字可以用 Val 函数来转换为数字和数据

```vb
Private Sub Command1_Click()

‘把文本框1和文本框2的值加起来

Sum = Val(Text1.Text) + Val(Text2.Text)

‘中标签上显示答案

Label1.Caption = Sum

End Sub
```

### 2.2.2 标签(Label)

- 标签是一个非常有用处的控件，因为它不仅是用来提供指示和指导，它也可以被用来显示输出。它的一个最重要的特性是标题
- 利用语法 Label.Caption ，它可以显示文字和数字数据。你可以在属性窗口或在运行时改变它的标题

### 2.2.3 命令按钮(CommandButton)

命令按钮是一个很重要的控件，因为它被户点击它时可以执行命令去运作一个程序

```vb
Private Sub Command1_Click ()

Statements

End Sub
```

### 2.2.4 图片框(PictureBox)

图片框可用来处理图形。你可以下载一个图片，在设计阶段就在属性窗口从选定的文件夹选择图片。您也可以在程序运行时加载图片，其指令是 LoadPicture

```vb
Picture1.Picture=LoadPicture ("C:\VB program\Images\grape.gif")
```

### 2.2.5 图像方框(Image)

图像方框 是另一个处理图象和照片的控件。它和图片框的功能几乎是相同的。不过，其中有一个重大的区别，它可以调整大小,它也可以用 LoadPicture 方法来加载图片

### 2.2.6 列表框(ListBox)

列表框的功能是陈列一个项目清单以便用户可以通过点击来选择项目。如果要增加项目，我们可以利用 additem 方法

```vb
Private Sub Form_Load ( )

List1.AddItem “第一课”

List1.AddItem “第二课”

List1.AddItem “第三课”

List1.AddItem “第四课”

End Sub
```

### 2.2.7 组合框(ComboBox)

组合框展现一个下拉式项目清单。用户可以通过点击来选择项目，从名单上。为了增添项目名单，我们可以利用 AddItem `这方法

```vb
Private Sub Form_Load ( )

Combo1.AddItem “Item1”

Combo1.AddItem “Item2”

Combo1.AddItem “Item3”

Combo1.AddItem “Item4”

End Sub
```

### 2.2.8 复选框(CheckBox)

- 复选框让用户可以选择或取消选择一个选项。当复选框被选中时，其值是设定为 1。如不被选中，其值设定为 0\_
- 你可以用程序来设定复选框的属性，如键入 check1.value = 1 ，就表示它被选中，check1.value = 0 就表示它不被选中，并用它来执行某些动作

```vb
Private Sub Check1_Click ()

If Check1.Value = 0 Then

Form1.BackColor = vbRed

ElseIf Check1.Value = 1 Then

Form1.BackColor = vbBlue

End If

End Sub
```

### 2.2.9 选项框(OptionButton)

选项框也可以让用户自由选择一个项目。但是，在同一时间中只有一个选项框可被选择。当一个选项框被选定时，其价值被设定为"True"时，反之则其价值被设定为"False

```vb
Private Sub Option1_Click ( )

Shape1.Shape = 0

End Sub

Private Sub Option2_Click()

Shape1.Shape = 1

End Sub

Private Sub Option3_Click()

Shape1.Shape = 2

End Sub

Private Sub Option4_Click()

Shape1.Shape = 3

End Sub

Private Sub Option5_Click()

Shape1.Shape = 4

End Sub

Private Sub Option6_Click()

Shape1.Shape = 5

End Sub
```

### 2.2.10 驱动器列表框(DriveListBox)

驱动器列表框，是用来显示在您的计算机上所有的驱动器。当你把这个控件纳入表格然后去运行程序，你将能够选择不同的驱动器

### 2.2.11 目录列表框(DirListBox)

目录列表框是用来显示清单目录或文件夹中选择一个驱动器。当你把这个控件纳入表格然后去运行程序，你将能够从所选驱动器中选择不同的目录

### 2.2.12 文件列表框(FileListBox)

文件列表框是用来显示文件列表在选定的目录或文件夹。当你把这个控件纳入表格然后去运行程序，你将能够从文件的列表中选择一个目录

# 3. 编写 VB 的程序代码

```vb
Private Sub Command1_Click
  程序代码
End Sub
```

_Sub 实际上是整个程序的一部分, 也称为子程序_
用来设定一个对象的属性或传递价值于它的语法是：`object.property` _对象和属性是以一个点来分开_
举例

- form1.show 的意思是显示表 1
- label1.visible =true 的意思是把 label1 设置为可被显示
- Text1.text = " VB6" ，目的就是要把 VB6 显示于 text1 的文本框中
- Text2.text = 100 ，是把 100 的数目显示于 text2 文本框中
- Timer1.enabled =false，是要禁用 Timer1 计时器

**几个例子**

```vb
Private Sub Command1_click

Label1.Visible=false

Label2.Visible=True

Text1.Text=”你是正确的!”

End sub
----
Private Sub Command1_click

Label1.Caption=” 欢迎”

Image1.visible=true

End sub
----
Private Sub Command1_click

Pictuire1.Show=true

Timer1.Enabled=True

Lable1.Caption=”开始计数“

End sub
```

**两个重要的 VB 函数：VAL 和 STR**
_VAL 的作用把键入文本框的文字转换成数值， 而 STR 刚好相反，它是把数值转换成字串_

```vb
Private Sub Form_Activate()

  Text3.text=text1.text+text2.text

End Sub
# 输入 12 ， 3
# 得到 123
```

```vb
Private Sub Form_Activate()

  Text3.text=val(text1.text)+val(text2.text)

End Sub
# 输入 12 ，3
# 得到 15
```

# 4. VB 数据处理

## 4.1 VB 基本数据

### 4.1.1 数字数据

数字数据是由数目构成的数据，可以进行数字运算，如加，减，乘，除等

|   类型   |                                                     取值范围                                                      |
| :------: | :---------------------------------------------------------------------------------------------------------------: |
|   Byte   |                                                     0 至 255                                                      |
| Integer  |                                                 -32,768 至 32,767                                                 |
|   Long   |                                          -2,147,483,648 至 2,147,483,648                                          |
|  Single  |                     -3.402823E+38 至 -1.401298E-45 负 &&&& 1.401298E-45 至 3.402823E+38 正数.                     |
|  Double  |  -1.79769313486232e+308 至 -4.94065645841247E-324 负数 &&&& 4.94065645841247E-324 至 1.79769313486232e+308 正数.  |
| Currency |                               -922,337,203,685,477.5808 至 922,337,203,685,477.5807                               |
| Decimal  | +/- 79,228,162,514,264,337,593,543,950,335 如果没有小数点 &&&& +/- 7.9228162514264337593543950335 (28 个小数点）. |

### 4.1.2 非数据类型

|          类型           |                    范围                     |
| :---------------------: | :-----------------------------------------: |
|  String(fixed length)   |              1 to 65,400 字符               |
| String(variable length) |               0 to 20 亿 字符               |
|          Date           | 公元 100 年正月一日至 9999 年十二月三十一日 |
|         Boolean         |           True 或 False（对或错）           |
|         Object          |                任何嵌入对象                 |
|    Variant(numeric)     |             任何价值大如 Double             |
|      Variant(text)      |       与 variable-length string 相同        |

### 4.1.3 后缀文的符号

后缀文是让你把数字转让给一个数据. 在某些情况下，我们需要在一个字的后面增加一个后缀文，使 VB 可以计算得更准确

| 后缀 | 数据类型 |
| :--: | :------: |
|  &   |   Long   |
|  !   |  Single  |
|  #   |  Double  |
|  @   | Currency |

此外，我们需要把字符串文字用开关引号 " " 围起来，日期和时间则用#标志围起来。字符串可以包含任何字符，包括数字

```vb
memberName="Turban, John."
TelNumber="1800-900-888-777"
LastDay=#31-Dec-00#
ExpTime=#12:00 am#
```

## 4.2 变数的管理(变量)

### 4.2.1 变数名称

**为变数命名时的规则**

- 它必须小于 255 个字符
- 不得有间隔
- 不能以号码来开始
- 不能用点

### 4.2.2 变数的宣示

`Dim variableName as DataType`

```vb
Dim password As String
Dim yourName As String
Dim firstnum As Integer
Dim secondnum As Integer
Dim total As Integer
Dim doDate As Date

# or

Dim password As String,  yourName As String, firstnum As Integer,.............
```

假如我们没有特别指明数据类型， VB 将自动宣告变数的类型
要宣示字符串，有两种可能的方式，一为可变长度的字符串，另一个为固定长度字符串。为可变长度的字符串，只是用同样的格式
对于固定长度字符串，你必须使用如下的格式:Dim VariableName as String _ n  
如：`Dim yourName as String _ 10`

## 4.3 VB 的常数和变数

### 4.3.1 常数

常数代表固定不变的数据，它可能是数字或文字。在使用常数时，我们必须预先宣示它们
宣示常数的格式是：`Const constantname As datatype=initializer`
constantname 是我们自己制定的名称，datatype 是资料类型而 initializer 则是初始设定值

如下例子

```vb
Const  Num  As Integer = 9.8

Const Pi As Single  = 3.142

Const SchoolName As String  = "中华中学“
```

### 4.3.2 变数

变数是在程序运送时会改变的数据，而常数在运算时是固定不变的。虽然我们在开始时可给于变数一个数值（初始值），但在程序运作时它的数值是可以改变的
变数的宣告格式如下：`Dim VariableName as Datatype[=initializer]`

如下例字

```vb
Dim Num As Single=1.234

Dim Num1,Num2  As Integer

Dim yourName As String

Dim starName As String="刘翔”
```

以 Dim 宣告各种变数 之后, 我们可以用以下的格式 赋值于这些变数 Variable=Expression

变数可以是一个已宣布的变数或控件的属性值. 它也可以是一个数学表达式, 一个字符串, 一个 布尔值 (对或错) 等等

### 4.3.3 VB 运算符

| 运算符 |       数学函数       |
| :----: | :------------------: |
|   ^    |         指数         |
|   \*   |         乘法         |
|   /    |         除法         |
|  Mod   |     整除后的余数     |
|   \\   |   整数除法 19\4=4    |
|  +or&  | 字串串连"v"&"b"="vb" |

**几个例子**

```vb
Dim firstName As String

Dim secondName As String

Dim yourName As String

Private Sub Command1_Click()

firstName = Text1.Text

secondName = Text2.Text

yourName = secondName + "  " + firstName

Label1.Caption = yourName

End Sub
```

```vb
Dim number1, number2, number3 as Integer

Dim total, average as variant

Private sub Form_Click

number1=val(Text1.Text)
number2=val(Text2.Text)
number3= val(Text3.Text)

Total=number1+number2+number3

Average=Total/5

Label1.Caption=Total

Label2.Caption=Average

End Sub
```

---

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

# 7. 学习作业

## 7.1 第一次作业

### 1. 倒计时控件

![作业要求图片](https://course-proxy2.buct.edu.cn/meol/common/ckeditor/openfile.jsp?id=DBCPDDDHDEDIDGDJCPGJGNGBGHGFCOHAGOGH)

**作业代码**

```vb
Private Sub Command1_Click()
    Timer1.Interval = 50
End Sub

Private Sub Command2_Click()
    End
End Sub

Private Sub Timer1_Timer()
    Text2.Text = Format(Now(), "yyyy/MM/dd hh:mm:ss")
    Text3.Text = #10/1/2020# - Date & "天"
    Text1.Text = "2020-10-01"
End Sub
```

剩下的随便改改 bg，caption，font 等等的

小知识点：

- Access Key: 再名称前加& &emsp;`即&s`
- 关于日期的格式，参考[Format 函数](https://blog.csdn.net/bigheadsheep/article/details/12013267)这篇文章

小问题：

- 怎么把输入的日期格式化为计算数据,不会更高级的输入转化，只能先死输入

解决：

- 使用 CDate 函数将字符串转化为日期

新的问题：

- 在重新输到`2020-10-` 的时候会报错

解决：

- 添加一行代码

完全版代码

```vb
Private Sub Command1_Click()
    Timer1.Interval = 50
End Sub

Private Sub Command2_Click()
    End
End Sub

Private Sub Text1_Click()
    Text1 = ""
End Sub

Private Sub Timer1_Timer()
    Text2.Text = Format(Now(), "yyyy/MM/dd hh:mm:ss")
    yy = Val(Left$(Text1.Text$, 4))   '  text1中的年
    mon = Val(Mid$(Text1.Text$, 6, 2)) '          月
    dday = Val(Right$(Text1.Text$, 2))  '         日

    If Text1.Text = "" Then
        Text3.Text = ""
    Else                      ' 加入判断 让到 - 的时候自动补全
        If Text1.Text = yy & "-" & mon & "-" Then
            t1 = Text1.Text & "01"
            Text3.Text = CDate(t1) - Date & "天"
        Else
            Text3.Text = CDate(Text1.Text) - Date & "天"
        End If
    End If
End Sub
```

### 2. 加法运算器

![作业要求图片](https://course-proxy2.buct.edu.cn/meol/common/ckeditor/openfile.jsp?id=DBCPDDDHDEDIDGDGCPGJGNGBGHGFCOHAGOGH)

**作业代码**

```vb
Private Sub Command1_Click(Index As Integer)
    Text3.Text = Val(Text1.Text) + Val(Text2.Text)
End Sub

Private Sub Command2_Click(Index As Integer)
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text1.SetFocus
End Sub

Private Sub Command3_Click()
    End
End Sub
```

小知识点：

- `Text1.SetFocus`按下按钮后将鼠标指针重新指回`Text1`的位置，即使焦点回到加数 A 框
- val 将字符型数据转换为数值型数据，str 将数值型转换为字符型

## 7.2 第二次作业

### 1. 华氏度与摄氏度的转换

![作业要求图片](https://course-proxy2.buct.edu.cn/meol/common/ckeditor/openfile.jsp?id=DBCPDEDFDADGDFDFCPGJGNGBGHGFCOHAGOGH)

```vb
Option Explicit
Dim C As Variant, F As Variant, CI As Double, FI As Double

Private Sub Form_Load()
    Label4.Enabled = False
    Timer1.Interval = 50
End Sub

Private Sub label3_click()
    C = Text1.Text
    If IsNumeric(C) Then
        CI = Val(C)
        FI = Round(9 / 5 * CI + 32, 1)
        Text2.Text = FI
    Else
        MsgBox "摄氏度不是数"
        Text1.Text = ""
    End If
End Sub

Private Sub Label4_Click()
    F = Text2.Text
    If IsNumeric(F) Then
        FI = Val(F)
        CI = Round(5 / 9 * (FI - 32), 1)
        Text1.Text = CI
    Else
        MsgBox "华氏度不是数"
        Text2.Text = ""
    End If
End Sub

Private Sub Text1_Click()
    Label3.Enabled = True: Label4.Enabled = False
    Text1.Text = "": Text2.Text = ""
End Sub

Private Sub Text1_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then label3_click
End Sub

Private Sub Text2_Click()
    Label4.Enabled = True: Label3.Enabled = False
    Text1.Text = "": Text2.Text = ""
End Sub

Private Sub Text2_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then Label4_Click
End Sub

Private Sub Timer1_Timer()
    C = Text1.Text: F = Text2.Text
    If C <> "" Or F <> "" Then
        label3_click
        Label4_Click
    End If
End Sub
```

小知识点：
- VB中的不等于`<>`
- enabled可以让控件是否响应用户，如正向转换时，关闭逆向开关；逆向转换时，关闭正向开关


### 2. 二次方程根的求解

![作业要求图片](https://course-proxy2.buct.edu.cn/meol/common/ckeditor/openfile.jsp?id=DBCPDEDFDADGDEDFCPGJGNGBGHGFCOHAGOGH)

**作业代码**

```vb
Option Explicit
Dim a As Variant, b As Variant, c As Variant, x1 As Variant, x2 As Variant
Dim ai As Double, bi As Double, ci As Double, dta As Double, xs1 As Double, xs2 As Double, xx1 As Double, xx2 As Double

Private Sub Command1_Click()
    a = Text1.Text: b = Text2.Text: c = Text3.Text
    If IsNumeric(a) And IsNumeric(b) And IsNumeric(c) Then
        ai = Val(a): bi = Val(b): ci = Val(c)
        dta = bi ^ 2 - 4 * ai * ci
        If dta > 0 Then
            x1 = (-bi + Sqr(dta)) / (2 * ai)
            x2 = (-bi - Sqr(dta)) / (2 * ai)
            Text4.Text = x1
            Text5.Text = x2
        ElseIf dta = 0 Then
            x1 = (-bi) / (2 * ai)
            x2 = (-bi) / (2 * ai)
            Text4.Text = x1
            Text5.Text = x2
        Else
            xs1 = Round((-bi) / (2 * ai), 2)
            xx1 = Round(Sqr(-dta) / (2 * ai), 2)
            Text4.Text = Str(xs1) & "+" & Str(xx1) & "i"
            xs2 = Round((-bi) / (2 * ai), 2)
            xx2 = Round(Sqr(-dta) / (2 * ai), 2)
            Text5.Text = Str(xs2) & "-" & Str(xx2) & "i"
        End If
    Else
        MsgBox "abc不全是数字"
    End If
End Sub

Private Sub Command2_Click()
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text4.Text = ""
    Text5.Text = ""
    Text1.SetFocus
End Sub

Private Sub Command3_Click()
    End
End Sub

Private Sub Text1_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then Command1_Click
End Sub
Private Sub Text2_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then Command1_Click
End Sub
Private Sub Text3_KeyPress(KeyAscii As Integer)
    If KeyAscii = 13 Then Command1_Click
End Sub
```

小知识点：

- Dim声明
- ElseIf的使用
- MsgBox的使用  `MsgBox "提示信息"`
- Round(x,2)  约到小数点后几位
- keypress 的应用，可以执行事件