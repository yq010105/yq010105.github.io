---
title: Arduino学习
date: 2020-10-19 22:22:22
toc: true
categories: 学习力
summary: 单片机基础
tags:
  - 单片机
---

# 1. 入门

- 数字IO
- 模拟IO
- 串口IO

**输入设备 Input**
- 开关功能:某种状态下接通电路
类型:数字输入(开或关)

- 电位计功能:调节旋转程度
类型:模拟输入(旋转不同值不同)

- 蓝牙从功能:无线接收数据
类型:串口输入(向Arduino发送信息)

**输出设备 Output**
- LED功能:指示亮或灭
类型:数字输出

- 马达功能:转动
类型:模拟输出(调整转速)

- 蓝牙主功能:无线发送数据
类型:串口输出

![arduino入门](/img/arduino/arduino.png)

## 1.1 注释

`/* */` 注释
`int a = 0;` 要有分号结尾

```c
void setup() {
启动时/按下复位后运行一次
}
void loop() {
永远重复运行
}
```

## 1.2 变量

**变量类型**

1. `int 变量名` 整数 ，默认值为0

`int current_temperature` cdu为整数变量
`int current_temperature = 18` 赋值

整数的范围为-32,768到32,767，超过上限，返回到最下限

>[变量参考资料-太极创客](http://www.taichi-maker.com/homepage/reference-index/arduino-code-reference/)

### 1.2.1 变量的作用域

全局变量 setup和loop外
局部变量 setup中或loop中，两个不同函数中，不能互相使用


## 1.3 函数

`pinMode(LED_BUILTIN,OUTPUT);` 初始化led数字引脚为输出模式
`pinMode(13,OUTPUT)`如果UNO中LED接的引脚为13，也可以这样写
`digitalWrite(LED_BUILTIN,HIGH);` 将数字引脚写为高电平 /亮
`digitalWrite(LED_BUILTIN,LOW);`  将数字引脚写为低电平 /灭
`delay(1000);` 延时等待1秒

>[函数参考资料-太极创客](http://www.taichi-maker.com/homepage/reference-index/arduino-code-reference/)

## 1.4 数字输出

LED发光二极管
OUTPUT

## 1.5 数字输入

开关，输入信号
INPUT，识别HIGH和LOW两种状态
引脚悬空floating

`int pushButton = 2;` 给引脚2取一个名字
`pinMode(pushButton,INPUT);` 初始化2数字引脚为输入模式

`Serial.begin(9600);` 启动串口通讯 ，每秒9600位
`Serial.println(button);`显示按键状态

`int buttonState = digitalRead(pushButton);`

`digitalRead(被读引脚号码)`读取数字引脚的电平状态，返回HIGH/LOW值，1/0

## 1.6 输入上拉模式

INPUT_PULLUP

```c++
pinMode(2, INPUT_PULLUP);
pinMode(13, OUTPUT);
```

`int sensorVal = digitalRead(2)` 将开关状态数值读取到变量中

上拉模式，开关断开-高电平，开关闭合-低电平

sensorVal 高电平 - 开关断开 - 13输出LOW

```c++
if (sensorVal == HIGH) {
  digitalWrite(13, LOW);
} else {
  digitalWrite(13, HIGH);
}
```

关系运算符 ： `==`等于 `!=`不等于