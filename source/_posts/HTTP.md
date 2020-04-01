---
title: HTTP协议的介绍
date: 2020-02-13 12:50:04
categories: 学习力
summary: HTTP 协议即 Hyper Text Transfer Protocol（超文本传输协议）,是用于从万维网WWW服务器传输超文本到本地浏览器的传送协议
tags:
  - Spider
---

<!--more-->

## 1. 特点

- HTTP 基于 TCP/IP 协议：http 协议是基于 TCP/IP 协议之上的应用层协议
- HTTP 是无连接：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间
- HTTP 是基于请求－响应模式：HTTP 协议规定,请求从客户端发出,最后服务器端响应该请求并 返回
- HTTP 是无状态保存：HTTP 协议是无状态协议。无状态是指协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快

## 2. URL

HTTP 使用统一资源标识符（Uniform Resource Identifiers, URI）来传输数据和建立连接。URL 是一种特殊类型的 URI，包含了用于查找某个资源的足够的信息

**例子解析**：_http://www.aspxfans.com:8080/news/index.asp?boardID=5&ID=24618&page=1#name_

- 协议部分：该 URL 的协议部分为“http：”
- 域名部分：该 URL 的域名部分为“www.aspxfans.com”
- 端口部分：跟在域名后面的是端口，域名和端口之间使用“:”作为分隔符
- 虚拟目录部分：从域名后的第一个“/”开始到最后一个“/”为止，是虚拟目录部分。虚拟目录也不是一个 URL 必须的部分。本例中的虚拟目录是“/news/”
- 文件名部分：从域名后的最后一个“/”开始到“？”为止，是文件名部分，如果没有“?”,则是从域名后的最后一个“/”开始到“#”为止，是文件部分，如果没有“？”和“#”，那么从域名后的最后一个“/”开始到结束，都是文件名部分。本例中的文件名是“index.asp”。文件名部分也不是一个 URL 必须的部分，如果省略该部分，则使用默认的文件名
- 锚部分：从“#”开始到最后，都是锚部分。本例中的锚部分是“name”。锚部分也不是一个 URL 必须的部分
- 参数部分：从“？”开始到“#”为止之间的部分为参数部分，又称搜索部分、查询部分。本例中的参数部分为“boardID=5&ID=24618&page=1”。参数可以允许有多个参数，参数与参数之间用“&”作为分隔符

## 3. Request

![request解析图](/img/http/http_request.png)

---

**常见请求头**

- accept:浏览器通过这个头告诉服务器，他支持的数据类
- Accept-Charset:浏览器通过这个告诉服务器，他锁支持的字符集
- Accept-Encoding:浏览器通过这个告诉服务器，他支持的压缩格式
- Accept-Language:浏览器通过这个告诉服务器，他的语言环境
- Host：浏览器通过这个告诉服务器，像访问那台主机
- If-Modified-Since:浏览器通过这个头告诉服务器，缓存数据的时间
- Referer：浏览器通过这个头告诉服务器，客户机是从哪个页面来的（防盗链）
- Connection:浏览器通过这个头告诉服务器，请求完后是断开连接还是维持连接
- X-Requested-With:XMLHttpResquest 代表通过 ajax 方式进行访问的
- User-Agent:请求载体的身份标识

## 4. Response

![response解析图](/img/http/http_response.png)

---

**常见的响应头信息**

- Location：服务器通过这个头，来告诉浏览器跳转到哪里
- Server:服务器通过这个头，告诉路浏览器服务器的型号
- Content-Encoding:服务器通过这个头，告诉浏览器数据压缩的格式
- Content-Length:服务器通过这个头，告诉浏览器会送数据的长度
- Content-Language:服务器通过这个头，告诉浏览器语言环境
- Content-Type:服务器通过这个头，告诉浏览器回送数据的类型
- Refresh:服务器通过这个头，告诉浏览器定时刷新
- Content-Disposition:服务器通过这个头，告诉浏览器以下载方式打开数据
- Transfer-Encoding:服务器通过这个头，告诉浏览器数据是以块方式回送的
- Expires:-1 控制浏览器不要缓存
- Cache-Control:no-cache
- Pragma: no-cache

**响应状态码**

|     |              类别              |          原因短语          |
| :-: | :----------------------------: | :------------------------: |
| 1xx |  Informational(信息性状态码)   |     接受的请求正在处理     |
| 2xx |      Success(成功状态码)       |      请求正常处理完毕      |
| 3xx |   Redirection(重定向状态码)    | 需要进行附加操作以完成请求 |
| 4xx | Client Error(客户端错误状态码) |     服务器无法处理请求     |
| 5xx | Server Error(服务器错误状态码) |     服务器处理请求出错     |

> [百度百科详细对比表](https://baike.baidu.com/item/HTTP%E7%8A%B6%E6%80%81%E7%A0%81/5053660?fr=aladdin)

## 5. HTTPS 协议

HTTPS (Secure Hypertext Transfer Protocol)安全超文本传输协议，HTTPS 是在 HTTP 上建立 SSL 加密层，并对传输数据进行加密，是 HTTP 协议的安全版
![https](/img/http/https.png)

> [参考教程](https://www.cnblogs.com/angle6-liu/p/10459132.html)
