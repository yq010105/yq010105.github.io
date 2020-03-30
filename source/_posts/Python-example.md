---
title: Python Example
top: false
cover: false
date: 2020-03-21 22:45:11
categories:	技术力
tags:
	- Python
summary: python写的几个小程序
password:
---

# 1. 每日手动记录支付宝基金余额

```python
import openpyxl as xl
from openpyxl import Workbook
import os
import time
import plotly.offline as ptly 
import plotly.graph_objs as go
import pandas as pd

def daily_init():
    wb = Workbook()
    ws = wb.active
    ws['A1'] = '日期'
    ws['B1'] = '基金余额'
    ws['A2'] = '03/21/20'
    ws['B2'] = 10.00
    wb.save('fund.xlsx')

def daily_save():
    filex = "fund.xlsx"
    if os.path.exists(filex):
        wb = xl.load_workbook('fund.xlsx')
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        sheet = wb['Sheet']

    ws = wb.active
    ws['A1'] = '日期'
    ws['B1'] = '基金余额'
    ws['A2'] = '03/21/20'
    ws['B2'] = 10.00

    today = datag()
    td_yues = today[1]
    td_yue = td_yues[sheet.max_row-2]
    daily = float(input("\n请输入今天的收益/亏损："))
    yue = td_yue + daily
    
    dt = time.strftime("%D", time.localtime()) 
    maxrow = sheet.max_row + 1
    ws.cell(row=maxrow,column=1,value=dt)
    ws.cell(row=maxrow,column=2,value=yue)
    
    print(f'\n数据已保存:{dt} \t {yue} \n')
    wb.save('fund.xlsx')

def datag():
    filex = 'fund.xlsx'
    if os.path.exists(filex):
        wb = xl.load_workbook('fund.xlsx')
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        sheet = wb['Sheet']

    ws = wb.active
    dts = []
    yues = []
    for row in ws.iter_rows(min_row=2, min_col=1,max_col=1,max_row=sheet.max_row ):
        for cell in row:
            dts.append(str(cell.value))
    for row in ws.iter_rows(min_row=2, min_col=2,max_col=2,max_row=sheet.max_row ):
        for cell in row:
            yues.append(cell.value)
    wb.save('fund.xlsx')
    return dts,yues

def datalook():
    wb = xl.load_workbook('fund.xlsx')
    sheet = wb['Sheet']
    ws = wb.active
    dts = []
    yues = []
    for row in ws.iter_rows(min_row=2, min_col=1,max_col=1,max_row=sheet.max_row ):
        for cell in row:
            dts.append(str(cell.value))
    for row in ws.iter_rows(min_row=2, min_col=2,max_col=2,max_row=sheet.max_row ):
        for cell in row:
            yues.append(cell.value)
    for i in range(sheet.max_row-1):
        print(dts[i],end='\t')
        print(yues[i])

# def check():
#     # 读取Excel中Sheet中的数据
#     data = pd.DataFrame(pd.read_excel('fund.xlsx', 'Sheet'))

#     # 查看读取数据内容
#     print(data)

#     # 查看是否有重复行
#     re_row = data.duplicated()
#     print(re_row)

#     # 查看去除重复行的数据
#     no_re_row = data.drop_duplicates()
#     print(no_re_row)

#     # 查看基于[物品]列去除重复行的数据
#     wp = data.drop_duplicates(['日期'])
#     print(wp)

#     # 将去除重复行的数据输出到excel表中
#     no_re_row.to_excel("fund.xlsx")

def qs():
    dys = datag()
    dts = dys[0]
    yues = dys[1]
    data = []

    trace1 = go.Scatter(x=dts,
                        y=yues,
                        mode='lines+markers',  # mode可选'markers','lines','lines+markers'
                        name= 'Money',
                        marker=dict(size=10,  # 若设为变量则可用散点大小表示变量大小
                                    color='rgba(152, 0, 0, .8)',
                                    line=dict(width=2,
                                                color='rgb(0, 0, 0)'
                                                ),
                                    opacity=[]
                                    )
                        )
    data.append(trace1)
    axis_template = dict(
        showgrid=True,  # 网格
        zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
        nticks=20,
        showline=True,
        title='Date',
        mirror='all',
        zerolinecolor="#FF0000"
    )
    ayis_template = dict(
        showgrid=True,  # 网格
        zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
        nticks=20,
        showline=True,
        title='Money',
        mirror='all',
        zerolinecolor="#FF0000"
    )
    layout = go.Layout(font=dict(family='Courier New, monospace', size=18, color='#3D3D3D'),
                        title='基金实况' ,xaxis=axis_template,yaxis=ayis_template
                        )
    fig = go.Figure(data=data, layout=layout)
    ptly.plot(fig, filename='fund.html')

if __name__ == "__main__":
    filexx = 'fund.xlsx'
    if not os.path.exists(filexx):
        print('----什么？这是你的第一次？好了，已经帮你弄好了（指初始化）----')
        daily_init()
        exit()
    else: 
        p = int(input('今天是否保存过数据了呢？0/1：'))
        if p == 1 :
            print('\n----哦，你已经好了？那算了----\n')
        else:
            daily_save()
            print('----好了，保存好了----\n')
    pd = int(input('想不想看一下趋势图-0/1：'))
    if pd == 1 :
        print('\n----那就给你看一下吧----\n')
        qs()
        datalook()
    else:
        print('\n----既然不想看，那就算了吧----')
```

然后可以再桌面新建一个`fund.bat`脚本直接运行

```bat
e:
cd E:/learn/py/fund	# 进入到fund所在目录
python fund.py		# 运行python文件
pause				# 让屏幕停留
```

功能：可以记录日常的基金走势，然后记录数据

不足：不能够自动删除excel中的重复的数据，（如同一天的数据）


# 2. 图中图——将一幅图套娃

[迷糊老师](https://space.bilibili.com/39665558)的程序，hhh很好玩，b站[迷糊老师视频](https://www.bilibili.com/video/BV1QE411P7GV)

```python
from PIL import Image

def fill_img_with_img(imgParent, imgChild):
    imgSize =(imgParent.width*imgChild.width, imgParent.height*imgChild.height)
    imgRet = Image.new('L', imgSize, 'white') 

    i = 1 
    for w in range(imgParent.width):
        print(i)
        i += 1
        for h in range(imgParent.height):    
            if imgParent.getpixel((w, h)) < 127:
                imgRet.paste(imgChild,(w*imgChild.width, h*imgChild.height))
    return imgRet

if __name__ == '__main__':
    imgParent = Image.open('parent.jpg')
    imgParent = imgParent.convert('L')

    imgChild = Image.open('child2.png')
    imgChild = imgChild.convert('L')

    imgRet = fill_img_with_img(imgParent,imgChild)

    imgRet.save('result.png')
```

# 3. 好奇心——用程序检查哪些网站能打开

## 3.1 初步，只能检查IP地址##不成熟的探索

```python
import requests
import urllib.request
import time 
from urllib import error , request

f = open('re.txt',"w",encoding='utf-8')

j = 0
k = 0

for i in range(255):
    htmls = []
    https = []
    http = 'http://123.56.22.' + str(i)
    try:
        reponse = request.urlopen(http)
        https.append(http)
        j += 1 
        print(f'这是第{j}个网站了')
        f.write('url' + '\t' + http + '\n' )
        continue
    except error.URLError as e:
        k += 1
        print(f'访问页面出错1,{k}次了')
    except urllib.error.URLError:
        print('访问页面出错2')
# print(f'总共是{https}')
f.close()
```

## 3.2 开始加一点细节，也不太完善
