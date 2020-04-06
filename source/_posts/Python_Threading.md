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
* `args` target对应得函数得参数，用元组传入，比如`func(age,name)` `Thread(target = func , args = (13, 'name'))`
* `daemon` 主线程默认是false，，如果没有指定则继承父线程的值。True则如果主线程运行结束，该线程也停止运行；False则该线程会继续运行直到运行结束，无视主线程如何
* `group` 是预留的一个参数，用于以后扩展ThreadGroup类，现在没用

## 2.5 Thread对象

属性和方法：
* name 线程名称
* ident 线程标识符号
* daemon 是否为守护线程

___init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)
参数：
* group 无用，保留参数
* target 可调用的目标
* name 线程的名称
* args,kwargs 调用目标的参数
* daemon 是否为守护线程
* start() 开始执行
* join(timeout=None) 阻塞timeout秒，否则直到启动的线程终止前一直挂起
* is_alive () 线程是否存活
* isDaemon() 是否为守护线程
* setDaemon(daemonic) 设置为守护线程

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

threading模块的类对象

* Thread 执行线程
* Timer 在运行前等待一段时间的执行线程
* Lock 原语锁（互斥锁，简单锁）
* RLock 重入锁，使单一线程可以（再次）获得已持有的锁
* Condition 条件变量，线程需要等待另一个线程满足特定条件
* Event 事件变量，N个线程等待某个事件发生后激活所有线程
* Semaphore 线程间共享资源的寄存器
* BoundedSemaphore 与Semaphore 相似，它不允许超过初始值
* Barrie 执行线程达到一定数量后才可以继续

threading模块的函数

* activeCount() 获取当前活动中的Thread对象个数
* currentThread() 获取当前的Thread对象
* enumerate() 获取当前活动的Thread对象列表
* settrace(func) 为所有线程设置一个跟踪（trace）函数
* setprofile(func) 为所有线程设置配置文件（profile）函
* stack_size(size=None) 获取新创建线程的栈大小，也可设置线程栈的大小为size。

# 3. 线程进阶

## 3.1 派生Thread 的子类，并创建子类的实例

我们可以通过继承Thread类，派生出一个子类，使用子类来创建多线程

**记住要在子类中初始化父类的方法Thread.__init__(self) 。需要重构 run() 方法来执行多线程的程序**

```python
from threading import Thread
from time import sleep, ctime

# 创建 Thread 的子类 
class MyThread(Thread):
    def __init__(self, func, args):
        '''
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        '''
        Thread.__init__(self)   # 不要忘记调用Thread的初始化方法
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def func(name, sec):
    print('---开始---', name, '时间', ctime())
    sleep(sec)
    print('***结束***', name, '时间', ctime())

def main():
    # 创建 Thread 实例
    t1 = MyThread(func, (1, 1))
    t2 = MyThread(func, (2, 2))
    # 启动线程运行
    t1.start()
    t2.start()
    # 等待所有线程执行完毕
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
```

## 3.2 获取可调用对象的返回值

在多线程中运行的程序时与主线程分开，我们没法直接获取线程中程序的返回值。这时就可以使用派生Thread 的子类，将给过保存的实例属性中，通过一个新方法获取运行结果

```python
from threading import Thread
from time import sleep, ctime

# 创建 Thread 的子类
class MyThread(Thread):
    def __init__(self, func, args):
        '''
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        '''
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def getResult(self):
        return self.result


def func(name, sec):
    print('---开始---', name, '时间', ctime())
    sleep(sec)
    print('***结束***', name, '时间', ctime())
    return sec


def main():
    # 创建 Thread 实例
    t1 = MyThread(func, (1, 1))
    t2 = MyThread(func, (2, 2))
    # 启动线程运行
    t1.start()
    t2.start()
    # 等待所有线程执行完毕
    t1.join()
    t2.join()
    # 或线程中程序的运行结果
    print(t1.getResult())
    print(t2.getResult())


if __name__ == '__main__':
    main()
```

## 3.3 多线程的同步问题

一般在多线程代码中，总会有一些特定的函数或代码块不想被多个线程同时执行，如：修改数据库、更新文件或其他会产生程序冲突的类似情况

当任意数量的线程可以访问临界区的代码，当在同一时刻只能有一个线程可以通过时，就需要使用同步。我们可以选择合适的同步原语，也可以让线程控制机制来执行同步。

最常用的同理原语有：锁/互斥，以及信号量。锁是最简单最低级的机制。信号量用于多线程竞争有限资源的情况。

>强烈推荐[大佬的教程](https://zhuanlan.zhihu.com/p/94344847)


## 3.4 Lock 同步锁（原语锁）

### 3.4.1 同步锁的使用

**加锁 与 解锁**

```python
import threading

# 创建一个锁对象
lock = threading.Lock()

# 获得锁，加锁
lock.acquire()

# 释放锁，解锁
lock.release()
```

当我们通过 lock.acquire() 获得锁后线程程将一直执行不会中断，直到该线程 lock.release( )释放锁后线程才有可能被释放(注意：锁被释放后线程不一定会释放)

```python
import time
import threading

# 生成一个锁对象
lock = threading.Lock()


def func():
    global num  # 全局变量
    # lock.acquire()  # 获得锁，加锁
    num1 = num
    time.sleep(0.1) 
# sleep()操作，当在没有锁的情况下线程将在这里被释放出来，让给下一线程运行，而我们的num值还没有被修改，所以后面线程的num1的取值都是100
    num = num1 - 1
    # lock.release()  # 释放锁，解锁
    time.sleep(2)

num = 100
l = []

for i in range(100):  # 开启100个线程
    t = threading.Thread(target=func, args=())
    t.start()
    l.append(t)

# 等待线程运行结束. 等到线程结束后再print num
for i in l:
    i.join()

print(num)
```

注意：上面代码先将lock.acquire()和lock.release()行注释掉表示不使用锁，取消lock.acquire()和lock.release()行的注释表示使用锁

不使用锁程序运行输出为 99；使用锁程序运行结果为0

**Lock 与GIL(全局解释器锁）存在区别**

* Lock 锁的目的，它是为了保护共享的数据，同时刻只能有一个线程来修改共享的数据，而保护不同的数据需要使用不同的锁
* GIL用于限制一个进程中同一时刻只有一个线程被CPU调度，GIL的级别比Lock高，GIL是解释器级别

**GIL与Lock同时存在，程序执行如下：**

>1. 同时存在两个线程：线程A，线程B
>2. 线程A 抢占到GIL，进入CPU执行，并加了Lock，但为执行完毕，线程被释放
>3. 线程B 抢占到GIL，进入CPU执行，执行时发现数据被线程A Lock，于是线程B被阻塞
>4. 线程B的GIL被夺走，有可能线程A拿到GIL，执行完操作、解锁，并释放GIL
>5. 线程B再次拿到GIL，才可以正常执行

通过上述应该能看到，Lock 通过牺牲执行的效率换数据安全

### 3.4.2 死锁

多线程最怕的是遇到死锁，两个或两个以上的线程在执行时，因争夺资源被相互锁住而相互等待

*互锁造成死锁*

```python
import threading

# 生成一个锁对象
lock1 = threading.Lock()
lock2 = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_A()
        self.fun_B()

    def fun_A(self):
        lock1.acquire()
        print('A_1 加锁', end='\t')
        lock2.acquire()
        print('A-2 加锁', end='\t')
        time.sleep(0.1)
        lock2.release()
        print('A-2 释放', end='\t')
        lock1.release()
        print('A-1 释放')

    def fun_B(self):
        lock2.acquire()
        print('B-1 加锁', end='\t')
        lock1.acquire()
        print('B-2 加锁', end='\t')
        time.sleep(0.1)
        lock1.release()
        print('B-1 释放', end='\t')
        lock2.release()
        print('B-2 释放')

if __name__ == '__main__':
# 需要四个以上线程，才会出现死锁现象
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
```
如果两个锁同时被多个线程运行，就有可能出现死锁，如果没出现死锁，就多运行几遍就会出现死锁现象

### 3.4.3 重入锁/递归锁
`threading.RLock()`
为了支持同一个线程中多次请求同一资源，Python 提供了可重入锁(RLock)。这个RLock内部维护着一个锁(Lock)和一个计数器(counter)变量，counter 记录了acquire 的次数，从而使得资源可以被多次acquire。直到一个线程所有 acquire都被release(计数器counter变为0)，其他的线程才能获得资源。

```python
import time
import threading

# 生成一个递归对象
Rlock = threading.RLock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_A()
        self.fun_B()

    def fun_A(self):
        Rlock.acquire()
        print('A加锁1', end='\t')
        Rlock.acquire()
        print('A加锁2', end='\t')
        time.sleep(0.2)
        Rlock.release()
        print('A释放1', end='\t')
        Rlock.release()
        print('A释放2')

    def fun_B(self):
        Rlock.acquire()
        print('B加锁1', end='\t')
        Rlock.acquire()
        print('B加锁2', end='\t')
        time.sleep(3)
        Rlock.release()
        print('B释放1', end='\t')
        Rlock.release()
        print('B释放2')

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
```

当运行到程序B时，即使B休眠了3秒也不会切换线程。

使用重入锁时，counter 没有变为0(所有的acquire没有被释放掉)，即使遇到长时间的io操作也不会切换线程。

# 4. 线程实战

## 4.1 初步的练习和详细解释

