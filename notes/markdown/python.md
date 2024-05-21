# Python

> 记录python常用操作

## 虚拟环境的使用

> 本地环境下 --- 当前目录

1. `python3 -m venv --upgrade-deps venv` 创建虚拟环境
2. `. venv/bin/activate` 激活虚拟环境

## Matplotlib

> 这是python最常用的一个图标库

### 创建图表

```python
import matplotlib.pyplot as plt
import numpy as np

# plt.plot(xpoint, ypoint, args)
# xpoint: 数据点x坐标
# ypoint: 数据点y坐标
# args: 格式化字符串，用于指定数据点的样式，如颜色、形状等


points = [(1, 3), (2, 4), (3, 1), (4, 2)]
x = [point[0] for point in points]
y = [point[1] for point in points]

################### 创建图标 ###################

# 创建一个画布， num=1 表示使用第一个画布， figsize=(6,6) 表示画布大小为6x6
fig = plt.figure(num=1,figsize=(12,6))

## 创建一个子图，111 表示子图的布局
# 111： 表示将画布分为1行1列，1：表示第一个子图
ax = fig.add_subplot(121)
ax.plot(x, y, 'o')
ax = fig.add_subplot(122)
ax.set_title('Line Plot')
ax.plot(x, y, '-')


## 显示图表
plt.show()
```

### plt常用函数

- `plt.rcParams["font.family"]="SimHei"` 防止中文标题显示错误，设置字体为黑体
- `plt.rcParams["font.size"]="30"` 设置字体大小

### ax 常用函数

- `ax.set_title('Line Plot')` 设置标题
- `ax.set_xlim(1, 7.1)` 设置x轴刻度范围
- `ax.set_ylim(1, 7.1)` 设置y轴刻度范围
- `ax.set_xticks([1, 2, 3, 4])` 设置x轴显示的刻度为[1, 2, 3, 4]
- `ax.set_yticks([1, 2, 3, 4])` 设置x轴显示的刻度为[1, 2, 3, 4]
- `ax.set_xticklabels(['a', 'b', 'c', 'd'], fontproperties="SimHei", fontsize=12, color='red')` 设置x轴标签和字体
- `ax.set_yticklabels(['a', 'b', 'c', 'd'], fontproperties="SimHei", fontsize=12, color='red') 设置y轴标签和字体`
- `ax.legend(loc=1,labelspacing=1,handlelength=1,fontsize=14,shadow=True)` 设置标签

## numpy

