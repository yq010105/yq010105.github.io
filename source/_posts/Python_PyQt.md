---
title: Python中PyQt库的学习
top: false
toc: true
cover: false
date: 2020-04-02 19:13:42
categories: 学习力
tags:
    - Python
summary: 学习PyQt来做GUI，因为萌芽杯的需要
password:
---

<!--more-->

**初步的代码理解**
*先会用个大概，浅显的理解*

```python
import os,sys
from PyQt5 import QtCore,QtWidgets,QtGui
import clock as cl

# 打开时的提示
def tipclock1(w):
    label = QtWidgets.QLabel(w)
    label.setGeometry(QtCore.QRect(40,300,200,45))
    label.setFont(QtGui.QFont('Roman times',15))
    label.setText('桌面表针已打开')

def tipimg1(w):
    label = QtWidgets.QLabel(w)
    label.setGeometry(QtCore.QRect(40,350,200,45))
    label.setFont(QtGui.QFont('Roman times',15))
    label.setText('图像识别已打开')

def tipdata1(w):
    label = QtWidgets.QLabel(w)
    label.setGeometry(QtCore.QRect(40,400,200,45))
    label.setFont(QtGui.QFont('Roman times',15))
    label.setText('数据分析已打开')

# 关闭时的提示
def tipclock0(w):
    label = QtWidgets.QLabel(w)
    label.setGeometry(QtCore.QRect(300,300,200,45))
    label.setFont(QtGui.QFont('Roman times',15))
    label.setText('桌面表针已关闭')

def tipimg0(w):
    label = QtWidgets.QLabel(w)
    label.setGeometry(QtCore.QRect(300,350,200,45))
    label.setFont(QtGui.QFont('Roman times',15))
    label.setText('图像识别已关闭')

def tipdata0(w):
    label = QtWidgets.QLabel(w)
    label.setGeometry(QtCore.QRect(300,400,200,45))
    label.setFont(QtGui.QFont('Roman times',15))
    label.setText('数据分析已关闭')

# 主界面
def get_gui(w):
    # 位置w，位置h，大小w，大小h
    w.setGeometry(600,300,540,500)
    w.setWindowTitle('Python')
    w.setWindowIcon(QtGui.QIcon('7.ico'))
    QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif',10))
    w.setToolTip('This is python')

    for i in range(0,3): 
        label = QtWidgets.QLabel(w)
        label.setGeometry(QtCore.QRect(40,20+i*60,220,45))
        label.setFont(QtGui.QFont('Roman times',15))
        if i == 0 :
            label.setText('打开桌面模拟表针:')
            # tipclock1(w)
            # tipclock0(w)
        elif i == 1 :
            label.setText('打开识别图像程序:')
            # tipimg1(w)
            # tipimg0(w)
        elif i == 2 :
            label.setText('打开数据分析程序:')
            # tipdata1(w)
            # tipdata0(w)
        elif i == 3 :
            label.setText('打开桌面模拟表针:')
        else :
            label.setText('打开桌面模拟表针:')
        # text = QtWidgets.QLineEdit(w)
        # text.setGeometry(QtCore.QRect(150,30,160,30))
        
        button = QtWidgets.QPushButton(w)
        button.setGeometry(QtCore.QRect(280,20+i*60,100,45))
        # button.move(150,100)
        button.setText('打开')
        if i == 0 :
            button.clicked.connect(cl.drawuse)
        
        if button.isActiveWindow:
            tipclock1(w)

        button = QtWidgets.QPushButton(w)
        button.setGeometry(QtCore.QRect(400,20+i*60,100,45))
        button.setText('关闭')
        # if i == 0 :
            # button.clicked.connect()

    w.show()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    get_gui(w)
    sys.exit(app.exec_())
```