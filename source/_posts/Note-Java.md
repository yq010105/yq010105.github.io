---
title: Java-Note
date: 2020-02-15 19:58:04
toc: true
categories: 学习力
summary: Java 语言学习笔记本
tags:
  - Java
  - Note
---

<!--more-->

> [java 参考学习教程](https://www.runoob.com/java/java-basic-syntax.html)

## 1. java 基础语法

- _对象_：对象是类的一个实例，有状态和行为。例如，一条狗是一个对象，它的状态有：颜色、名字、品种；行为有：摇尾巴、叫、吃等
- _类_：类是一个模板，它描述一类对象的行为和状态
- _方法_：方法就是行为，一个类可以有很多方法。逻辑运算、数据修改以及所有动作都是在方法中完成的
- _实例变量_：每个对象都有独特的实例变量，对象的状态由这些实例变量的值决定

### 1.1 java 程序`HelloWorld.java`

```java
public class HelloWorld {
    /* 第一个Java程序
     * 它将打印字符串 Hello World
     */
    public static void main(String []args) {
        System.out.println("Hello World"); // 打印 Hello World
    }
}
# Hello World
```

**cmd 窗口**
`javac HelloWorld.java --调试`
`java Helloworld --运行`

### 1.2 基本语法

- 大小写敏感：Java 是大小写敏感的，这就意味着标识符 Hello 与 hello 是不同的
- 类名：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 MyFirstJavaClass
- 方法名：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写
- 源文件名.java：源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 .java。（如果文件名和类名不相同则会导致编译错误）
- 主方法入口：所有的 Java 程序由 `public static void main(String []args)` 方法开始执行

### 1.3 java 标识符

_Java 所有的组成部分都需要名字。类名、变量名以及方法名都被称为标识符_

- 所有的标识符都应该以字母（A-Z 或者 a-z）,美元符（\$）、或者下划线（\_）开始
- 首字符之后可以是字母（A-Z 或者 a-z）,美元符（\$）、下划线（\_）或数字的任何字符组合
- 关键字不能用作标识符
- 标识符是大小写敏感的
- 合法标识符举例：age、\$salary、\_value、\_\_1_value
- 非法标识符举例：123abc、-salary

### 1.4 java 修饰符

_像其他语言一样，Java 可以使用修饰符来修饰类中方法和属性。主要有两类修饰符_

- 访问控制修饰符 : default, public , protected, private
- 非访问控制修饰符 : final, abstract, static, synchronized

### 1.5 java 变量

- 局部变量
- 类变量--静态变量
- 成员变量--非静态变量

### 1.6 java 数组

_数组是储存在堆上的对象，可以保存多个同类型变量_

### 1.7 java 枚举

_Java 5.0 引入了枚举，枚举限制变量只能是预先设定好的值。使用枚举可以减少代码中的 bug_
_例如，我们为果汁店设计一个程序，它将限制果汁为小杯、中杯、大杯。这就意味着它不允许顾客点除了这三种尺寸外的果汁_

```java
class FreshJuice {
   enum FreshJuiceSize{ SMALL, MEDIUM , LARGE }
   FreshJuiceSize size;
}

public class FreshJuiceTest {
   public static void main(String []args){
      FreshJuice juice = new FreshJuice();
      juice.size = FreshJuice.FreshJuiceSize.MEDIUM  ;
   }
}
```

### 1.7.1 java 关键字(不可以用于变量)

|         类别         |    关键字    |           说明           |
| :------------------: | :----------: | :----------------------: |
|       访问控制       |   private    |          私有的          |
|                      |  protected   |         受保护的         |
|                      |    public    |          公共的          |
| 类、方法和变量修饰符 |   abstract   |         声明抽象         |
|                      |    class     |            类            |
|                      |   extends    |        扩充，继承        |
|                      |    final     |    最终值，不可改变的    |
|                      |  implements  |       实现（接口）       |
|                      |  interface   |           接口           |
|                      |    native    |      本地，原生方法      |
|                      |     new      |         新，创建         |
|                      |    static    |           静态           |
|                      |   strictfp   |        严格，精准        |
|                      | synchronized |        线程，同步        |
|                      |  transient   |           短暂           |
|                      |   volatile   |          易失的          |
|     程序控制语句     |    break     |         跳出循环         |
|                      |     case     | 定义一个值供 switch 选择 |
|                      |   continue   |           继续           |
|                      |   default    |           默认           |
|                      |      do      |           运行           |
|                      |     else     |           否则           |
|                      |     for      |           循环           |
|                      |      if      |           如果           |
|                      |  instanceof  |           实例           |
|                      |    return    |           返回           |
|                      |    switch    |      根据值选择执行      |
|                      |    while     |           循环           |
|       错误处理       |    assert    |    断言表达式是否为真    |
|                      |    catch     |         捕捉一场         |
|                      |   finally    |     有没有异常都执行     |
|                      |    throw     |     抛出一个异常对象     |
|                      |    throws    |  声明一个异常可能被抛出  |
|                      |     try      |         捕获异常         |
|        包相关        |    impot     |           引入           |
|                      |   package    |            包            |
|       基本类型       |   boolean    |          布尔型          |
|                      |     byte     |          字节型          |
|                      |     char     |          字符型          |
|                      |    double    |        双精度浮点        |
|                      |    float     |        单精度浮点        |
|                      |     int      |           整型           |
|                      |     long     |          长整型          |
|                      |    short     |          短整型          |
|       变量引用       |    super     |        父类。超类        |
|                      |     this     |           本类           |
|                      |     void     |         无返回值         |
|      保留关键字      |     goto     |   是关键字，但不能使用   |
|                      |    const     |   是关键字，但不能使用   |
|                      |     null     |            空            |

### 1.8 java 注释

```java
/*多行
*注释
*/

// 单行注释
/*单行注释*/
```

### 1.9 java 空行----忽略

### 1.10 继承

- 在 Java 中，一个类可以由其他类派生。如果你要创建一个类，而且已经存在一个类具有你所需要的属性或方法，那么你可以将新创建的类继承该类
- 利用继承的方法，可以重用已存在类的方法和属性，而不用重写这些代码。被继承的类称为超类（super class），派生类称为子类（subclass）

### 1.11 接口

- 在 Java 中，接口可理解为对象间相互通信的协议。接口在继承中扮演着很重要的角色
- 接口只定义派生要用到的方法，但是方法的具体实现完全取决于派生类

### 1.12 java 源程序与编译型运行区别

![java_pic](/img/java/java.png)

## 2. 对象和类

_一个群体中有很多 boy 和 girl_
_其中 boy 和 girl 为类 class，而具体的每个人为该类的对象_

### 2.1 java 中的类

```java
public class Dog{
  String breed;
  int age;
  String color;
  void barking(){
  }

  void hungry(){
  }

  void sleeping(){
  }
}
```

一个类中可以包含一下类型的变量：

- 局部变量：在方法、构造方法或者语句块中定义的变量被称为局部变量。变量声明和初始化都是在方法中，方法结束后，变量就会自动销毁
- 成员变量：成员变量是定义在类中，方法体之外的变量。这种变量在创建对象的时候实例化。成员变量可以被类中方法、构造方法和特定类的语句块访问
- 类变量：类变量也声明在类中，方法体之外，但必须声明为 static 类型
  一个类可以拥有多个方法，在上面的例子中：barking()、hungry()和 sleeping()都是 Dog 类的方法

### 2.2 构造方法

- 每个类都有构造方法。如果没有显式地为类定义构造方法，Java 编译器将会为该类提供一个默认构造方法。
- 在创建一个对象的时候，至少要调用一个构造方法
- 构造方法的名称必须与类同名，一个类可以有多个构造方法

```java
public class Puppy{
    public Puppy(){
    }

    public Puppy(String name){
        // 这个构造器仅有一个参数：name
    }
}
```

### 2.3 创建对象

_对象是根据类创建的。在 Java 中，使用关键字 new 来创建一个新的对象_

- 声明：声明一个对象，包括对象名称和对象类型
- 实例化：使用关键字 new 来创建一个对象
- 初始化：使用 new 创建对象时，会调用构造方法初始化对象

```java
public class Puppy{
   public Puppy(String name){
      //这个构造器仅有一个参数：name
      System.out.println("小狗的名字是 : " + name );
   }
   public static void main(String[] args){
      // 下面的语句将创建一个Puppy对象
      Puppy myPuppy = new Puppy( "tommy" );
   }
}
```
