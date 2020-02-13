---
title: Hexo
date: 2020-02-04 15:34:18
tags:
    - Hexo
---
>**建立hexo_blog，参考b站up:[CodeSheep](https://space.bilibili.com/384068749)的[视频](https://www.bilibili.com/video/av44544186)**
>>**所用主题 :[yilia](https://github.com/litten/hexo-theme-yilia)，主要按照[大佬博客](http://yansheng836.coding.me/)中的[这一分类](http://yansheng836.coding.me/tags/hexo/)进行修改**
<!-- more -->

# 1. hexo基操
## 1.1 master分支
|描述|代码|
|:----:|:----:|
| 新建页面&emsp;type:'tags' |`hexo new page 'title'`|
| 新建md	|		`hexo n "title"`| 
| 清理	|`hexo clean`|
| 生成 |`hexo g`|
| 部署到远端；推到github	|`hexo d`|
| 启动预览,blog |`hexo s`| 

## 1.2 blog 分支
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


# 2. source/md-(blog目录下)
* 没有跳过的会转化为HTML，在blog中体现

# 3. source/main.0cf68a.css文件中
## 3.1 left-bg
* left-col 中<hr/>

## 3.2 body-bg
* 背景图片，先将背景调至半透明，然后添加图片
* body 中
>具体修改参考[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/72a91df5.html)

## 3.3 copy代码块
>按照[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/e9d1b881.html)

# 4. 修改建站时间
## 4.1 footer.ejs
* yilia/layout/_partial/footer.ejs
>参考[这一篇](http://yansheng836.coding.me/article/50902a4.html)

# 5. 看板娘(かんばんむすめ)
* **安装插件:**  `npm install --save hexo-helper-live2d` **[github项目](https://github.com/EYHN/hexo-helper-live2d)**
* **安装模型:**  `npm install live2d-widget-model-模型名` **[模型名参考](https://huaji8.top/post/live2d-plugin-2.0/)**
* **在yilia/_config.yml中添加**
```yml
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
* *过于占内存，已卸载*
>参考[这一篇](http://yansheng836.coding.me/article/e239dc63.html)

# 6. 网易云音乐插件
* 在`/yilia/layout/_partial/post/left-col.ejs`中最后的`</nav>`标签上方添加
```js
	<% if (theme.music && theme.music.enable){ %>
				<%# "网易云音乐插件" %>
				<%# "bottom:120px; left:auto;position:absolute;  width:85%" %>
				<% var defaultHeight = theme.music.type == 1 ? '32' : '66'; %>
				<% var defaultIframeHeight = theme.music.type == 1 ? '52' : '86'; %>
				<div>
					<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width="240" height="<%=defaultIframeHeight%>" src="//music.163.com/outchain/player?type=2&id=<%=theme.music.id||1400594005%>&auto=<%=theme.music.autoPlay?1:0%>&height=<%=defaultHeight%>"></iframe>
				</div>
				<% if (theme.music.text || theme.music.text == null){ %>
					<% var musicText = ( theme.music.text == null || theme.music.text == true ) ? "这似乎是首纯音乐，请尽情的欣赏它吧！" : theme.music.text; %>
					<p style="font-size: 24px;font-family: 'Times New Roman', Times, serif;"><%-musicText%><p>
				<% } %>
			<% } %>
```
* 然后在yilia配置文件`_config.yml`中添加
```yml
# 网易云音乐插件
music:
  enable: true
  # 播放器尺寸类型(1：长尺寸、2：短尺寸)
  type: 1 
  #id: 1334445174  # 网易云分享的音乐ID(更换音乐请更改此配置项)
  autoPlay: false  # 是否开启自动播放
  # 提示文本(关闭请设置为false)
  text: '底部文字'
```
>参考大佬做的[yilia-plus](https://github.com/JoeyBling/hexo-theme-yilia-plus)中的配置