---
title: Python_Opencv
date: 2020-02-18 20:42:34
summary: Python中opencv的学习和使用，可以操作图片，跟ps中知识挺像的hhh
categories: 学习力
tags:
  - Python
  - Compete
---

<!--more-->

# 0.基本知识的学习

## 0.1 基本操作

引用库
`import cv2`

cv2.IMREAD_COLOR:彩色图像 RGB 三通道
cv2.IMREAD_GRAYSCALE：灰度图像 灰度一个通道

- `img = cv2.imread('1.jpg')`打开图像----type(img) = numpy.ndarry
- `img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)`打开为灰度图像
- `cv2.imshow('image',img)`展示图像，窗口 image
- `cv2.waitKey(0)`窗口停留时间毫秒级，0 表示按任意键退出
- `cv2.destroyALLWindows()`销毁窗口
- `cv2.imwrite('result.jpg',img)`保存图像，（文件名，图片）

_可以直接定义一个函数_

```py
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyALLWindows()
```

## 0.1.1 画直线

像素点坐标，左为零，上为零
左上角为坐标原点，而坐标系是从左到右 x 符合，从上到下，y 要取负

```py
img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像
print(img.shape) # 输出：(320, 320, 3)

def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 图片，初始坐标，结束坐标，图线颜色，图线粗细
cv2.line(img,(0,100),(100,0),(0,0,255),2)
cv2.line(img,(0,200),(100,0),(0,255,0),2)
cv_show('line',img)
```

## 0.2 基本属性/函数

img.shape # (414.500.3) (h,w,rgb=3)
img.size # h\*w\*rgb
img.dtype # uint8

## 0.3 读取视频

cv2.VideoCapture 捕获摄像头

- `vc = cv2.VideoCapture('test.mp4')` 打开视频

```py
# 检查是否正确打开
if vc.isOpened():
    open. frame = vc.read()
else:
    open = False

while open:

# 播放视频 循环每一帧
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #转化为灰度
        cv2.namedWindow('result',0)
        cv2.imshow('result',gray)
        if cv2.waitKey(10) & 0xFF == 27: # 10刚刚好速度，27按esc退出
            break

vc.release()
cv2.destroyAllWindows()
```

## 0.4 感兴趣区域

图像截取

```py
img = cv.imread('1.jpg')
cat = img[0:200,0:200]
cv.show('cat',cat)
```

## 0.5 特殊选取,切分通道

b：::0
g：::1
r：::2

```py
b,g,r = cv2.split(img)  # 切分
b.shape == g.shape == r.shape

img = cv2.merge((b,g,r))    # 合并
img.shape
```

## 0.6 边界填充

图像的边界

```py
# 上下左右填充大小
import cv2

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyALLWindows()

img = cv2.imread('./img/1.jpg')
# 定义边界大小
top_size, bottom_size, left_size,right_size = (50,50,50,50)
# 复制法，复制最边缘像素
replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType = cv2.BORDER_REPLICATE)
# 反射法 对感兴趣的图像中的像素在两边进行复制  ba|abc|cb
reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType = cv2.BORDER_REFLECT)
# 反射法   edcb|abcdefgh|gfedc
reflect2 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType = cv2.BORDER_REFLECT_101)
# 外包装法  cdefgh|abcdefgh|abcdef
wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType = cv2.BORDER_WRAP)
# 常量法   常数值补充
constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType = cv2.BORDER_CONSTANT)

```

## 0.7 数值计算\图像融合\大小放缩

```py
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

img11 = img1 + 10  # [500,500,3] 中每一块都加10
img1[:5,:,0].shape 只打印前五行
img11[:5,:,0]
(img1+img11)[:5,:,0]    如果超出，则结果取余
cv2.add(img1,img11)[:5,:,0] 如果超出255，则不取余直接用255

# 图像融合

img1+img2 #shape不同，则加不了
img1.shape  # (414,500,3)
img2.shape  # (419,499,3)
img2 = cv2.resize(img2,(500,414))   # 改变大小
img2.shape  # (414,500,3)

res = cv2.addWeighted(img1,0.4,img2,0.6,0)
# res = img1*0.4+img2*0.6+0     权重


# 图像大小放缩
res = cv2.resize(img,(0,0),fx=0.5,fy=2)
```

## 0.8 图像阈值

```py
cv2.threshold():
参数：
    img:图像对象，必须是灰度图
    thresh:阈值 0~255   eg:127
    maxval：最大值  255
    type:
        cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxval
            超过阈值部分取最大值maxval=255 white，否则取0 black
            亮的地方白，暗的地方黑
        cv2.THRESH_BINARY_INV： 小于阈值的像素置为maxval，大于阈值的置为0
            亮的地方黑，暗的地方白
        cv2.THRESH_TRUNC：      小于阈值的像素不变，大于阈值的置为thresh
            指定一个截断值，大于阈值部分变成阈值，小于的不变
        cv2.THRESH_TOZERO       小于阈值的像素置0，大于阈值的不变
            大于阈值部分不变，小于的全变为0
        cv2.THRESH_TOZERO_INV   小于阈值的不变，大于阈值的像素置0
            大于阈值变为0   ，小于阈值的不变
返回两个值
    ret:阈值
    img：阈值化处理后的图像

cv2.adaptiveThreshold() 自适应阈值处理，图像不同部位采用不同的阈值进行处理
参数：
    img: 图像对象，8-bit单通道图
    maxValue:最大值
    adaptiveMethod: 自适应方法
        cv2.ADAPTIVE_THRESH_MEAN_C     ：阈值为周围像素的平均值
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 阈值为周围像素的高斯均值（按权重）
    threshType:
        cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxValuel
        cv2.THRESH_BINARY_INV:  小于阈值的像素置为maxValue，大于阈值的置为0
    blocksize: 计算阈值时，自适应的窗口大小,必须为奇数 （如3：表示附近3个像素范围内的像素点，进行计算阈值）
    C： 常数值，通过自适应方法计算的值，减去该常数值
(mean value of the blocksize*blocksize neighborhood of (x, y) minus C)
```

## 0.9 图像平滑-去掉噪音点

```py
import cv2
import numpy as np

img = cv2.imread('./img/1.jpg')

def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyALLWindows()

# 均值滤波
# 简单的平均卷积操作 # (3,3)卷积盒
blur = cv2.blur(img,(3,3))  # （奇数，奇数） 中心的值根据周围数改变

# 方框滤波
# 与均值滤波相似   normalize 是否做归一化，true与均值一样
#                                       false 会越界>255 ，所有越界值全为255
box = cv2.boxFilter(img,-1,(3,3),normalize =True)

# 高斯滤波
# 高斯模糊---正态分布，离中心值越远，值越小
aussian = cv2.GaussianBlur(img,(5,5),1)     # (5,5)的盒

# 中值滤波
# 中间的值
median = cv2.medianBlur(img,5)

# 展示所有的
# 三张图片拼接在一起
res = np.hstack((blur,aussian,median))
resv = np.vstack((blur,aussian,median))

cv_show('res',res)
```

## 0.10 形态学-腐蚀操作-去掉毛刺

边界里的盒子如果有 0 有 255，则全变为 0

```py
import numpy as np
# 去毛刺，r通道
kernel = np.ones((5,5),np.uint8)    # （5，5）腐蚀大小
erosion = cv2.erode(img,kernel,iterations = 2)  # iterations 做几次腐蚀

```

## 0.11 形态学-膨胀操作

_腐蚀后图像太细，使用膨胀_
边界里的盒子如果有 0 有 255，则全变为 255 白

```py
kernel = np.ones((3,3),np.uint8)
dilate = cv2.dilate(erosion,kernel,iterations=1)
```

## 0.12 开运算与闭运算

```py
# 开运算--先腐蚀后膨胀
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,KERNEL)

# 闭运算--先膨胀后腐蚀
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
```

## 0.13 梯度运算

```py
# 梯度运算 = 膨胀-腐蚀 = 轮廓
kernel = np.ones((7,7),np.uint8)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)  # 轮廓
```

## 0.14 礼帽 黑帽

```py
# 礼帽 = 原始输入 - 开运算 = 毛刺
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

# 黑帽 = 闭运算 - 原始输入 = 毛刺+更胖整体 - 毛刺
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

```

## 0.15 图像梯度-Sobel 算子

![sobel](/img/opencv/1.jpg)
梯度：边缘位置的像素数值不同，数值差越大，梯度越大
边缘检测，物体分辨
右减左，下减上 &emsp; 从右到左，从下至上

```py
# dst = cv2.Sobel(img,ddepth,dx,dy,ksize)
# ddepth:图像深度 -1
# dx dy：水平，竖直 1 0
# ksize：盒的大小

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 3)
# cv2.CV_64F 负数形式
# 白-黑是正数，黑-白是负数，所有负数会被截断为0，所以要取绝对值

sobelx = cv2.convertScaleAbs(sobelx)
# 取绝对值

sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 3)
# y方向
sobely = cv2.convertScaleAbs(sobely)

# x,y分别求出，再求和
sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

# 不建议直接计算，及dx，dy都为 1
# 轮廓会更加的虚

```

## 0.16 图像梯度 Scharr&&Laplacian 算子

scharr -- 更敏感 -- 描绘轮廓更细致
![sobel](/img/opencv/2.jpg)

laplacian -- 二阶导 -- 更更敏感，对噪音点敏感，很少单独使用
![sobel](/img/opencv/3.png)

```
scharrx = cv2.Scharr(img,cv2.CV_64F,1,0)
scharry = cv2.Scharr(img,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((scharrxy,laplacian))
```

三种算子区别
![三种算子区别](/img/opencv/123区别.png)

## 0.17 Canny 边缘检测--综合

- 高斯滤波器，平滑处理，滤除噪声
- 计算图像中每个像素点的梯度强度和方向
- 应用非极大值抑制，消除小的不明显的地方
  a 检测出目标可能性 90%，b 是 80%，则会抑制掉 b，把 b 丢掉
- 应用双阈值，检测来确定真实的和潜在的边缘
- 通过抑制孤立的弱边缘最终完成边缘检测

① 高斯滤波器
归一化平滑处理
② 梯度和方向，Sobel 算子
③ 非极大值抑制
a. 线性插值法
b. 简便算法;八个方向分别比较
④ 双阈值检测
maxVal|minVal
梯度值>maxVal 边界
minVal < 梯度 < maxVal 连有边界，保留，否则舍弃
梯度 < minVal 舍弃
⑤ 最终结果
canny 函数

```py
img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

v1 = cv2.Canny(img,80,150)  # minVal,maxVal
v2 = cv2.Canny(img,50,150)

```

## 0.18 图像金字塔

越往上走图像越小
图像 800\*800 变为 400\*400
各层分别提取

- 高斯金字塔（高斯滤波）

1. 向下采样，缩小，往金字塔顶走
   将偶数行和列去掉，1234 去掉 24，行列变为原来的一半
   4\*4 --- 2\*2
2. 向上采样，放大
   将数据高斯分布给周边新加列行
   2\*2 --- 4\*4

```py
img = cv2.imread('1.jpg')
# 向上
up = cv2.pyrUp(img)
# 向下
down = cv2.pyrDown(img)

# 先上 再下，，会变模糊
down_up = cv2.pyrDown(up)
```

![拉普拉斯金字塔](/img/opencv/拉普拉斯.png)

- 拉普拉斯金字塔
  原始 - 先 down 再 up = result
  result - down up = reslt1

```py
down = cv2.pyrDown(img)
down_up = cv2.pyrUp(down)
result = img - down_up
```

## 0.19 图像轮廓

图像边缘--零散
图像轮廓--完整
cv2.findContours(img,mode,method)

- mode:轮廓检测模式
  RETR_EXTERNAL 只检测外轮廓
  RETR_LIST 检索所有的轮廓，将其保存到一条链表中
  RETR_CCOMP 检索所有轮廓，并将他们组织为两层，顶层是各部分的外部边界，第二层空洞边界
  RETR_TREE（常用）检测所有轮廓，并重构嵌套轮廓的整个层次
- method:轮廓逼近方法
  CHAIN_APPROX_NONE：以 freeman 链码方式输出轮廓，其他方法输出多边形
  CHAIN_APPROX_SIMPLE：压缩水平，垂直，斜的部分

```py
img = cv2.imread('1.jpg')
gray = cv2.cvColor(img,cv2.COLOR_BGR2GRAY)
# 使用二值图像---更好的边缘检测
ret, thresh = cv2.threshold(gray,122,255,cv2.THRESH_BINARY)
# cv2.imshow('result',thresh)

binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# binary 二值图像
# contours 轮廓信息
# hierarchy 层级

# 绘制轮廓,必须先备份
draw_img = img.copy()
res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
# draw_img 原图像上绘制
# contours 轮廓信息
# -1 所有轮廓，（几个轮廓） 0 第一个轮廓外圈，1 轮廓里圈
# (0,0,255) BGR 红色的线
# 2 线条宽度--不能太大，能看出轮廓内外层差异

# 轮廓得到以后,具体轮廓拿出来，contours为list
cnt = contours[0]

# 算面积
cv2.contourArea(cnt)

# 周长 true 闭合
cu2.arcLength(cnt,True)
```

**轮廓近似**

```py
# 轮廓近似，将轮廓变得规则起来
# 用直线近似曲线,曲线上找一点，到直线的距离最大，
# d<T 可以近似     d>T,不可以直接用一条直线近似，而是分割开来，继续判断
img = cv2.imread('1.jpg')
gray = cv2.cvColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,122,255,cv2.THRESH_BINARY)
binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

draw_img = img.copy()
res = cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)

epsilon = 0.1*cv2.arcLength(cnt,True)   # 周长百分比做阈值
# 0.1百分比，越大，轮廓变化越大
approx = cv2.approxPolyDP(cnt,epsilon,True)

draw_img = img.copy()
res = cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)

```

边界矩形(外接矩形)

```py
cnt = contours[0]
# 外接矩形
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# 矩形面积
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area) / rect_area
print(f'轮廓面积与边界矩形比:{extent}')
```

外接圆

```py
(x,y).radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)
```

## 0.20 模板匹配----匹配对象在另一个图像哪里

从左到右，从上到下，进行匹配
匹配计算方法

- TM_SQDIFF----平方项匹配，值越小，越相关
- TM_CCORR-----计算相关性，值越大，越相关
- TM_CCOEFF----计算相关系数，值越大，越相关
- TM_SQDIFF_NORMED:计算归一化平方不同，越接近 0，越相关
- TM_CCORR_NORMED:计算归一化相关性，越接近 1，越相关
- TM_CCOEFF_NORMED:计算归一化的相关系数，越接近 1，越相关
- 最好用归一化的方法
  返回结果
  匹配的地方大小：
  原图结果 A\*B,模板大小 a\*b,返回结果矩阵：(A-a+1)\*(B-b+1)

```py
img = cv2.imread('1.jpg',0)
# (263,263)
template = cv2.imread('11.jpg',0)
# (110,85)
h,w = template.shape[:2]

res = cv2.matchTemplate(img,template,cv2.TM_SQDIFE)
# (154,179)

min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
# 最小值，最大值，最小值位置，最大值位置
# 该方法关注最小值位置 框左上角的点，根据res.shape画出图像

# top_left & res.shape得到最好匹配结果
top_left = min_loc
bottom_right = (top_left[0] + w,top_left[1] + h)
img2 = img.copy()
cv2.rectangle(img2,top_left,bottom_right,255,2)
# 展示出来
cv_show('res',img2)
```

匹配多个对象

```py
# 匹配多个对象
img_rgb = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('11.jpg',0)
h,w = template.shape[:2]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
# 取匹配程度大于0.8的坐标
loc = np.where(res>= threshold)
for pt in zip(*loc[::1]):   # * 表示可选参数
    bottom_right = (pt[0]+w,pt[1]+h)
    cv2.rectangle(img_rgb,pt,bootom_right,(0,0,255),2)
cv2.imshow('img',img_rgb)
cv2.waitKey(0)
```

## 0.21 直方图

图片像素的统计直方图
cv2.calcHist(img,channels,mask,histSize,ranges)
img -- 图片
channels--通道 0 -- 自动灰度图 'b' 'g' 'r'
mask--淹模图像，掩码，统计某一部分
创建掩码
mask = np.zeros(img,shape[:2],np.uint8)
选择掩码保存部分
mask[100:300,100:400] = 255 白色保存部分 # masked_img = cv2.bitwise_and(img,img,mask=mask)
hisSize -- BIN 的数目，直方图范围
ranges -- 像素值取值反围

`hist = cv2.calcHist([img],[0],None,[256],[0,256])`

```py
img =cv2.imread('1.jpg')
hist = cv2.calcHist([img],[0],None,[256],[0,256])
# 画出直方图
plt.hist(img,ravel(),256):
plt.show
```

直方图均衡化

```py
# 如果统计出来的直方图 不太平均
# 平均化
equ = cv2.equalizeHist(img)
plt.hist(equ,ravel(),256)
plt.show

# 结果更加的明显
# 一个部分分给其他部分，进行均衡
# 分模块进行均衡化
# 但有的图会出现边界
```

自适应直方图均衡化

```py
clahe = cv2.createCLAHE(clipLimit = 2.0,tileGridSize = (8，8))
res_clahe = clahe.apply(img)
cv2.imshow('result',res_clahe)
```

## 0.22 傅里叶变换

现实中的事物都是运动的
而傅里叶的频域中一切都是静止的，现实中的东西在频域中分为高频，低频

- 高频：变化剧烈的灰度分量，eg：边界
- 低频：变化缓慢的灰度变量，eg：一片大海
  ![傅里叶](/img/opencv/傅里叶.png)
  滤波
  低通滤波器：只保留低频，图像变得模糊
  高通滤波器：只保留高频，图像细节增强

在 频域中处理，更加方便

```py
cv2.dft()
# 逆变换
cv2.idft()

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg',0)
# 输入图像必须先转换成float32格式
img_float32 = np.float32(img)
# 得到的结果中 频率为0的部分在左上角，通常要转换到中心位置，用shift变换
dft = cv2.dft(img_float32,flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
# cv2.dft()返回结果是双通道的，通常还要转换为图像格式
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
```

低通：

```py
import numpy as np
import cv2
from matplotlib import pyplot as plt

def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('./img/clock1.jpg',0)
# 输入图像必须先转换成float32格式
img_float32 = np.float32(img)
# 得到的结果中 频率为0的部分在左上角，通常要转换到中心位置，用shift变换
dft = cv2.dft(img_float32,flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
# cv2.dft()返回结果是双通道的，通常还要转换为图像格式
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

rows,cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

# 要magn里面
# 创建一个掩码  zeros 全为0 全不要
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30] = 1   # 中间为低频，低频要
fshift = dft_shift*mask
# shift 回去
f_ishift = np.fft.ifftshift(fshift)

img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


plt.subplot(121), plt.imshow(img,cmap = 'gray')
plt.title('input image'), plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap = 'gray')
plt.title('magnitude spectrum'), plt.xticks([]),plt.yticks([])
plt.show()
图像模糊
```

高通

```py
import numpy as np
import cv2
from matplotlib import pyplot as plt

def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('./img/clock1.jpg',0)
# 输入图像必须先转换成float32格式
img_float32 = np.float32(img)
# 得到的结果中 频率为0的部分在左上角，通常要转换到中心位置，用shift变换
dft = cv2.dft(img_float32,flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
# cv2.dft()返回结果是双通道的，通常还要转换为图像格式
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

rows,cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

# 全为1 全要
mask = np.ones((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30] = 0   # 中间为0，中间不要，即低频不要
fshift = dft_shift*mask
# shift 回去
f_ishift = np.fft.ifftshift(fshift)

img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

# 展示
plt.subplot(121), plt.imshow(img,cmap = 'gray')
plt.title('input image'), plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap = 'gray')
plt.title('magnitude spectrum'), plt.xticks([]),plt.yticks([])
plt.show()
```

## 0.23 摄像头获取视频或图片获取感兴趣部分

```py
import cv2

def video_show():
    choose_video = False
    while True:
        ret1,frame = video.read()
        if not ret1:
            print("视频获取失败！")
            break
        cv2.imshow("Video_show",frame)
        if cv2.waitKey(1) & 0xff == ord("q"):
            # rects = []
            # fromCenter = False
            # Select multiple rectangles
            # select_data = cv2.selectROI("Image", frame, rects, fromCenter)
            select_data = cv2.selectROI("Video_show",frame)
            choose_video = True
        if choose_video :
            #获取选择框内的图像
            choose_data = frame[select_data[1]:select_data[1]+select_data[3],select_data[0]:select_data[0]+select_data[2]]
            cv2.imshow("choose_video",choose_data)
        if cv2.waitKey(1) & 0xff == ord("p"):
            break
    video.release()
    # cv2.destroyAllWindows()
    return choose_data
if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    video_show()
```

### 0.23.1 选取 roi 区域定义

```py
# 方法1：使用表示矩形区域的Rect，参数有矩形左上角坐标、矩形的长和宽
# Mat imageROI;
imageROI = image(Rect(500,250,logo.cols,logo.rows));

# 方法2：指定感兴趣的行或列的范围（Range），Range是指从起始索引到终止索引（不包括终止索引）的一段连续序列
# Mat imageROI;
imageROI = image(Range(250,250+logoImage.rows),Range(200,200+logoImage.cols));
```

# 1. 图像识别相关

## 1.1 两张图片对比

**返回一张对比后的图片**

轮子安装
`pip install pillow`
`pip install PIL`

```py
from PIL import Image
from PIL import ImageChops


def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("【+】We are the same!")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                "image must match the size of the region.使用2纬的box避免上述问题")
        print("【{0}】{1}".format(e, text))


if __name__ == '__main__':
    name1 = './对比图片/' + input('输入要对比的图片名字---带后缀格式----：')
    name2 = './对比图片/' + input('第二张图片的名字：')
    name = '对比结果' + input('你的对比结果后缀是什么：')
    compare_images(name1, name2, name)
    print('-------已完成-------')
```

> [参考教程](https://www.cnblogs.com/botoo/p/8416315.html)

# 2. 根据数据生成表格，图线

# 2.1 python 根据数据生图线

# 3. 慢慢学 opencv

[先行教程](https://www.cnblogs.com/silence-cho/p/10926248.html)

## 3.1 在新窗口打开图片，保存图片，基操

```py
import cv2

img_path = './img/' + input('输入图像路径：--带后缀--')
# 读取图片
h = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
# 创建一个窗口
cv2.namedWindow('printwindow')
cv2.namedWindow('window',0)    # 0 自由改变窗口大小

# 改变图片颜色
imgviewx = cv2.cvtColor(imgviewx,cv2.COLOR_BGR2GRAY)

# 显示图片，（窗口名，读入的图像）
cv2.imshow('printwindow',h)
# 窗口等待任意键盘按键输入，0为一直等待
cv2.waitKey(0)
# 保存图片
cv2.imwrite('./img/result.jpg',imgviewx)
# 销毁窗口
cv2.destroyAllWindows()
```

## 3.2 图像阈值化

**参数说明：**

```py
cv2.threshold():
参数：
    img:图像对象，必须是灰度图
    thresh:阈值
    maxval：最大值
    type:
        cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxval
        cv2.THRESH_BINARY_INV： 小于阈值的像素置为maxval，大于阈值的置为0
        cv2.THRESH_TRUNC：      小于阈值的像素不变，大于阈值的置为thresh
        cv2.THRESH_TOZERO       小于阈值的像素置0，大于阈值的不变
        cv2.THRESH_TOZERO_INV   小于阈值的不变，大于阈值的像素置0
返回两个值
    ret:阈值
    img：阈值化处理后的图像

cv2.adaptiveThreshold() 自适应阈值处理，图像不同部位采用不同的阈值进行处理
参数：
    img: 图像对象，8-bit单通道图
    maxValue:最大值
    adaptiveMethod: 自适应方法
        cv2.ADAPTIVE_THRESH_MEAN_C     ：阈值为周围像素的平均值
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 阈值为周围像素的高斯均值（按权重）
    threshType:
        cv2.THRESH_BINARY:     小于阈值的像素置为0，大于阈值的置为maxValuel
        cv2.THRESH_BINARY_INV:  小于阈值的像素置为maxValue，大于阈值的置为0
    blocksize: 计算阈值时，自适应的窗口大小,必须为奇数 （如3：表示附近3个像素范围内的像素点，进行计算阈值）
    C： 常数值，通过自适应方法计算的值，减去该常数值
(mean value of the blocksize*blocksize neighborhood of (x, y) minus C)
```

**例子**

```py
import cv2

imgpath = './img/' + input('输入图像路径')
imgviewx = cv2.imread(imgpath)
# 将图像转化为灰度
imgviewx = cv2.cvtColor(imgviewx,cv2.COLOR_BGR2GRAY)
# 边界设置
imgresult = cv2.copyMakeBorder(imgviewx,20,20,20,20,cv2.BORDER_DEFAULT)

ret,threl = cv2.threshold(imgviewx,127,255,cv2.THRESH_BINARY)

cv2.namedWindow('window2',0)
cv2.imshow('window2',threl)
cv2.waitKey(0)
cv2.destroyALLWindows()
```

## 3.3 图像形状变化

### 3.3.1 cv2.resize() 图像缩放

参数

```py
cv2.resize() 放大和缩小图像
    参数：
        src: 输入图像对象
        dsize：输出矩阵/图像的大小，为0时计算方式如下：dsize = Size(round(fx*src.cols),round(fy*src.rows))
        fx: 水平轴的缩放因子，为0时计算方式：  (double)dsize.width/src.cols
        fy: 垂直轴的缩放因子，为0时计算方式：  (double)dsize.heigh/src.rows
        interpolation：插值算法
            cv2.INTER_NEAREST : 最近邻插值法
            cv2.INTER_LINEAR   默认值，双线性插值法
            cv2.INTER_AREA        基于局部像素的重采样（resampling using pixel area relation）。对于图像抽取（image decimation）来说，这可能是一个更好的方法。但如果是放大图像时，它和最近邻法的效果类似。
            cv2.INTER_CUBIC        基于4x4像素邻域的3次插值法
            cv2.INTER_LANCZOS4     基于8x8像素邻域的Lanczos插值

    cv2.INTER_AREA 适合于图像缩小， cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR 适合于图像放大
```

```py
import cv2
import numpy as np

# 缩小图像为原来的一半
img = cv2.imread('messi5.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# 或者

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
```

### 3.3.2 仿射变换

仿射变换（从二维坐标到二维坐标之间的线性变换，且保持二维图形的“平直性”和“平行性”。仿射变换可以通过一系列的原子变换的复合来实现，包括平移，缩放，翻转，旋转和剪切）
**参数**

```py
cv2.warpAffine()   仿射变换（从二维坐标到二维坐标之间的线性变换，且保持二维图形的“平直性”和“平行性”。仿射变换可以通过一系列的原子变换的复合来实现，包括平移，缩放，翻转，旋转和剪切）
    参数：
        img: 图像对象
        M：2*3 transformation matrix (转变矩阵)
        dsize：输出矩阵的大小,注意格式为（cols，rows）  即width对应cols，height对应rows
        flags：可选，插值算法标识符，有默认值INTER_LINEAR，
               如果插值算法为WARP_INVERSE_MAP, warpAffine函数使用如下矩阵进行图像转dst(x,y)=src(M11*x+M12*y+M13,M21*x+M22*y+M23)
        borderMode：可选， 边界像素模式，有默认值BORDER_CONSTANT
        borderValue:可选，边界取值，有默认值Scalar()即0
```
