---
title: Python中openpyxl库的学习
date: 2020-02-22 14:40:22
summary: Python openpyxl的操作方法,用python操作excel
categories: 学习力
tags:
  - Python
---

**Python openpyxl 的操作方法**

> [参考教程](https://www.jb51.net/article/169356.htm)

<!--more-->

# 1. 打开文件夹

**`from openpyxl import Workbook`**

## 1.1 创建

```py
# 实例化
wb = Workbook()
# 激活worksheet
ws = wb.active
```

## 1.2 储存

每个文件操作完之后需要储存

```py
wb.save('文件名.xlsx')
```

## 1.3 打开已有

```py
wb2 = load_workbook('文件名.xlsx')
```

# 2. 创建表

# 2.1 创建表（sheet

```py
# 方式一：插入到最后(default)
ws1 = wb.create_sheet("Mysheet")
# 方式二：插入到最开始的位置
ws2 = wb.create_sheet("Mysheet", 0)
```

## 2.2 选择表

```py
# sheet 名称可以作为 key 进行索引
ws3 = wb["New Title"]
ws4 = wb.get_sheet_by_name("New Title")
```

## 2.3 查看表名（sheet）

```py
# 显示所有表名
print(wb.sheetnames)
['Sheet2', 'New Title', 'Sheet1']
# 遍历所有表
for sheet in wb:
    print(sheet.title)
```

# 3. 单元格

## 3.1 储存数据

```py
#  方式一 数据可以直接分配到单元格中(可以输入公式)
ws['A1'] = 42
# 方式二：可以附加行，从第一列开始附加(从最下方空白处，最左开始)(可以输入多行)
ws.append([1,2,3])
# 方式三：Python 类型会被自动转换
ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")
```

## 3.2 访问单元格（call）

### 3.2.1 单单元格访问

```py
# 方法一
c = ws['A4']
# 方法二：row 行；column 列
d = ws.cell(row=4, column=2, value=10)
# 方法三：只要访问就创建
for i in range(1,101):
    for j in range(1,101):
        ws.cell(row=i, column=j)
```

### 3.2.2 多单元格访问

```py
# 通过切片
cell_range = ws['A1':'C2']

# 通过行(列)
colC = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]

# 通过指定范围(行 → 行)
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)
<Cell Sheet1.A1>
<Cell Sheet1.B1>
<Cell Sheet1.C1>
<Cell Sheet1.A2>
<Cell Sheet1.B2>
<Cell Sheet1.C2>　

# 通过指定范围(列 → 列)
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)
<Cell Sheet1.A1>
<Cell Sheet1.B1>
<Cell Sheet1.C1>
<Cell Sheet1.A2>
<Cell Sheet1.B2>
<Cell Sheet1.C2>

# 遍历所有 方法一
ws = wb.active
ws['C9'] = 'hello world'
tuple(ws.rows)
((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
(<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
...
(<Cell Sheet.A8>, <Cell Sheet.B8>, <Cell Sheet.C8>),
(<Cell Sheet.A9>, <Cell Sheet.B9>, <Cell Sheet.C9>))

# 遍历所有 方法二
tuple(ws.columns)
((<Cell Sheet.A1>,
<Cell Sheet.A2>,
<Cell Sheet.A3>,
...
<Cell Sheet.B7>,
<Cell Sheet.B8>,
<Cell Sheet.B9>),
(<Cell Sheet.C1>,
...
<Cell Sheet.C8>,
<Cell Sheet.C9>))
```

# 4. 其他

## 4.1 改变 sheet 标签按钮颜色

```py
ws.sheet_properties.tabColor = "1072BA"
```

## 4.2 获取最大行，最大列

```py
# 获得最大列和最大行
print(sheet.max_row)
print(sheet.max_column)
```

## 4.3 获取每一行每一列

```py
sheet.rows为生成器, 里面是每一行的数据，每一行又由一个tuple包裹。
sheet.columns类似，不过里面是每个tuple是每一列的单元格。
# 因为按行，所以返回A1, B1, C1这样的顺序
for row in sheet.rows:
  for cell in row:
    print(cell.value)

# A1, A2, A3这样的顺序
for column in sheet.columns:
  for cell in column:
    print(cell.value)
```

## 4.4 根据数字得到字母，根据字母得到数字

```py
from openpyxl.utils import get_column_letter, column_index_from_string

# 根据列的数字返回字母
print(get_column_letter(2)) # B
# 根据字母返回列的数字
print(column_index_from_string('D')) # 4
```

## 4.5 删除工作表

```py
# 方式一
wb.remove(sheet)
# 方式二
del wb[sheet]
```


## 4.6 矩阵置换（行 → 列）

```py
rows = [
  ['Number', 'data1', 'data2'],
  [2, 40, 30],
  [3, 40, 25],
  [4, 50, 30],
  [5, 30, 10],
  [6, 25, 5],
  [7, 50, 10]]

list(zip(*rows))

# out
[('Number', 2, 3, 4, 5, 6, 7),
 ('data1', 40, 40, 50, 30, 25, 50),
 ('data2', 30, 25, 30, 10, 5, 10)]

# 注意 方法会舍弃缺少数据的列(行)
rows = [
  ['Number', 'data1', 'data2'],
  [2, 40  ], # 这里少一个数据
  [3, 40, 25],
  [4, 50, 30],
  [5, 30, 10],
  [6, 25, 5],
  [7, 50, 10],
]
# out
[('Number', 2, 3, 4, 5, 6, 7), ('data1', 40, 40, 50, 30, 25, 50)]
```

## 4.7 设置单元格风格

### 4.7.1 需要导入的类

`from openpyxl.styles import Font, colors, Alignment`

### 4.7.2 字体

```py
bold_itatic_24_font = Font(name='等线', size=24, italic=True, color=colors.RED, bold=True)
# 代码指定了等线24号，加粗斜体，字体颜色红色。直接使用cell的font属性，将Font对象赋值给它
sheet['A1'].font = bold_itatic_24_font
```

### 4.7.3 对齐方式

```py
# 设置B1中的数据垂直居中和水平居中
sheet['B1'].alignment = Alignment(horizontal='center', vertical='center')
```

### 4.7.4 设置行高和列宽

```py
# 第2行行高
sheet.row_dimensions[2].height = 40
# C列列宽
sheet.column_dimensions['C'].width = 30
```

### 4.7.5 合并和拆分单元格

```py
# 合并单元格， 往左上角写入数据即可
sheet.merge_cells('B1:G1') # 合并一行中的几个单元格
sheet.merge_cells('A1:C3') # 合并一个矩形区域中的单元格
```
