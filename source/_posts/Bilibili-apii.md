---
title: Bilibili_Api
date: 2020-02-15 13:26:23
tags:
    - Bilibili
---

**bilibili api 相关信息**
_有关 bilibili-api 的链接_

<!--more-->

# 1. _up 信息，名字，等级，视频总播放量，文章总浏览数_

**https://api.bilibili.com/x/space/upstat?mid=uid&jsonp=jsonp**

# 2. _up 信息，关注数，黑名单，粉丝数_

**https://api.bilibili.com/x/relation/stat?vmid=UID&jsonp=jsonp**

# 3. bilibili 某视频评论区的信息

**http://api.bilibili.com/x/v2/reply?jsonp=jsonp&;pn=页数&type=1&oid=av号**

# 4. bilibili 主页各个分区信息（信息量巨大）

**https://www.bilibili.com/index/ding.json**

# 5. bilibili 视频 av 号，弹幕，评论，收藏，硬币，分享，喜欢等基本信息

**http://api.bilibili.com/archive_stat/stat?aid=av号&type=jsonp**

# 6. bilibili 主站

**https://api.bilibili.com/x/web-interface/online?&;jsonp=jsonp**

# 7. up的粉丝数量，但有限制，最对250个

**https://api.bilibili.com/x/relation/followers?vmid=uid&pn=5&ps=0&order=desc&jsonp=jsonp**