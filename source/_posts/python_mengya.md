---
title: Python_mengya
date: 2020-02-19 12:51:09
tags:
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