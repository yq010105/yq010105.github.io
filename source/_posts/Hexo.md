---
title: Hexo
date: 2020-02-04 15:34:18
categories: 技术力
summary: Hexo博客基本操作
tags:
  - Hexo
---

> **建立 hexo_blog，参考 b 站 up:[CodeSheep](https://space.bilibili.com/384068749)的[视频](https://www.bilibili.com/video/av44544186)**
>
> > **所用主题 :[yilia](https://github.com/litten/hexo-theme-yilia)，主要按照[大佬博客](http://yansheng836.coding.me/)中的[这一分类](http://yansheng836.coding.me/tags/hexo/)进行修改**

<!-- more -->

## 1. hexo 基操

### 1.1 master 分支

|           描述            |          代码           |
| :-----------------------: | :---------------------: |
| 新建页面&emsp;type:'tags' | `hexo new page 'title'` |
|          新建 md          |    `hexo n "title"`     |
|           清理            |      `hexo clean`       |
|           生成            |        `hexo g`         |
|  部署到远端；推到 github  |        `hexo d`         |
|       启动预览,blog       |        `hexo s`         |

### 1.2 blog 分支

- 6、将当前目录下修改的所有代码从工作区添加到暂存区 . 代表当前目录
  > `git add .`
- 7、将缓存区内容添加到本地仓库
  > `git commit -m "提交信息"`
- 8、将本地版本库推送到远程服务器,将本地库如果设置了 blog 为默认分支，可以直接 git push
  > `git push origin blog`
- 9、先将远程仓库 master 中的信息同步到本地仓库 master 中
  > `git pull origin master`
- 10、查看工作区代码相对于暂存区的差别
  > `git status`

> 参考[简书网站](https://www.jianshu.com/p/2e1d551b8261 "简书")

## 2. source/md-(blog 目录下)

- 没有跳过的会转化为 HTML，在 blog 中体现

## 3. 添加背景图片和左侧图片

主要在`source/main.0cf68a.css` 文件中修改

> 具体修改参考[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/72a91df5.html)

### 3.1 左侧背景

`themes/yilia/layout/_partial/left-col.ejs`文件中注释掉原来代码，添加新的无属性代码

```js
<!-- <div class="overlay" style="background: <%= theme.style && theme.style.header ? theme.style.header : defaultBg %>"> -->
<!-- 左侧边栏（上半部分）不设置背景颜色 -->
<div class="overlay" >
```

`themes\yilia\source\main.0cf68a.css`中修改添加背景图片

```css
.left-col {
  /* background:#fff; 注释掉原来的修改背景*/
  background: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ),
    url("http://bucket836.oss-cn-shenzhen.aliyuncs.com/wallpaper/381535373.jpeg")
      no-repeat 0% 20% / cover;
  width: 300px;
  position: fixed;
  opacity: 1;
  transition: all 0.3s ease-in;
  -ms-transition: all 0.3s ease-in;
  height: 100%;
  z-index: 999;
}
```

如果你的背景图片跟文字颜色不匹配(字看不清)，可以修改中文件

```css
 .left-col #header a {
    color:#696969
    color:#673ab7^M
 }
 .left-col #header a:hover {
    color:#b0a0aa
    color: #03A9F4^M
 }
 .left-col #header .header-subtitle {
     text-align:center;
    color:#999;
    color:#673ab7;
     font-size:18px;
```

### 3.2 文章背景

先将文章背景调成透明色,搜索`.article {`

```css
.article {
  margin: 30px;
  border: 1px solid #ddd;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
  background: rgba(255, 255, 255, 0.4); /*调成透明色，才能看清背景图片*/
  transition: all 0.2s ease-in;
}
```

然后再添加背景图片，搜索`body {`

```css
body {
  margin: 0;
  font-size: 14px;
  font-family: Helvetica Neue, Helvetica, STHeiTi, Arial, sans-serif;
  line-height: 1.5;
  color: #333;
  /*background-color:rgb(85, 144, 161); */
  min-height: 100%;
  background: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ), url(./img/1_.jpg) no-repeat 0% 20% / cover; /*添加背景图片*/
}
```

**如果修改完代码，背景还没有变，可能你的 body 或者 article 定义了两次，前面有一个 body{},后面还有一个，只要删掉后面的就可以了**
_需要自己好好的找一找_

**如果你的 main.0cf68a.css,文件代码很乱，可以在[我的 Github](https://github.com/yq010105/hexo_themes/blob/master/yilia/source/main.0cf68a.css)中复制** _别问我怎么知道的_

### 3.3 copy 代码块

> 按照[大佬博客](http://yansheng836.coding.me/)中的[这一篇](http://yansheng836.coding.me/article/e9d1b881.html)

## 4. 添加网站运行时间

_简单配置_
修改`\themes\yilia\layout\_partial\footer.ejs`，在`</footer>`上面添加如下内容

```js
<!--《添加网站运行时间 -->
<!--<br/>-->
<span id="timeDate">载入天数...</span><span id="times">载入时分秒...</span>
<script>
    var now = new Date();

    function createtime() {
        var grt = new Date("07/25/2019 12:00:00"); //此处修改你的建站时间或者网站上线时间
        now.setTime(now.getTime() + 250);
        days = (now - grt) / 1000 / 60 / 60 / 24;
        dnum = Math.floor(days);
        hours = (now - grt) / 1000 / 60 / 60 - (24 * dnum);
        hnum = Math.floor(hours);
        if (String(hnum).length == 1) {
            hnum = "0" + hnum;
        }
        minutes = (now - grt) / 1000 / 60 - (24 * 60 * dnum) - (60 * hnum);
        mnum = Math.floor(minutes);
        if (String(mnum).length == 1) {
            mnum = "0" + mnum;
        }
        seconds = (now - grt) / 1000 - (24 * 60 * 60 * dnum) - (60 * 60 * hnum) - (60 * mnum);
        snum = Math.round(seconds);
        if (String(snum).length == 1) {
            snum = "0" + snum;
        }
        document.getElementById("timeDate").innerHTML = " | 本站已安全运行 " + dnum + " 天 ";
        document.getElementById("times").innerHTML = hnum + " 小时 " + mnum + " 分 " + snum + " 秒";
    }
    setInterval("createtime()", 250);
</script>
<!-- 添加网站运行时间》 -->
```

> 参考[这一篇](http://yansheng836.coding.me/article/50902a4.html)

## 5. 看板娘(かんばんむすめ)

- **安装插件:** `npm install --save hexo-helper-live2d` **[github 项目](https://github.com/EYHN/hexo-helper-live2d)**
- **安装模型:** `npm install live2d-widget-model-模型名` **[模型名参考](https://huaji8.top/post/live2d-plugin-2.0/)**
- **在 blog/\_config.yml 中添加**
- _我在 yilia 中配置没有效果，但在 blog 中有效果_

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

- **关闭 live2D:** `enable:false`
- **卸载模型:** `npm uninstall live2d-widget-model-模型名`
- **卸载插件:** `npm uninstall hexo-helper-live2d`
- **删掉 yilia/\_config.yml 中配置**
- ~~_过于占内存，已卸载_~~、_33 真是太可爱了_
  > [2233 娘的 model](https://github.com/52cik/bilibili-haruna)
  > 参考[这一篇](http://yansheng836.coding.me/article/e239dc63.html)

## 6. 网易云音乐插件

- 在`/yilia/layout/_partial/post/left-col.ejs`中最后的`</nav>`标签上方添加

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

- 然后在 yilia 配置文件`_config.yml`中添加

```yml
# 网易云音乐插件
music:
  enable: true
  # 播放器尺寸类型(1：长尺寸、2：短尺寸)
  type: 1
  #id: 1334445174  # 网易云分享的音乐ID(更换音乐请更改此配置项)
  autoPlay: false # 是否开启自动播放
  # 提示文本(关闭请设置为false)
  text: "底部文字"
```

> 参考大佬做的[yilia-plus](https://github.com/JoeyBling/hexo-theme-yilia-plus)中的配置

## 7. 添加背景特效

### 7.1 点击爱心

- 在`/yilia/source/js/`下添加`love.js`文件,书写代码

```js
(function(window, document, undefined) {
  var hearts = [];
  window.requestAnimationFrame = (function() {
    return (
      window.requestAnimationFrame ||
      window.webkitRequestAnimationFrame ||
      window.mozRequestAnimationFrame ||
      window.oRequestAnimationFrame ||
      window.msRequestAnimationFrame ||
      function(callback) {
        setTimeout(callback, 1000 / 60);
      }
    );
  })();
  init();

  function init() {
    css(
      ".heart{width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);}.heart:after,.heart:before{content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: absolute;}.heart:after{top: -5px;}.heart:before{left: -5px;}"
    );
    attachEvent();
    gameloop();
  }

  function gameloop() {
    for (var i = 0; i < hearts.length; i++) {
      if (hearts[i].alpha <= 0) {
        document.body.removeChild(hearts[i].el);
        hearts.splice(i, 1);
        continue;
      }
      hearts[i].y--;
      hearts[i].scale += 0.004;
      hearts[i].alpha -= 0.013;
      hearts[i].el.style.cssText =
        "left:" +
        hearts[i].x +
        "px;top:" +
        hearts[i].y +
        "px;opacity:" +
        hearts[i].alpha +
        ";transform:scale(" +
        hearts[i].scale +
        "," +
        hearts[i].scale +
        ") rotate(45deg);background:" +
        hearts[i].color;
    }
    requestAnimationFrame(gameloop);
  }

  function attachEvent() {
    var old = typeof window.onclick === "function" && window.onclick;
    window.onclick = function(event) {
      old && old();
      createHeart(event);
    };
  }

  function createHeart(event) {
    var d = document.createElement("div");
    d.className = "heart";
    hearts.push({
      el: d,
      x: event.clientX - 5,
      y: event.clientY - 5,
      scale: 1,
      alpha: 1,
      color: randomColor()
    });
    document.body.appendChild(d);
  }

  function css(css) {
    var style = document.createElement("style");
    style.type = "text/css";
    try {
      style.appendChild(document.createTextNode(css));
    } catch (ex) {
      style.styleSheet.cssText = css;
    }
    document.getElementsByTagName("head")[0].appendChild(style);
  }

  function randomColor() {
    return (
      "rgb(" +
      ~~(Math.random() * 255) +
      "," +
      ~~(Math.random() * 255) +
      "," +
      ~~(Math.random() * 255) +
      ")"
    );
  }
})(window, document);
```

- 在`yilia/layout/layout.ejs`中添加代码(切记在</body>标签前添加)

```js
<!-- 《页面点击小红心 -->
<% if (theme.love){ %>
  <script type="text/javascript" src="/js/love.js"></script>
<% } %>
<!-- 页面点击小红心》 -->
```

- 在`yilia/_config.yml`中添加配置

```yml
#点击小红心
love: true
```

### 7.2 背景线条

- 在`yilia/layout/layout.ejs`中添加代码

```js
<!--动态线条背景-->
<% if (theme.canvas_nest.enable){ %>
  <script type="text/javascript" color="<%=theme.canvas_nest.color %>" opacity="<%=theme.canvas_nest.opacity %>"
      zIndex="<%=theme.canvas_nest.zIndex %>" count="<%=theme.canvas_nest.count %>"
      src="//cdn.bootcss.com/canvas-nest.js/1.0.0/canvas-nest.min.js">
  </script>
<% } %>
```

- 在`yilia/_config.yml`中添加配置

```yml
# 动态线条效果，会向鼠标集中
canvas_nest:
  enable: false
  color: "255, 235, 59" # color of lines, default: '0,0,0'; RGB values: (R,G,B).(note: use ',' to separate.)
  pointColor: "156,39,176" # color of points, default: '0,0,0'; RGB values: (R,G,B).(note: use ',' to separate.)
  opacity: "0.8" # the opacity of line (0~1), default: 0.5.
  count: "99" # the number of lines, default: 99.
  zIndex: "-1" # z-index property of the background, default: -1.
```

### 7.3 背景点击文字

- 在`yilia/source/js/`下添加`click_show_text.js`文件，添加代码

```js
var a_idx = 0;
jQuery(document).ready(function($) {
  $("body").click(function(e) {
    var a = new Array(
      "富强",
      "民主",
      "文明",
      "和谐",
      "自由",
      "平等",
      "公正",
      "法治",
      "爱国",
      "敬业",
      "诚信",
      "友善"
    );
    var $i = $("<span/>").text(a[a_idx]);
    a_idx = (a_idx + 1) % a.length;
    var x = e.pageX,
      y = e.pageY;
    $i.css({
      "z-index": 5,
      top: y - 20,
      left: x,
      position: "absolute",
      "font-weight": "bold",
      color: "#FF0000"
    });
    $("body").append($i);
    $i.animate(
      {
        top: y - 180,
        opacity: 0
      },
      3000,
      function() {
        $i.remove();
      }
    );
  });
  setTimeout("delay()", 2000);
});

function delay() {
  $(".buryit").removeAttr("onclick");
}
```

- 在`yilia/layout/layout.ejs`中添加代码

```js
<!--单击显示文字-->
<% if (theme.click_show_text){ %>
  <script type="text/javascript" src="/js/click_show_text.js"></script>
<% } %>
```

- 在`yilia/_config.yml`中添加配置

```yml
# 鼠标点击显示文字
click_show_text: false
```

> [参考博客](http://yansheng836.coding.me/article/cf9c6a5e.html)

## 8. 修改手机端的页面背景颜色，文章的背景颜色以及头像上方颜色

_在`main.0cf68a.css`中修改@media 下的模块_

### 8.1 页面背景颜色(图片)

添加下列代码，即为修改页面的背景托 i 按

```css
@media screen and (max-width: 800px) {
  body {
    background: linear-gradient(
        rgba(255, 127, 127, 0.212),
        rgba(255, 255, 255, 0.2)
      ), url(./img/phone2.jpg) no-repeat 0% 20% / cover;
  }
}
```

### 8.2 文章背景颜色

找到`@media`下的 article

```css
.article {
  margin: 30px;
  border: 1px solid #ddd;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
  background: rgba(85, 185, 185, 0.425);
  transition: all 0.2s ease-in;
}
```

根据自己喜好改变`background`属性值

### 8.3 头像图片

直接在`_config.yml`中修改，我改成了透明即`header: 'rgba(255, 127, 127, 0)'`


## 9. 给你的网页添加动态标题

在网站的开头或者结尾添加代码，我是在`layout.ejs`上添加的

```js
<script>
  var OriginTitile=document.title;
  var st;
  document.addEventListener('visibilitychange',function(){
  if(document.hidden){
      document.title="(つェ⊂)看不惹~"+OriginTitile;
      clearTimeout(st);
      console.log('hide');
  }
  else{
      document.title='(*´∇｀*)被你发现了~ '+OriginTitile;
      console.log('show');
      st=setTimeout(function(){
      document.title=OriginTitile;
      },6000);
      console.log('endChange=');
  }
  });
</script>
```