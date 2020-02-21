---
title: Python_mengya_process
date: 2020-02-19 12:51:09
tags:
    - Python 
    - 萌芽杯
---

**代码的构造过程，并没有写完**
<!--more-->

# 1. 测试
## 1.1 视频经过梯度处理
```py
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
```py
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

```py
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