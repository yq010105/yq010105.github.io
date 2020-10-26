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
pinMode(2, INPUT_PULLUP); - 2引脚为开关输入上拉
pinMode(13, OUTPUT); - 13引脚为输出LED
```

`int sensorVal = digitalRead(2)` 将开关状态数值读取到变量中

上拉模式:开关断开-高电平，开关闭合-低电平

sensorVal 高电平 - 开关断开 - 13输出LOW

```c++
if (sensorVal == HIGH) {
  digitalWrite(13, LOW);
} else {
  digitalWrite(13, HIGH);
}
```

关系运算符 ： `==`等于 `!=`不等于

## 1.7 boolean运算符

`&&` 与 、 `||` 或 、 `!` 非

**非**
```c++
boolean pushButton;
void setup() {
  pinMode(2,INPUT_PULLUP);
  pinMode(13,OUTPUT);
}

void loop() {
  pushButton = digitalRead(2);
/*逻辑非运算*/
  if (!pushButton) {
    digitalWrite(13, HIGH); /*pushButton 为false ，则点亮LED*/
  } else {
    digitalWrite(13, LOW);
  }
}

/*if括号中如果为1.运行if后程序，如果为0，则运行else*/
```

**与** ： 都真，才真
```c++
boolean pushButton1;
boolean pushButton2;
void setup() {
  pinMode(2,INPUT_PULLUP);
  pinMode(8,INPUT_PULLUP);
  pinMode(13,OUTPUT);
}

void loop() {
  pushButton1 = digitalRead(2);
  pushButton2 = digitalRead(8);
/*逻辑与运算*/
  if (!pushButton1 && !push Button) {
    digitalWrite(13, HIGH); /*1和2都是1，才会点亮*/
  } else {
    digitalWrite(13, LOW);
  }
}
```

**或** ：只要有一个为真，就是真


## 1.8 LED数码管

一位8段共阴极数码管

![LED数码管](/img/arduino/led.png)

不同引脚给出高电平，就能显示不同的数字

# 2. 基础知识学习

## 2.1 循环

```c++
int pinNumber = 3;
while(pinNumber <=9>){
  pinMode(pinNumber, OUTPUT);
  pinNumber = pinNumber +1;
}

/*do while*/
do{
  语句
}while(表达式);
```

```c++
for (int brightness = 0 ; brightness <=255 ; brightness++) {
  语句
}
```

## 2.2 if

```c++
  if (!pushButton) {
    digitalWrite(13, HIGH); /*pushButton 为false ，则点亮LED*/
  } else {
    digitalWrite(13, LOW);
  }

  if (!pushButton) {
    digitalWrite(13, HIGH); /*pushButton 为false ，则点亮LED*/
  } else if {
    digitalWrite(13, LOW);
  }
  else{
    语句
  }
```

## 2.3 switch...case

```c++
switch (var) {
    case 1:
        //当var等于1时执行这里的程序
        break;
    case 2:
        //当var等于2时执行这里的程序
        break;
    default:
        // 如果var的值与以上case中的值都不匹配
        // 则执行这里的程序
        break;
}
```

## 2.4 random()

`random(0,4)` 0/1/2/3随机数

## 2.5 自定义函数

不带参数
```c++
void displayClear() {
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
  digitalWrite(7,LOW);
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
} 

displayClear()  /*调用函数*/
```

带参数
```c++
void displayNumber(int ledNumber) {
  语句
}
void displayNumber(int ledNumber , long ledNumber2) {
  语句
}


/*调用*/
displayNumber(myNumber);
```

带参数，带返回值
```c++
int getRandomNumber(int minNumber, int maxNumber){
  int randomNumber;
  randomNumber = random(minNumber, maxNumber);
  return randomNumber
}
/*返回randomNumber*/

return ;
/*返回0*/
```

`randomSeed(analogRead(A0))`来自A0引脚模拟输入的数值作为随机种子

## 2.6 串口监视器

```c++
Serial.begin(9600);
Serial.print("变量的值是"); /*字符串*/
Serial.println(bianliang); /*变量*/
serial.println(""); /*空白行*/
```

## 2.7 模拟输出

可以不用`pinMode()`

`analogWrite(ledPin, brightness)`
`analogWrite(引脚编号, 参数)`

## 2.8 PWM

`analogWrite(ledPin, 127)` 50%亮度

2毫秒内，50%高电平，50%低电平

PWM脉冲宽度调制

## 2.9 电位器模拟输入

电位器，旋钮改变R1，R2比值
R1 + R2 = 固定值

3个引脚，1接地，2接输入引脚，3接5V引脚

旋钮旋转来改变第2引脚的电位，

`analogRead(引脚号码)`

`analogRead(A0)`**读取**模拟输入引脚数值，将**0-5V**的电压输入信号映射到数值**0-1023**

将5V分为1024份， 2.5V 对应数值 512
引脚输入范围可以使用analogReference()进行调整

>>[太极创客解释](http://www.taichi-maker.com/homepage/reference-index/arduino-code-reference/analogread/)

## 2.10 等比映射

`map(analogInputVal, 0 ,1023 , 0 , 255);`

将0-1023映射到0-255

# 3. 模块学习
## 3. ESP8266入门

使用arduino研究esp8266


# 4. 开始学库

## 4.1 servo

