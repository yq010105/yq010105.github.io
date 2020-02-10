---
title: Hexo
date: 2020-02-04 15:34:18
tags:
    - Hexo
---

## 一、hexo基操
### master分支
* 1、新建md			
>`hexo n "title"` 
* 2、清理	
>`hexo clean`
* 3、生成
>`hexo g`
<!-- more -->
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


## 二、source/md-(blog目录下)
* 没有跳过的会转化为HTML，在blog中体现
>**所用主题 :[yilia](https://github.com/litten/hexo-theme-yilia)，主要按照[大佬博客](http://yansheng836.coding.me/)中的[这一分类](http://yansheng836.coding.me/tags/hexo/)进行修改**
## 三、source/main.0cf68a.css
### left-bg
* left-col 中<hr/>
### body-bg
* body 中
>具体修改参考[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/72a91df5.html)
### copy代码块
>按照[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/e9d1b881.html)
