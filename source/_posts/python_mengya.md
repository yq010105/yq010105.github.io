---
title: Python_mengya_process
date: 2020-02-19 12:51:09
top: true
cover: true
coverImg: /img/cover/mengya1.jpg
img: /img/cover/mengya1.jpg
categories: 技术力
summary: 识别表的指针，代码的构造过程，并没有写完（萌芽杯比赛项目）
tags:
  - Python
  - Compete
---

# 1. 测试

## 1.1 视频经过梯度处理

```python
import cv2

vc = cv2.VideoCapture('./video/1.mp4')
if vc.isOpened():
    open, frame = vc.read()
else:
    open = False

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0)
        # sobely = cv2.Sobel(gray,cv2.CV_64F,0,1)
        # sobelx = cv2.convertScaleAbs(sobelx)
        # sobely = cv2.convertScaleAbs(sobely)
        # sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
        v1 = cv2.Canny(gray,10,50)
        cv2.namedWindow('result',0)
        # cv2.imshow('result',sobelxy)
        cv2.imshow('result',v1)
        if cv2.waitKey(10) & 0xFF == 27:
            break

vc.release()
cv2.destroyAllWindows()
```

## 1.2 检测指针，绘制直线

```python
import cv2
import numpy as np
import os

img = cv2.imread('./img/clock2.jpg')    # + input('请输入文件路径：')
def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def linedraw(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # edges = cv.Canny(gray, 50, 150, apertureSize=3)
        # 自动检测可能的直线，返回的是一条条线段
    ret, thresohold = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY)
    # aussian = cv2.GaussianBlur(thresohold, (5, 5), 1) 高斯

    # kernel = np.ones((5, 5), np.uint8)  # （5，5）腐蚀大小
    # erosion = cv2.erode(thresohold, kernel, iterations=1) 去噪音点

    edges = cv2.Canny(thresohold, 10, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength=110, maxLineGap=10)
        # print(type(lines))
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255,0), 2)
    cv_show('result',image)

linedraw(img)
os.system("pause")
```

## 1.3 小综合；根据表盘识别指针并求出斜率

```python
import cv2
import numpy as np
import math

img = cv2.imread('./img/clock1.jpg', cv2.IMREAD_UNCHANGED)
# 裁剪图片  具体指针要改
imgbufen = img[70:566,0:1000]
# 将图像的阈值化 小于阈值的为max 大于阈值的为0，
# 主要是因为这个指针是黑的,圆形遮罩也是黑的，所以先把指针反转为白的
# 具体指针要改
imgfan = cv2.threshold(imgbufen,127,255,cv2.THRESH_BINARY_INV)[1]

# 输出图像
def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 得到一个圆形遮罩，返回中间圆形
def get_zhezhao(imgfan):
    #获取图片尺寸
    height, width = imgfan.shape[:2]
    height = int(height)
    width = int(width)

    #生成内显示模板
    circleIn = np.zeros((height, width, 1), np.uint8)
    circleIn = cv2.circle(circleIn, (width // 2, height // 2), min(height, width) // 2, (1), -1)

    #原图与内显示模板融合
    #生成空白图片
    imgIn = np.zeros((height, width, 4), np.uint8)
    #复制前3个通道
    imgIn[:, :, 0] = np.multiply(imgfan[:, :, 0], circleIn[:, :, 0])
    imgIn[:, :, 1] = np.multiply(imgfan[:, :, 1], circleIn[:, :, 0])
    imgIn[:, :, 2] = np.multiply(imgfan[:, :, 2], circleIn[:, :, 0])
    #设置α通道的不透明部分
    circleIn[circleIn == 1] = 1
    imgIn[:, :, 3] = circleIn[:, :, 0]
    # cv2.imwrite('./img/result1.jpg', imgIn)
    # cv_show('imgin',imgIn)
    return imgIn

# 得到线，霍夫直线
def getlines(imgIn):
    gray = cv2.cvtColor(imgIn,cv2.COLOR_BGR2GRAY)
    # cv_show("gray",gray)
    edges = cv2.Canny(gray, 10, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength=110, maxLineGap=10)
            # print(type(lines))
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # print(x1,y1,x2,y2)
        cv2.line(imgbufen, (x1, y1), (x2, y2), (0, 255,0), 2)
        # cv_show('img',imgbufen)
        floatx1.append(float(x1))
        floaty1.append(float(y1))
        floatx2.append(float(x2))
        floaty2.append(float(y2))
    # cv_show('imgline',imgbufen)
    return floatx1,floaty1,floatx2,floaty2

def get_thr_k():
    thrs = []
    ks = []
    for i in range(len(floatx1)):
        x1 = floatx1[i]
        y1 = floaty1[i]
        x2 = floatx2[i]
        y2 = floaty2[i]
        k = (y1-y2)/(x2-x1)
        thr = math.atan(k)
        thr = math.degrees(thr)
        i += 1
        ks.append(k)
        thrs.append(thr)
    return ks,thrs


imgIn = get_zhezhao(imgfan)
floatx1,floaty1,floatx2,floaty2 = [],[],[],[]
getlines(imgIn)

# print(floatx1,floaty1,floatx2,floaty2)


# 多条直线的角度列表，单条直线直接thrs[0]
thrs = get_thr_k()
print(f'直线的斜率为：{thrs[0][0]}')
print(f'直线与横线间角度值：{thrs[1][0]}')
cv_show('imgline',imgbufen)
```

## 1.4 更高级的检测指针，然后返回指针斜率

```python
import cv2
import math
import linekthr as lt
import numpy as np

def get_pointer_rad(img):
    '''获取角度'''
    shape = img.shape
    c_y, c_x, depth = int(shape[0] / 2), int(shape[1] / 2), shape[2]    # h,w,cute
    x1=c_x+c_x*1.5  # 指针长度--宽 2.5倍
    src = img.copy()
    freq_list = []
    for i in range(361):        # 算法
        x = (x1 - c_x) * math.cos(i * math.pi / 180) + c_x
        y = (x1 - c_x) * math.sin(i * math.pi / 180) + c_y
        temp = src.copy()   # 备份
        cv2.line(temp, (c_x, c_y), (int(x), int(y)), (0, 255, 0), thickness=1)  # 在temp上画线
        t1 = img.copy()
        t1[temp[:, :, 1] == 255] = 255
        c = img[temp[:, :, 1] == 255]
        points = c[c == 0]
        freq_list.append((len(points), i))
        cv2.imshow('d', temp)
        # cv2.imshow('d1', t1)
        cv2.waitKey(1)
    # key = lambda x: float(x[0])
    # keytup = max(freq_list, key=key)
    # thrth = keytup[1]
    # print(f'当前角度:{thrth}度')
    # print('当前角度：',max(freq_list, key=key),'度')
    cv2.destroyAllWindows()
    return max(freq_list, key=lambda x: x[0])

img = cv2.imread('./img/clock_re.png')
imgc = img[0:165,6:171]

def getthr():
    thres = np.random.randint(40,100)   # 随机数范围
    # print(thres)
    imgfan = cv2.threshold(imgc, thres, 255, cv2.THRESH_BINARY)[1]
    max = get_pointer_rad(imgfan)
    # lt.cv_show('imgfan',imgfan)
    # print(max)
    # exit()
    thrs = []
    thr = max[1]
    return thr

def get_averg():
    tol = 0
    h = 20          # 统计次数
    for i in range(h):
        thr = getthr()
        tol = tol + thr
        print(f'第{i+1}次的角度:{thr}')
    averg = tol / h
    return averg

print(f'角度的平均值：{get_averg()}')
```

# 2. 初步完成~~核心~~

`line_get.py`

```python
import cv2
import math
import numpy as np

# 获取指针角度值
def get_pointer_rad(img):
    shape = img.shape
    c_y, c_x, depth = int(shape[0] / 2), int(shape[1] / 2), shape[2]    # h,w,cute
    x1=c_x+c_x*1.5  # 指针长度--宽 2.5倍
    src = img.copy()
    freq_list = []
    for i in range(361):        # 算法
        x = (x1 - c_x) * math.cos(i * math.pi / 180) + c_x
        y = (x1 - c_x) * math.sin(i * math.pi / 180) + c_y
        temp = src.copy()   # 备份
        cv2.line(temp, (c_x, c_y), (int(x), int(y)), (0, 255, 0), thickness=1)  # 在temp上画线
        t1 = img.copy()
        t1[temp[:, :, 1] == 255] = 255
        c = img[temp[:, :, 1] == 255]
        points = c[c == 0]
        freq_list.append((len(points), i))
        # 可以展示匹配过程
        # cv2.imshow('d', temp)
        # cv2.imshow('d1', t1)
        # 如果要求固定检测时间不要太快，可以在这里调慢
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    return max(freq_list, key=lambda x: x[0])

def getthr(imgc):
    thres = np.random.randint(40,100)   # 随机数范围
    imgfan = cv2.threshold(imgc, thres, 255, cv2.THRESH_BINARY)[1]
    max = get_pointer_rad(imgfan)
    thr = max[1]
    return thr

def get_averg(imgc,h):
    tol = 0
    h = int(h)          # 统计次数
    for i in range(h):
        thr = getthr(imgc)
        tol = tol + thr
        # debug 看看角度是否正确统计
        # print(f'第{i+1}次的角度:{thr}')
        print(i+1,end='、')
    averg = tol / h
    return averg

if __name__ == '__main__':
    img = cv2.imread('./img/clock_re.png')
    imgc = img[0:165, 6:171]
    print(f'角度的平均值：{get_averg(imgc,5)}')
```

`xlsx_get.py`

```python
from openpyxl import Workbook
import openpyxl as xl
import cv2
import line_get as lg
import os
import time


def get_xlsx():
    # 新建xlsx或打开已有xlsx
    filex = 'data.xlsx'
    if os.path.exists(filex):
        print('--在result.xlsx中写入数据--')
        wb = xl.load_workbook('data.xlsx')
        # 文件表单定位
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        print('--新建一个data.xlsx--')
        sheet = wb['Sheet']

    # 储存数据
    ws = wb.active
    ws['A1'] = '指针角度'
    ws['B1'] = '转换角度'
    ws['C1'] = '测试时间'
    img = cv2.imread('./img/clock_re.png')
    imgh = img[0:165,6:171]

    cishu = int(input('请输入需要多少组数据--一直测则输入0--：'))
    pingjun = int(input('请输入多少组算一次平均值--推荐10--:'))

    row = 0
    if cishu == 0 or cishu < 0:
        while row >= cishu :
            maxrow = sheet.max_row
            # print(f'excel中第{maxrow + 1}行输入数据-----')
            # 测几次来算平均值 imgh,10--10次
            thr = lg.get_averg(imgh,pingjun)
            ws.cell(row=maxrow+1,column=1,value=thr)
            print(f'第{row + 1}组-----角度平均值数据：{thr}，输入到第{maxrow + 1}行中')
            if thr>0 and thr<=45:
                cdu = thr/2.25 +100
            elif thr>=135 and thr <= 360:
                cdu = (thr - 135)/2.25
            else :
                cdu = '故障'
            ws.cell(row=maxrow+1,column=2,value=cdu)
            timed = time.strftime("%H:%M:%S", time.localtime())  # %Y-%m-%d
            ws.cell(row=maxrow+1,column=3,value=timed)
            row += 1
            wb.save('result.xlsx')
    else:
        while row < cishu :
            maxrow = sheet.max_row
            # print(f'excel中第{maxrow + 1}行输入数据-----')
            # 测几次来算平均值 imgh,10--10次
            thr = lg.get_averg(imgh,pingjun)
            ws.cell(row=maxrow+1,column=1,value=thr)
            print(f'第{row + 1}组-----角度平均值数据：{thr}，输入到第{maxrow + 1}行中')
            if thr>0 and thr<=45:
                cdu = thr/2.25 +100
            elif thr>=135 and thr <= 360:
                cdu = (thr - 135)/2.25
            else :
                cdu = '故障'
            ws.cell(row=maxrow+1,column=2,value=cdu)
            timed = time.strftime("%H:%M:%S", time.localtime())  # %Y-%m-%d
            ws.cell(row=maxrow+1,column=3,value=timed)
            row += 1
            wb.save('data.xlsx')

if __name__ == '__main__':
    get_xlsx()
```

`keshihua_data.py`
**主要运行文件**

```python
import plotly.offline as ptly
import plotly.graph_objs as go
import openpyxl as xl
import xlsx_get as xg

xg.get_xlsx()
data=[]
wb = xl.load_workbook('data.xlsx')
sheet = wb['Sheet']
ws = wb.active

cdu = []
for row in ws.iter_rows(min_row=2, min_col=2,max_col=2,max_row=sheet.max_row ):
    for cell in row:
        cdu.append(cell.value)
timed = []
for row in ws.iter_rows(min_row=2, min_col=3,max_col=3,max_row=sheet.max_row ):
    for cell in row:
        timed.append(cell.value)

trace1 = go.Scatter(x = timed,
                    y = cdu,
                    mode = 'lines+markers',   #mode可选'markers','lines','lines+markers'
                    name = 'data',
                    marker = dict(size = 10,        #若设为变量则可用散点大小表示变量大小
                                  color = 'rgba(152, 0, 0, .8)',
                                  line = dict(width = 2,
                                              color = 'rgb(0, 0, 0)'
                                              ),
                                  opacity=[]
                                )
            )
data.append(trace1)
layout = go.Layout(font=dict(family='Courier New, monospace', size=18, color='#3D3D3D'),
                   title='温度值'
    )
fig = go.Figure(data=data, layout=layout)
ptly.plot(fig, filename = 'data.html')
```

# 3. 进一步优化，直接再存到 excel 同时绘制图线，达到粗略得实时

`keshihua_data_shishi.py`

- 1.实时显示，但不太美观，而且不丝滑
- 2.界面美观，但不会实时显示

```python
# import plotly.offline as ptly
# import plotly.graph_objs as go
import openpyxl as xl
from openpyxl import Workbook
import line_get as lg
import cv2
import time
import os
import matplotlib.pyplot as plt

def save_xlsx(thr,cdu,timed):
    filex = 'ssdata.xlsx'
    if os.path.exists(filex):
        print(f'--在ssdata.xlsx中写入数据--')
        wb = xl.load_workbook('ssdata.xlsx')
        # 文件表单定位
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        print('--新建一个ssdata.xlsx--')
        sheet = wb['Sheet']

    ws = wb.active
    ws['A1'] = '指针角度'
    ws['B1'] = '转换角度'
    ws['C1'] = '测试时间'

    maxrow = sheet.max_row + 1
    ws.cell(row=maxrow,column=1,value=thr)
    ws.cell(row=maxrow,column=2,value=cdu)
    ws.cell(row=maxrow,column=3,value=timed)

    wb.save('ssdata.xlsx')

def get_cts():
    filex = 'ssdata.xlsx'
    if os.path.exists(filex):
        print(f'--在ssdata.xlsx中写入数据--')
        wb = xl.load_workbook('ssdata.xlsx')
        # 文件表单定位
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        print('--新建一个ssdata.xlsx--')
        sheet = wb['Sheet']
    ws = wb.active
    cdu = []
    for row in ws.iter_rows(min_row=2, min_col=2,max_col=2,max_row=sheet.max_row ):
        for cell in row:
            cdu.append(str(cell.value))
    timed = []
    for row in ws.iter_rows(min_row=2, min_col=3,max_col=3,max_row=sheet.max_row ):
        for cell in row:
            timed.append(cell.value)
    return cdu,timed

def get_shishi(cishu,pingjun):
    img = cv2.imread('./img/clock_re.png')
    imgh = img[0:165,6:171]

    row = 0
    cts = get_cts()
    cdus = cts[0]
    timeds = cts[1]

    while row >= cishu :
        thr = lg.get_averg(imgh,pingjun)
        if thr > 0 and thr <= 45:
            cdu = thr / 2.25 + 100
        elif thr >= 135 and thr <= 360:
            cdu = (thr - 135) / 2.25
        else:
            cdu = '测试故障'
        cdus.append(str(cdu))
        timed = time.strftime("%H:%M:%S", time.localtime())
        timeds.append(timed)

        # 保存数据
        save_xlsx(thr,cdu,timed)

        # plt.figure(1)
        plt.clf()  # 清空画布上的所有内容
        fig1 = plt.figure(num='温度-时间', figsize=(20, 10), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
        plt.xlabel('Time')
        plt.ylabel('Temp')
        plt.plot(timeds, cdus, 'r-s')
        # plt.draw()  # 注意此函数需要调用
        # time.sleep(0.01)
        plt.pause(0.01)

        if len(timeds) >= 22:
            timeds = []
            cdus = []
            plt.clf()
        else :
            continue

        # # plotly 数据可视化 美观，可是不会动态
        # data = []
        # namee = str(round(cdu,1)) + '°C'
        # trace1 = go.Scatter(x=timeds,
        #                     y=cdus,
        #                     mode='lines+markers',  # mode可选'markers','lines','lines+markers'
        #                     name= namee,
        #                     marker=dict(size=10,  # 若设为变量则可用散点大小表示变量大小
        #                                 color='rgba(152, 0, 0, .8)',
        #                                 line=dict(width=2,
        #                                           color='rgb(0, 0, 0)'
        #                                           ),
        #                                 opacity=[]
        #                                 )
        #                     )
        # data.append(trace1)
        # axis_template = dict(
        #     showgrid=True,  # 网格
        #     zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
        #     nticks=20,
        #     showline=True,
        #     title='Time',
        #     mirror='all',
        #     zerolinecolor="#FF0000"
        # )
        # ayis_template = dict(
        #     showgrid=True,  # 网格
        #     zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
        #     nticks=20,
        #     showline=True,
        #     title='Temp',
        #     mirror='all',
        #     zerolinecolor="#FF0000"
        # )
        # layout = go.Layout(font=dict(family='Courier New, monospace', size=18, color='#3D3D3D'),
        #                    title='温度值' ,xaxis=axis_template,yaxis=ayis_template
        #                    )
        # fig = go.Figure(data=data, layout=layout)
        # ptly.plot(fig, filename='ssdata.html')

if __name__ == '__main__':
    get_shishi(0,5)
```

`keshihua_shishi.py`

```python
import keshihua_data_shishi as kds

cishu = 0   # 0 - 一直测
pingjun = int(input('请输入多少组算一次平均数--建议10组--:'))

while True:
    kds.get_shishi(cishu,pingjun)

```

# 4. 粗糙的整合--待优化

```python
import math
import numpy as np
import openpyxl as xl
from openpyxl import Workbook
import cv2
import time
import os
import matplotlib.pyplot as plt
import plotly.offline as ptly
import plotly.graph_objs as go

# 获取指针角度值
def get_pointer_rad(img):
    shape = img.shape
    c_y, c_x, depth = int(shape[0] / 2), int(shape[1] / 2), shape[2]    # h,w,cute
    x1=c_x+c_x*1.5  # 指针长度--宽 2.5倍
    src = img.copy()
    freq_list = []
    for i in range(361):        # 算法
        x = (x1 - c_x) * math.cos(i * math.pi / 180) + c_x
        y = (x1 - c_x) * math.sin(i * math.pi / 180) + c_y
        temp = src.copy()   # 备份
        cv2.line(temp, (c_x, c_y), (int(x), int(y)), (0, 255, 0), thickness=1)  # 在temp上画线
        t1 = img.copy()
        t1[temp[:, :, 1] == 255] = 255
        c = img[temp[:, :, 1] == 255]
        points = c[c == 0]
        freq_list.append((len(points), i))
        # 可以展示匹配过程
        # cv2.imshow('d', temp)
        # cv2.imshow('d1', t1)
        # 如果要求固定检测时间不要太快，可以在这里调慢
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    return max(freq_list, key=lambda x: x[0])

def getthr(imgc):
    thres = np.random.randint(40,100)   # 随机数范围
    imgfan = cv2.threshold(imgc, thres, 255, cv2.THRESH_BINARY)[1]
    max = get_pointer_rad(imgfan)
    thr = max[1]
    return thr

def get_averg(imgc,h):
    tol = 0
    h = int(h)          # 统计次数
    for i in range(h):
        thr = getthr(imgc)
        tol = tol + thr
        # debug 看看角度是否正确统计
        # print(f'第{i+1}次的角度:{thr}')
        print(i+1,end='、')
    averg = tol / h
    return averg


def save_xlsx(thr,cdu,timed):
    filex = 'ssdata.xlsx'
    if os.path.exists(filex):
        print(f'--在ssdata.xlsx中写入数据--')
        wb = xl.load_workbook('ssdata.xlsx')
        # 文件表单定位
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        print('--新建一个ssdata.xlsx--')
        sheet = wb['Sheet']

    ws = wb.active
    ws['A1'] = '指针角度'
    ws['B1'] = '转换角度'
    ws['C1'] = '测试时间'

    maxrow = sheet.max_row + 1
    ws.cell(row=maxrow,column=1,value=thr)
    ws.cell(row=maxrow,column=2,value=cdu)
    ws.cell(row=maxrow,column=3,value=timed)

    wb.save('ssdata.xlsx')

def get_cts():
    filex = 'ssdata.xlsx'
    if os.path.exists(filex):
        print(f'--在ssdata.xlsx中写入数据--')
        wb = xl.load_workbook('ssdata.xlsx')
        # 文件表单定位
        sheet = wb['Sheet']
    else:
        wb = Workbook()
        print('--新建一个ssdata.xlsx--')
        sheet = wb['Sheet']
    ws = wb.active
    cdu = []
    for row in ws.iter_rows(min_row=2, min_col=2,max_col=2,max_row=sheet.max_row ):
        for cell in row:
            cdu.append(str(cell.value))
    timed = []
    for row in ws.iter_rows(min_row=2, min_col=3,max_col=3,max_row=sheet.max_row ):
        for cell in row:
            timed.append(cell.value)
    return cdu,timed

def get_shishi(cishu,pingjun):
    # img = cv2.imread('./img/clock_re.png')
    imgh = cv2.imread('frame.jpg')
    # imgh = img[0:165,6:171]

    # 读取excle中数据
    cts = get_cts()
    cdus = cts[0]
    timeds = cts[1]

    row = True
    while row:
        thr = get_averg(imgh,pingjun)
        if thr > 0 and thr <= 45:
            cdu = thr / 2.25 + 100
        elif thr >= 135 and thr <= 360:
            cdu = (thr - 135) / 2.25
        else:
            cdu = '测试故障'
        cdus.append(str(cdu))
        timed = time.strftime("%H:%M:%S", time.localtime())
        timeds.append(timed)

        # 保存数据
        save_xlsx(thr,cdu,timed)


        # # plotly 数据可视化 美观，可是不会动态
        # data = []
        # cdu1 = round(cdu ,1)
        # namee = str(cdu1) + '°C'
        # trace1 = go.Scatter(x=timeds,
        #                     y=cdus,
        #                     mode='lines+markers',  # mode可选'markers','lines','lines+markers'
        #                     name= namee,
        #                     marker=dict(size=10,  # 若设为变量则可用散点大小表示变量大小
        #                                 color='rgba(152, 0, 0, .8)',
        #                                 line=dict(width=2,
        #                                           color='rgb(0, 0, 0)'
        #                                           ),
        #                                 opacity=[]
        #                                 )
        #                     )
        # data.append(trace1)
        # axis_template = dict(
        #     showgrid=True,  # 网格
        #     zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
        #     nticks=20,
        #     showline=True,
        #     title='Time',
        #     mirror='all',
        #     zerolinecolor="#FF0000"
        # )
        # ayis_template = dict(
        #     showgrid=True,  # 网格
        #     zeroline=True,  # 是否显示基线,即沿着(0,0)画出x轴和y轴
        #     nticks=20,
        #     showline=True,
        #     title='Temp',
        #     mirror='all',
        #     zerolinecolor="#FF0000"
        # )
        # layout = go.Layout(font=dict(family='Courier New, monospace', size=18, color='#3D3D3D'),
        #                    title='温度值' ,xaxis=axis_template,yaxis=ayis_template
        #                    )
        # fig = go.Figure(data=data, layout=layout)
        # ptly.plot(fig, filename='ssdata.html')
        # break

        # 实时数据，停不下来
        # plt.figure(1)
        plt.clf()  # 清空画布上的所有内容
        fig1 = plt.figure(num='温度-时间', figsize=(20, 10), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
        plt.xlabel('Time')
        plt.ylabel('Temp')
        plt.plot(timeds, cdus, 'r-s')
        # plt.draw()  # 注意此函数需要调用
        # time.sleep(0.01)
        plt.pause(0.01)

        if len(timeds) >= 22:
            timeds = []
            cdus = []
            plt.clf()
            row = False
        else :
            break


def video_show(video,ci):
    i = 1
    while True:
        ret1,frame = video.read()
        if not ret1:
            print("视频获取失败！")
            break
        framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        template = cv2.imread('./img/moban_c.jpg')
        # print(template.shape)
        # exit()
        theight , twidth = template.shape[0] , template.shape[1]
        result = cv2.matchTemplate(frame,template,cv2.TM_SQDIFF_NORMED)
        cv2.normalize(result,result,0,1,cv2.NORM_MINMAX,-1)
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

        # # min_loc：矩形定点
        # # (min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
        # # (0,0,225)：矩形的边框颜色；2：矩形边框宽度
        cv2.rectangle(frame ,min_loc ,(min_loc[0] + twidth ,min_loc[1] + theight) ,(255 ,0 ,0) ,2)
        cv2.imshow("Video_show",frame)

        choose_data = framegray[min_loc[0]:(min_loc[0] + twidth ),min_loc[1]: (min_loc[1] + theight)]
        # choose_datafan = cv2.threshold(choose_data ,110,255 ,cv2.THRESH_BINARY_INV)[1]
        cv2.imshow("choose_video",choose_data)
        if i%ci == 0 :
            cv2.imwrite(f'frame.jpg',choose_data)
            print(f'照片已保存--frame.jpg--：')
            break
        i += 1
        if cv2.waitKey(1) & 0xff == ord("e"):
            break
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    cishu = 0  # 0 - 一直测
    # pingjun = int(input('请输入多少组算一次平均数--建议2组--:'))
    pingjun = 5
    ci = 100
    # ci = int(input('请输入多少时间换一组照片--100大概3.638s左右--：'))
    while True:
        video = cv2.VideoCapture(0)
        video_show(video ,ci)
        get_shishi(cishu ,pingjun)
```

# 5. 下一步的优化

## 5.1 可以持续的调用摄像头
