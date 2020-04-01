---
title: Python中plotly的学习
date: 2020-02-22 18:57:30
summary: Python中plotly轮子的用法，更加高级的可视化轮子，（更美观，更方便）
categories: 学习力
tags:
  - Python
---

**数据可视化的 plotly**

> [参考教程](https://blog.csdn.net/weixin_34407348/article/details/91371969)

<!--more-->

# 1. 基本操作，初步理解代码

```py
# 生成一个直方图
import plotly.offline as ptly
import plotly.graph_objs as go

data=[]
trace1 = go.Bar(x=['first','second','third'],
                y=[20,40,30]
    )
data.append(trace1)
layout = go.Layout(font=dict(family='Courier New, monospace', size=18, color='#3D3D3D'),
                   title='example'
    )
fig = go.Figure(data=data, layout=layout)
ptly.plot(fig, filename = 'example.html')
```

或者用 dict 表示

```py
trace1 = {'type':'bar',
          'x':['first','second','third'],
          'y':[20,40,30]
    }
```

# 2. 图形属性`

## 2.1 柱状图

```py
trace1 = go.Bar(x=[],
                y=[],
                name='thename',
                width=0.5,
                marker=dict(color="#c45ca2"),
                opacity=1
            )
```

## 2.2 饼图

```py
trace1 = go.Pie(labels=[],
                values=[],
                hoverinfo='label+percent',
                textinfo='value',
                textfont=dict(size=20),
                marker=dict(colors=colors,
                           line=dict(color='#000000', width=2)),
                hole= .4,
                name="pie name",
                domain=dict(x = [0, .48]),
                opacity=1
            )
```

## 2.3 散点图，折线图

```py
trace1 = go.Scatter(x = [],
                    y = [],
                    mode = 'markers',   #mode可选'markers','lines','lines+markers'
                    name = 'the name',
                    marker = dict(size = 10,        #若设为变量则可用散点大小表示变量大小
                                  color = 'rgba(152, 0, 0, .8)',
                                  line = dict(width = 2,
                                              color = 'rgb(0, 0, 0)'
                                              ),
                                  opacity=[]
                                )
            )
```

# 3. 布局属性

```py
# 通用
layout = go.Layout(title='your title',  #大标题
                   font=dict(
                     family='Courier New, monospace',
                     size=18,
                     color='#3D3D3D'
                               ),#字体
                   width=1400,
                   height=800,              #图形的大小
                   margin=go.Margin(
                                    l=100,
                                    r=100,
                                    b=200,
                                    t=200,
                                    pad=0
                                    ),      #边距设置
                   plot_bgcolor='#ffffff',   #绘图部分背景颜色
                   paper_bgcolor='#ffffff',   #整体背景颜色
                   showlegend=True,        #是否显示图例，也可放在每个trace里单独设置
                   #图例相关参数设置：
                   legend=dict(orientation="v",
                                x=0,
                                y=1,
                                traceorder='normal',
                                font=dict(
                                        family='sans-serif',
                                        size=12,
                                        color='#000'
                                            ),
                                bgcolor='#E2E2E2',
                                bordercolor='#FFFFFF',
                                borderwidth=2
                            ),
                   #x轴相关参数设置（y轴对应yaxis）：
                   xaxis=dict(title='x Axis',
                              titlefont=dict(
                                        family='Courier New, monospace',
                                        size=18,
                                        color='#7f7f7f'
                                            ),
                               range=[],   #x轴范围，如[0,30]
                               type='-',
                              #x轴类型，可选["-","linear","log","date","category"]
                               domain=[0,0.45]
                              #设置x轴在整个图像占的位置范围（主要在有多张图时使用，第二个图用xaxis2设置相关参数）
                            )
    )


# 柱状图
layout = go.Layout(bargap=0.3,      #0~1
                   bargroupgap=0.1,  #0~1
                   barmode='',
                   #barmode: ["stack","group","overlay","relative"],设置多个trace的组合方式
                   barnorm=''
    )
```

## 3.1 设置坐标轴

```py
axis_template=dict(
    showgrid=True,  #网格
    zeroline=True,  #是否显示基线,即沿着(0,0)画出x轴和y轴
    nticks=20,
    showline=True,
    title='X axis',
    mirror='all',
    zerolinecolor="#FF0000"
)
layout=go.Layout(
    xaxis=axis_template,
    yaxis=axis_template
)
```

> [原文链接](https://blog.csdn.net/u012897374/article/details/77857980)

# 4. 图像整体属性

```py
ptly.plot(figure_or_data, show_link=True, link_text='Export to plot.ly',
         validate=True, output_type='file', include_plotlyjs=True,
         filename='temp-plot.html', auto_open=True, image=None,
         image_filename='plot_image', image_width=800, image_height=600,
         config=None)s
```

# 5. 数据处理

**包括 aggregate,filter,groupby,sort**

```py
# aggregate
transforms = [dict(
    type = 'aggregate',
    groups = [],        #用于分组的数组
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True),
    ]
  )]
"""
func参数可用：
"count","sum","avg","median","mode","rms","stddev","min","max","first","last"
"""

# filter
transforms = [dict(
    type = 'filter',
    target = 'y',
    operation = '>',
    value = 4
  )]
"""
operation参数可用:
"=","!=","<",">=",">","<=","[]","()","[)","(]","][",")(","](",")[","{}","}{"
"""

# groupby
transforms = [dict(
    type = 'groupby',
    groups = [],     #用于分组的数组
    styles = [
        dict(target = 'Moe', value = dict(marker = dict(color = 'blue'))),
        dict(target = 'Larry', value = dict(marker = dict(color = 'red'))),
        dict(target = 'Curly', value = dict(marker = dict(color = 'black')))
    ]
  )]

# sort
transforms = [dict(
    type = 'sort',
    target = 'x',
    order = 'ascending'   #升序ascending，降序descending
  )]
```
