---
title: VB的作业和复习
img: 
toc: true
top: false
cover: false
date: 2020-05-07 13:32:49
categories: 学习力
tags:
    - VB
summary: VB作业，因为笔记本里的东西太多了，所以新写一篇
password:
---

# 1. 学习作业

## 1.1 第一次作业

### 1. 倒计时控件

![第一次作业](/img/VB/zy/zy1_1.png)

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

![第一次作业2](/img/VB/zy/zy1_2.png)

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

## 1.2 第二次作业

### 1. 华氏度与摄氏度的转换

![第二次作业1](/img/VB/zy/zy2_1.png)

**作业代码**

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

- VB 中的不等于`<>`
- enabled 可以让控件是否响应用户，如正向转换时，关闭逆向开关；逆向转换时，关闭正向开关

### 2. 二次方程根的求解

![第二次作业2](/img/VB/zy/zy2_2.png)

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

- Dim 声明
- ElseIf 的使用
- MsgBox 的使用 `MsgBox "提示信息"`
- Round(x,2) 约到小数点后几位
- keypress 的应用，可以执行事件

## 1.3 第三次作业

### 所有水仙花数

![第三次作业](/img/VB/zy/zy3.png)

**作业代码**

```vb
Option Explicit

Private Sub Command1_Click()
    Dim a, b, c, num
    For num = 100 To 999
        a = num Mod 10
        b = num \ 10 Mod 10
        c = num \ 100
        If a ^ 3 + b ^ 3 + c ^ 3 = num Then Print num
    Next num
End Sub
```

小知识点：

- `15 mod 10`取余数 5
- `15 \ 10`整数相除得整数 1

## 1.4 第四次作业

### 1. sub 子过程计算和

![第四次作业1](/img/VB/zy/zy4_1.png)

**作业代码**

```vb
Option Explicit

Private Sub Command1_Click()
    Dim sr As Integer, j As Integer, s As Long, f As Long
    sr = Text1.Text
    s = 0
    For j = 1 To sr
        Call Tim(j, f)
        s = s + f
    Next j
    Text2.Text = s
End Sub

Sub Tim(k As Integer, f As Long)
    Dim i As Integer
        f = 0
        For i = 1 To k
            f = f + i
        Next i
End Sub
```

小知识点：

- sub 子过程的编写和调用：call 函数名(参数，返回结果)

### 2. 奖学金等级

![第四次作业2](/img/VB/zy/zy4_2.png)

**作业代码**

```vb
Option Explicit

Private Sub Command1_Click()
    Dim m1 As Long, m2 As Long, m3 As Long, jg As Long
    m1 = Text1.Text: m2 = Text2.Text: m3 = Text3.Text
    Call pd(m1, m2, m3, jg)
    If jg = 1 Then
        Text4.Text = "一等奖"
    ElseIf jg = 2 Then
        Text4.Text = "二等奖"
    ElseIf jg = 3 Then
        Text4.Text = "三等奖"
    Else
        Text4.Text = "没有奖"
    End If
End Sub

Sub pd(f1 As Long, f2 As Long, f3 As Long, jg As Long)
    Dim fpj As Long, p1 As Integer, p2 As Integer, p3 As Integer
    Dim f(1 To 3) As Integer, i As Variant
    fpj = (f1 + f2 + f3) / 3
    f(1) = f1: f(2) = f2: f(3) = f3
    p1 = 0: p2 = 0: p3 = 0
    For Each i In f
        If i = 100 Then
            p1 = p1 + 1
        End If
        If i >= 80 Then
            p2 = p2 + 1
        End If
        If i >= 75 Then
            p3 = p3 + 1
        End If
    Next i
    If (fpj > 95) Or (p1 >= 2 And p2 = 3) Then
        jg = 1
    ElseIf (fpj > 90) Or (p1 >= 1 And p3 = 3) Then
        jg = 2
    ElseIf p3 = 3 Then
        jg = 3
    End If
End Sub

Private Sub Text4_Click()
    Text1.Text = "": Text2.Text = "": Text3.Text = "": Text4.Text = ""
End Sub
```

重点注意：

- `for each a in f` 中的 a 必须是变体型变量

## 1.5 第五次作业

### 1. RGB 三色调色板

![第五次作业1](/img/VB/zy/zy5_1.png)

**作业代码**

```vb
Option Explicit
Dim r As Integer, g As Integer, b As Integer

Private Sub Command1_Click()
    Text2.ForeColor = Text1.BackColor
End Sub

Private Sub Command2_Click()
    Text2.BackColor = Text1.BackColor
End Sub

Private Sub HScroll1_Change()
    r = HScroll1.Value: g = HScroll2.Value: b = HScroll3.Value
    Text1.BackColor = RGB(r, g, b)
End Sub

Private Sub HScroll2_Change()
    r = HScroll1.Value: g = HScroll2.Value: b = HScroll3.Value
    Text1.BackColor = RGB(r, g, b)
End Sub

Private Sub HScroll3_Change()
    r = HScroll1.Value: g = HScroll2.Value: b = HScroll3.Value
    Text1.BackColor = RGB(r, g, b)
End Sub
```

小知识点：

- hscroll1.value 横向滚动条的值
- hscroll1_change() 判断横向滚动条的值是否发生变化,变化时执行的程序
- RGB()函数的使用

### 2. 成绩合计 & 密码验证

![第五次作业2](/img/VB/zy/zy5_2.png)

**作业代码 1**

```vb
Option Explicit
Dim i As Integer, t As Integer

Private Sub Command1_Click()
    t = 0
    For i = 0 To 4
        If Check1(i).Value Then
            t = t + Val(Text1(i).Text)
        End If
    Next i
    Text2.Text = t
End Sub
```

小知识点：

- 控件数组的使用
- check1.value 为 true 直接判断

**作业代码 2**

```vb
' Form2
Option Explicit
Dim reval As Integer

Private Sub bl_Click()
    reval = Shell("C:\Users\20180\Desktop\bz-live.bat", 2)
End Sub

Private Sub fb_Click()
    reval = Shell("C:\Users\20180\Desktop\fund.bat", 2)
End Sub

Private Sub Form_Click()
    PopupMenu b, 2
End Sub

Private Sub sc_Click()
    reval = Shell("C:\Users\20180\Desktop\scrcpy.bat", 2)
End Sub

Private Sub tc_Click()
    reval = Shell("C:\Users\20180\Desktop\timecal.bat", 2)
End Sub

'Form1

Option Explicit

Private Sub Command1_Click()
    If Text1.Text = "123" Then
        Form1.Hide
        Form2.Show
    Else
        Label2.Visible = True
        Label2.Caption = "password error"
        Text1.Text = ""
    End If
End Sub

Private Sub Form_Load()
    Label2.Visible = False
End Sub
```

小知识点：

- 主要是菜单的编辑，工具--菜单编辑器
- form1.hide & form2.show 窗体的隐藏和显示
- `reval = shell("C:\Users\20180\Desktop\fund.bat",2)`调用程序

## 1.6 第六次作业

### 学生成绩的录入、统计图表输出应用程序

![第六次作业](/img/VB/zy/zy6.png)

**作业代码**

**form1**

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
    Form2.Show
End Sub

Private Sub Form_Load()
    CommonDialog1.ShowSave
    Open CommonDialog1.FileName For Append As #2
End Sub
```

**form2**

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
        Text2.Text = Text2.Text & "    " & num(i) & _
        "    " & nam(i) & "    " & Str(g(i, 1)) & "    " & _
        Str(g(i, 2)) & "    " & Str(ave) & vbCrLf
        sum1 = sum1 + g(i, 1): sum2 = sum2 + g(i, 2)
    Next i
    Text2.Text = Text2.Text & "总平均" & " " & _
    Str(sum1 / n) & "   " & Str(sum2 / n)
    Write #4, "总平均", sum1 / n, sum2 / n
End Sub

Private Sub Command3_Click()
    Close #3, #4
    End
End Sub

Private Sub Command4_Click()
    Form3.Show
End Sub
```

**form3**

```vb
Option Explicit
Dim arrvalues(1 To 3, 1 To 3), num, nam
Dim s1, s2 As Integer
Dim i As Integer

Private Sub Command1_Click()
    CommonDialog1.ShowOpen
    Open CommonDialog1.FileName For Input As #5
    i = 1
    Do While Not EOF(5)
        Input #5, num, nam, s1, s2
        arrvalues(i, 1) = nam
        arrvalues(i, 2) = s1
        arrvalues(i, 3) = s2
        i = i + 1
    Loop
    MSChart1.ChartData = arrvalues
    Close #5
End Sub
```

小知识点：

- 主要是文件的读取和写入
- 条形图的绘制`CommonDialog`控件

## 1.7 第七次作业

![第七次作业](/img/VB/zy/zy7.png)

**作业代码**

```vb
Option Explicit
Dim i, t, x, y, pcolor As Variant

Private Sub Form_Click()
    Picture1.Scale (-1, 1)-(1, -1)
    Picture1.DrawWidth = 3
    Picture1.Line (-1, 0)-(1, 0), vbBl
    Picture1.Line (0, 1)-(0, -1), vbBlue
    Picture1.DrawWidth = 1
    For i = -1 To 1 Step 0.1
        Picture1.Line (i, 0.05)-(i, 0)
    Next i
    Timer1.Interval = 10
End Sub

Private Sub Timer1_Timer()
    Picture1.DrawWidth = 2
    pcolor = RGB(Rnd * 255, Rnd * 255, Rnd * 255)
    For t = 0 To 2 * 3.1415925 Step 0.001
        x = Sin(2 * t) * Cos(t)
        y = Sin(2 * t) * Sin(t)
        Picture1.PSet (x, y), pcolor
        Next t
End Sub
```

小知识点：

- Scale(x1,y1)-(x2,y2) 坐标轴的范围分成多少份
- PSet画点，一系列的点组成先线（用for循环）
