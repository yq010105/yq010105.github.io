---
title: Hexo
date: 2020-02-04 15:34:18
tags:
    - Hexo
---
>**建立hexo_blog，参考b站up:[CodeSheep](https://space.bilibili.com/384068749)的[视频](https://www.bilibili.com/video/av44544186)**
>>**所用主题 :[yilia](https://github.com/litten/hexo-theme-yilia)，主要按照[大佬博客](http://yansheng836.coding.me/)中的[这一分类](http://yansheng836.coding.me/tags/hexo/)进行修改**
<!-- more -->

## hexo基操
### master分支
* 1、新建md			
>`hexo n "title"` 
* 2、清理	
>`hexo clean`
* 3、生成
>`hexo g`
* 4、部署到远端；推到github 			
>`hexo d`
* 5、启动预览,blog 
>`hexo s` 

### blog 分支
* 6、将当前目录下修改的所有代码从工作区添加到暂存区 . 代表当前目录
>`git add .`
* 7、将缓存区内容添加到本地仓库
>`git commit -m "提交信息"`
* 8、将本地版本库推送到远程服务器,将本地库如果设置了blog为默认分支，可以直接git push
>`git push origin blog` 
* 9、先将远程仓库master中的信息同步到本地仓库master中
>`git pull origin master`
* 10、查看工作区代码相对于暂存区的差别
>`git status` 

>参考[简书网站](https://www.jianshu.com/p/2e1d551b8261 "简书")


## source/md-(blog目录下)
* 没有跳过的会转化为HTML，在blog中体现

## source/main.0cf68a.css
### left-bg
* left-col 中<hr/>
### body-bg
* body 中
>具体修改参考[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/72a91df5.html)
### copy代码块
>按照[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/e9d1b881.html)

## 修改建站时间
### footer.ejs
* yilia/layout/_partial/footer.ejs
>参考[这一篇](http://yansheng836.coding.me/article/50902a4.html)

## 看板娘
* **安装插件:**  `npm install --save hexo-helper-live2d` **[github项目](https://github.com/EYHN/hexo-helper-live2d)**
* **安装模型:**  `npm install live2d-widget-model-模型名` **[模型名参考](https://huaji8.top/post/live2d-plugin-2.0/)**
* **在yilia/_config.yml中添加**
```
# Live2D
## https://github.com/EYHN/hexo-helper-live2d
live2d:
  enable: true
  scriptFrom: local
  pluginRootPath: live2dw/
  pluginJsPath: lib/
  pluginModelPath: assets/
  tagMode: false
  debug: false
  model:
    use: live2d-widget-model-模型名 # 模型：https://huaji8.top/post/live2d-plugin-2.0/
  display:
    position: right
    width: 150
    height: 300
  mobile:
    show: true
```
* **关闭live2D:**  `enable:false`
* **卸载模型:**  `npm uninstall live2d-widget-model-模型名`
* **卸载插件:**  `npm uninstall hexo-helper-live2d`
* **删掉yilia/_config.yml中配置**
* *过于占内存*
>参考[这一篇](http://yansheng836.coding.me/article/e239dc63.html)