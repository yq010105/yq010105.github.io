---
title: Python多线程学习
top: false
cover: false
date: 2020-04-04 18:27:32
categories: 学习力
tags:
    - Python
summary: Python中的多线程，如何使用
password:
---

<!--more -->

# 1. 初步认识多线程

>参考[廖雪峰老师的教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017627212385376)

**多进程和多线程**
我的理解就是**单个CPU**可以执行一个或多个进程，每个任务执行很短时间，从而骗过人的感觉，让我们感觉好像是多个任务一起进行，而**多核CPU**可以并行执行多任务，如果任务数量超过CPU的数量，则会让一个CPU轮流执行多个任务
每个进程，也就是每个任务中又分为很多个子任务，也就是线程，一个进程中可以启动多个线程，各个线程中的任务可以同时进行

Python中的多任务执行有三种方式：
* 多进程模式，多个python程序同时进行，每个程序一个线程
* 多线程模式，一个python程序同时进行多个线程
* 多进程+多线程，这种模型非常复杂，我的脑子不够用，就不用了

我也想要执行一个任务，直来直去，但是总有种情况，我迫不得已要多任务同时进行，我太难了
比如我做的GUI，要求可以执行多个任务，但是也要能够暂停其中的一个任务，其他任务不受干扰，好了，废话不多说了，开始学习

# 2. 线程基础

```python
# 引入线程函数threading
from threading import Thread

def fund():
    print('执行的程序')

# 增加一个线程
th = Thread(target=fund)
# 开始进程
th.start()
# 等到一个进程结束时退出
th.join()
```
>参考知乎的大佬写的教程
>作者：Dwzb
>链接：https://zhuanlan.zhihu.com/p/34004179
>来源：知乎
>著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 2.1 线程的开始

`th.start()` 可以放到循环中，同时进行多个线程

## 2.2 线程结束时停止

`th.join()` 加上这句话，则多线程只能一个结束后执行下一个
如果没有这句语句，就会直接用多线程开始执行，不会等一个结束再执行下一个

```python
from threading import Thread
t = time.time()
ths = []
for _ in range(5):
    th = Thread(target = myfun)
    th.start()
    ths.append(th)
for th in ths:
    th.join()
print(time.time() - t)
# 结果为 1.0038363933563232
```

## 2.3 线程的名称

```python
import threading
print(threading.current_thread().getName())
def myfun():
    time.sleep(1)
    print(threading.current_thread().name)
    a = 1 + 1
for i in range(5):
    th = threading.Thread(target = myfun, name = 'thread {}'.format(i))
    th.start()
# 输出结果
MainThread
thread 0
thread 1
thread 4
thread 3
thread 2
```

* `threading.current_thread()`表示当前线程，可以调用`name`或`getName()`获取线程名称
* 任何进程的都会有一个主线程，这个进程与新加的线程是相互独立的
* `Thread`表示启动一个新的线程`name`参数表示线程的名字
* `threading.current_thread().getName()`是主进程名字`MainThread`,`th.name`则是子thread名字

## 2.4 Thread函数

参数介绍：
* `target` 线程执行的函数
* `name` 线程的名称
* `args` target对应得函数得参数，用元组传入，比如`args = (3, )`
* `daemon` 主线程默认是false，，如果没有指定则继承父线程的值。True则如果主线程运行结束，该线程也停止运行；False则该线程会继续运行直到运行结束，无视主线程如何
* `group` 是预留的一个参数，用于以后扩展ThreadGroup类，现在没用

## 2.5 Thread对象

属性和方法：
* getName()  .name  获取线程名
* setName() 设置线程名
* start()  join()
* join()有一个timeout参数，表示等待这个线程结束时，如果等待时间超过这个时间，就不再等，继续进行下面的代码，但是这个线程不会被中断
* run() 也是运行这个线程，但是必须等到这个线程运行结束才会继续执行之后的代码（如果将上面的start全换成run则相当于没有开多线程）
* is_alive()如果该线程还没运行完，就是True否则False
* daemon 返回该线程的daemon
* setDaemon(True)设置线程的daemon

## 2.6 threading

* threading.currentThread(): 返回当前的线程变量
* threading.enumerate(): 返回一个包含正在运行的线程的list
* threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果